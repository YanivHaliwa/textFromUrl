#!/usr/bin/env python3
import os
import sys
import requests
from bs4 import BeautifulSoup
import re
import shutil
from datetime import datetime
from requests.exceptions import ConnectionError, RequestException
from collections import OrderedDict

# Get the current directory and set up the textfiles directory
current_dir = os.getcwd()
textfiles = os.path.join(current_dir, "textFromUrl")

# Ensure the textfiles directory exists
os.makedirs(textfiles, exist_ok=True)

def extract_text_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    except ConnectionError:
        print(f"Failed to connect to this website or the URL is not correct")
        return None
    except RequestException as e:
        print(f"An error occurred: {e}")
        return None

    # Remove scripts and styles
    for script in soup(["script", "style"]):
        script.decompose()

    # Remove unwanted elements
    excluded_substrings = ['menu', 'button', 'flex', 'img', 'comment', 'footer', 'nav', 'feedback', 'image']
    for tag in soup.find_all():
        if tag.attrs and 'class' in tag.attrs:
            if any(excluded in ' '.join(tag.get('class', [])) for excluded in excluded_substrings):
                tag.decompose()

    # Extract and clean text
    text = soup.get_text(separator='\n', strip=True)
    lines = (line.strip() for line in text.splitlines())
    text = '\n'.join(line for line in lines if line)

    # Remove duplicate lines
    text = '\n'.join(OrderedDict.fromkeys(text.splitlines()))

    # Format for terminal display
    term_width = shutil.get_terminal_size((80, 20)).columns
    newtext = "\n".join(line.rjust(term_width) for line in text.split("\n"))

    if text:
        print(newtext)
    else:
        print("This website does not show any text or does not allow scraping.")

    # Prepare filename
    title = soup.title.string if soup.title else "No Title"
    title = re.sub(r'[^\w\s-]', '_', title).strip()[:50]  # Limit title length
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{title}_{timestamp}.txt"

    # Write to file
    file_path = os.path.join(textfiles, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(newtext)

    return filename

if __name__ == "__main__":
    website = input("Enter URL: ")
    filename = extract_text_from_url(website)
    
    if filename:
        file_path = os.path.join(textfiles, filename)
        try:
            with open(file_path, "r", encoding='utf-8') as f:
                file_content = f.read()
            print(f"\nContent saved to: {file_path}")
        except IOError as e:
            print(f"Error reading file: {e}")
    else:
        print("Failed to extract content from the URL.")