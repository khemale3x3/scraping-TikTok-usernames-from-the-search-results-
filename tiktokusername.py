from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Define TikTok Search URL
url = "https://www.tiktok.com/search?q=UGC%20example%220video%20us&t=1739768599900"

# Set up Selenium WebDriver
options = Options()
options.add_argument("--headless")  # Run in headless mode (remove if you want to see the browser)
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Scroll to load more results
for _ in range(100):  # Adjust the number of scrolls if needed
    driver.execute_script("window.scrollTo(10, document.body.scrollHeight);")
    time.sleep(5)  # Give time for content to load

# Find all elements containing usernames using data-e2e attribute
user_elements = driver.find_elements(By.XPATH, "//p[@data-e2e='search-card-user-unique-id']")

# Extract text (usernames) from elements
usernames = list(set([user.text.strip() for user in user_elements if user.text.strip()]))

# Close the browser
driver.quit()

# Convert usernames to TikTok profile URLs
df = pd.DataFrame({'Username': usernames})
df['Tiktok URL'] = df['Username'].apply(lambda x: f"https://www.tiktok.com/@{x}/")

# Save to CSV
df.to_csv('./tiktok_ugc_users.csv', index=False)

print(f"Scraped {len(usernames)} TikTok usernames successfully! Data saved to 'tiktok_ugc_users.csv'.")



