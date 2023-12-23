# %%
# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options to 
    #Disable the "enable-automation" flag.
    #Add the "no-sandbox" argument.
    #Add the "disable-infobars" argument.
    #Add the "disable-dev-shm-usage" argument.

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set the driver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# test open google website
driver.get('https://www.google.com')
time.sleep(5)

#navigate to login gmail
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")

# Identify the user name text box and enter the value
driver.find_element(By.ID, "identifierId").send_keys("parlayyarsu@gmail.com")
time.sleep(2)

# Clicks on the 'Next' button and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("California2023@#$")
time.sleep(2)

# Clicks on the 'Next' button again and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

#Uncomment below code to close the browser  
#driver.close()
