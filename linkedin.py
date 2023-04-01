from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from config import CFG


chromedriver_path = "/usr/bin/chromedriver"
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Login to LinkedIn
username = CFG['LI_USERNAME']
password = CFG['LI_PASSWORD']

driver.get('https://linkedin.com')

username_field = driver.find_element(By.NAME, 'session_key')
username_field.send_keys(username)

password_field = driver.find_element(By.NAME, 'session_password')
password_field.send_keys(password)

username_field.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

# Post Content
post_text = """
Write a post here.
"""

# Open 'create post' overlay
driver.get('https://www.linkedin.com/in/joseph-madsen/overlay/create-post/')

# Locate textbox and botton by XPATH 
post = driver.find_element(By.XPATH, "//div[@role='textbox']")
post.send_keys(post_text)

post_button = driver.find_element(By.XPATH, 
    "//button[@class='share-actions__primary-action artdeco-button " 
    "artdeco-button--2 artdeco-button--primary ember-view']")

post_button.click()

driver.implicitly_wait(10)

driver.quit()
