# Twitter Scraping with Selenium and Chrome WebDriver

This script scrapes tweets from a user's timeline using Python, Selenium, and the Chrome WebDriver using a Samsung refrigerator user agent. It then stores the tweets in a dictionary with keys in the format `author-month-day-year` and saves the dictionary as a JSON file.

This was created as a demonstration to show how stupid API restrictions are for reading tweets.

## Prerequisites

1. Python 3.x installed on your system.
2. Google Chrome browser installed on your system.

## Installation

1. Install Selenium:


pip install selenium


2. Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and add it to your system's PATH.

## Usage

1. Replace the `username` variable in the script with the desired user's Twitter handle.

2. Adjust the number of `scrolls` in the script to load more tweets.

3. Run the script:

python twitter_scraper.py


4. The script will save the tweets in a JSON file named `{username}_tweets.json` in the same directory as the script.
