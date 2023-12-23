# Selenium Gmail Login Automation project



<a href="https://opensource.org/licenses/MIT/" target="_blank"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-blue.svg" style="display: inherit;"/></a>  <a href="https://github.com/eaintkyawthmu" target="_blank"><img alt="AngelicML" src="https://img.shields.io/badge/Author-AngelicML-blue.svg" style="display: inherit;"/></a>

## About the Project

This project is a step-by-step tutorial on how to automate the login process for Gmail using Python, WebDriver, and Selenium. The goal of this project is to showcase the developer's skills in user authentication. The tutorial provides detailed instructions on setting up the Python environment, installing the necessary packages (selenium and webdriver_manager), and configuring the Chrome browser options for automation. It also includes code snippets that demonstrate how to navigate to the Gmail login page, enter the username, click the "Next" button, and perform other actions using Selenium's WebDriver API. The project emphasizes the importance of enabling less secure apps to access the Gmail account, while also highlighting the potential security risks associated with this setting. Overall, this tutorial serves as a practical guide for automating the Gmail login 


You can reach out to me via :

[![Gmail Badge](https://img.shields.io/badge/-Email--me-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:eaintkyawthmu@gmail.com)](mailto:eaintkyawthmu@gmail.com) [![Medium Badge](https://img.shields.io/badge/-Medium-black?style=flat-square&logo=Medium&logoColor=white&link=https://medium.com/@eaintkyawthmu/)](https://medium.com/@eaintkyawthmu/)      [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/eaintkyawthmu/)](https://www.linkedin.com/in/eaintkyawthmu/)   [![GitHub Badge](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github&logoColor=white&link=https://github.com/eaintkyawthmu/)](https://github.com/eaintkyawthmu) 
 



## Prerequisites

Before running the script, make sure you have the following installed:

- Python: Visit the official Python website at [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the appropriate version for your operating system.
- Pip: Pip is included by default with Python 3.4 and later versions. You can verify if pip is installed by running `pip --version` in your terminal.

## Installation

To install Python and pip, follow these steps:

1. **Download Python:**
    Visit the official Python website at [https://www.python.org/downloads/](https://www.python.org/downloads/). Download the version that is appropriate for your operating system (Windows, MacOS, Linux).

2. **Install Python:**
    Run the installer that you downloaded. On the first installer page, make sure you check the box labeled "Add Python to PATH" before clicking "Install Now".

3. **Verify Python Installation:**
    Open a new terminal window (Command Prompt for Windows, Terminal for MacOS and Linux). Type the following command and press Enter:

    ```bash
    python --version
    ```

    If Python is installed correctly, you should see a response with the Python version number.

4. **Install pip:**
    Pip is included by default with Python 3.4 and later versions. You can check if pip is installed by typing the following command in your terminal and pressing Enter:

    ```bash
    pip --version
    ```

    You can verify the installation by running `pip --version`

Once the Python environment is set up and the packages are installed, you can execute the code without any issues. If you don't have it yet, remember to read the above instruction before running the below code.

# This code snippet installs the required packages: selenium, webdriver_manager

%pip install selenium webdriver_manager

# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# When you try to login to your Google account, Google checks the browser and the app to ensure they meet certain security standards. If they don't, Google blocks the login attempt with the error "This browser or app may not be secure".

# To workaround is to enable less secure apps to access your account **Note! it can make your account more vulnerable to hacking. Test with extra account only**

# Setup Chrome options to
# Disable the "enable-automation" flag.
# Add the "no-sandbox" argument.
# Add the "disable-infobars" argument.
# Add the "disable-dev-shm-usage" argument.

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

# navigate to login gmail
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&hl=en&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession")

# Identify the user name text box and enter the value
driver.find_element(By.ID, "identifierId").send_keys("yourgmailacc@gmail.com")
time.sleep(2)

# Clicks on the 'Next' button and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

driver.find_element(By.XPATH, '//input[@name="Passwd"]').send_keys("yourpassword")
time.sleep(2)

# Clicks on the 'Next' button again and waits for 2 seconds.
driver.find_element(By.XPATH, "//span[text()='Next']").click()
time.sleep(2)

# close the browser
driver.close()

