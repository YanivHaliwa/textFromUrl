# TextFromUrl: Web Content Extraction Tool

This repository contains a Python script for extracting and cleaning text content from web pages. It's designed to scrape textual information from URLs, removing unnecessary elements and formatting the output for easy reading and analysis.


## Key Use Cases

1. **AI Text Analysis**: Extract clean text data from web pages to feed into AI models for analysis, summarization, or other natural language processing tasks.
2. **Research Data Collection**: Quickly gather text content from multiple web sources for academic or market research.
3. **Content Aggregation**: Compile text from various websites for content curation or comparison.
4. **SEO Analysis**: Extract main content from web pages for search engine optimization analysis.
5. **Web Archiving**: Save text content from websites for archival purposes or offline reading.
6. **Data Preprocessing for Machine Learning**: Prepare web content as input data for machine learning models, especially in text classification or sentiment analysis tasks.
7. **Competitive Analysis**: Gather and analyze text content from competitor websites.
8. **Legal or Compliance Reviews**: Extract text from websites for legal audits or compliance checks.

**for more scripts related cyber and securiy check here: [Cyber Security Scripts section](https://github.com/YanivHaliwa/Linux-Stuff/blob/master/README.md#cyber-security-scripts).**

### Features:

- Extracts text content from specified URLs
- Removes scripts, styles, and other non-content elements
- Filters out common UI elements (menus, buttons, footers, etc.)
- Eliminates duplicate lines and unnecessary whitespace
- Saves extracted text to timestamped files
- Provides terminal output of extracted content


### Usage:

Run the script and enter the URL when prompted:
```python3 urlscrap.py```

### Output:

- Displays extracted text in the terminal
- Saves text to a file in the `texts/` directory
- Filename format: `[Page_Title]_[Timestamp].txt`

## How It Works:

1. Sends a request to the specified URL with a user agent to mimic a browser
2. Parses the HTML content using BeautifulSoup
3. Removes script, style, and other non-content elements
4. Filters out elements with class names containing specified substrings
5. Extracts and cleans the remaining text content
6. Formats the text for terminal display and file saving

## Requirements:

- Python 3
- BeautifulSoup4
- Requests

Install dependencies:
```pip install beautifulsoup4 requests```

## Notes:

- Some websites may block or limit scraping attempts
- Always respect robots.txt and website terms of service
- The script may not work perfectly on all websites due to varying structures

## Ethical Use:

This tool should be used responsibly and ethically. Ensure you have the right to scrape content from the websites you target. Respect copyright and terms of service of the websites you interact with.

## Disclaimer:

The developers of this tool are not responsible for any misuse or for any damages that may result from the use of this tool. Use at your own risk and discretion.