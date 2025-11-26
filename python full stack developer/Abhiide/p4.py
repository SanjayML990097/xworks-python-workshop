from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome driver (you need ChromeDriver installed)
driver = webdriver.Chrome()

# Go to Google's Find My Device
driver.get("https://www.google.com/android/find")

# Wait for manual login
print("Please log in to your Google account in the opened browser...")
time.sleep(60)  # Wait 1 minute for manual login

# After login, the device map will load
print("If login was successful, you should see your device on the map.")
