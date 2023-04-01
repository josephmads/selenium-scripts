from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# set the path to the chromedriver executable
chromedriver_path = "/usr/bin/chromedriver"

# create a new ChromeDriver service object
service = Service(executable_path=chromedriver_path)

# create a new Chrome driver instance
driver = webdriver.Chrome(service=service)

# navigate to Google homepage
driver.get("https://www.google.com/")


# locate the search box element and enter the search term
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("Python Selenium tutorial")

# press the Enter key to submit the search
search_box.send_keys(Keys.RETURN)

# wait for the search results to load
driver.implicitly_wait(10)

# print the search results
search_results = driver.find_elements(By.CSS_SELECTOR, "div.g")
for result in search_results:
    print(result.text)

# close the browser window
driver.quit()
