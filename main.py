import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Set the user whose tweets you want to scrape
username = "elonmusk"

# Set the number of scrolls for loading more tweets (approximately 20 tweets per scroll)
scrolls = 10

# Set the Samsung refrigerator user agent
user_agent = "Mozilla/5.0 (Linux; Tizen 3.0; SAMSUNG Family Hub) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.0 Safari/537.36"

# Initialize the Chrome WebDriver with the custom user agent
options = Options()
options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(chrome_options=options)
driver.get(f"https://twitter.com/{username}")

# Wait for the tweets to load
time.sleep(2)

# Scroll the page to load more tweets
for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Find all the tweet elements on the page
tweets = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')

# Dictionary to store the tweets
tweets_dict = {}

# Extract and store the tweet text and date
for tweet in tweets:
    try:
        tweet_text = tweet.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
        tweet_date = tweet.find_element_by_xpath('.//div[2]/div[1]/div[1]/div[2]/time').get_attribute("datetime")
        tweet_date_obj = datetime.fromisoformat(tweet_date[:-1])  # Remove the 'Z' at the end of the datetime string
        date_key = f"{username}-{tweet_date_obj.month}-{tweet_date_obj.day}-{tweet_date_obj.year}"
        
        if date_key not in tweets_dict:
            tweets_dict[date_key] = [tweet_text]
        else:
            tweets_dict[date_key].append(tweet_text)
    except Exception as e:
        print(f"Error: {e}")

# Close the driver
driver.close()

# Save the tweets dictionary as a JSON file
with open(f"{username}_tweets.json", "w") as outfile:
    json.dump(tweets_dict, outfile, indent=4)