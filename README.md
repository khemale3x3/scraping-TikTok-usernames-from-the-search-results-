# scraping-TikTok-usernames-from-the-search-results-
This script automates the process of scraping TikTok usernames from the search results using Selenium WebDriver. It searches for UGC example videos and extracts the usernames of content creators.


How the Script Works
Set up Selenium WebDriver

Uses webdriver_manager to install and manage the ChromeDriver.
Configures headless mode to run without opening a browser.
Opens the TikTok search URL for UGC example videos.
Load the Page and Scroll

Waits 5 seconds for the page to load.
Scrolls 100 times to load more results (can be adjusted).
Uses JavaScript (execute_script) to scroll down.
Extract Usernames

Finds all elements containing usernames using XPath:
//p[@data-e2e='search-card-user-unique-id']
Stores unique usernames in a list.
Create TikTok Profile URLs

Converts each username into a TikTok profile URL.
Save Data to CSV

Saves the usernames and profile links in tiktok_ugc_users.csv.
Prints Success Message

Displays the total number of scraped usernames.
