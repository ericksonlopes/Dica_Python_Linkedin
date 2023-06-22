# pip install requests selenium
import os
import platform

import requests
from selenium import webdriver


def download_webdriver():
    # gets the current operating system
    system = platform.system()

    # Directory where the webdriver will be stored
    webdriver_dir = os.path.join(os.getcwd(), 'webdriver')

    # Checks the operating system and sets the appropriate driver URL and name
    if system == 'Windows':
        driver_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        driver_name = 'chromedriver_win32.zip'
    elif system == 'Linux':
        driver_url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
        driver_name = 'chromedriver_linux64.zip'
    else:
        print(f'The operating system is not supported {system}.')
        return

    # Create the webdriver directory if it doesn't exist
    os.makedirs(webdriver_dir, exist_ok=True)

    # Creates a .gitignore file inside the webdriver directory
    # so that it will be ignored by version control (Git)
    print("*", file=open(os.path.join(webdriver_dir, ".gitignore"), 'w', encoding='utf-8'))

    # Full path to webdriver
    webdriver_path = os.path.join(webdriver_dir, driver_name)

    # Checks if the webdriver has already been downloaded
    if not os.path.exists(webdriver_path):
        try:

            # Get the latest version of the webdriver
            response = requests.get(driver_url)
            version = response.text.strip()
            # Constructs the webdriver download URL
            driver_url = f'https://chromedriver.storage.googleapis.com/{version}/{driver_name}'
            response = requests.get(driver_url)
            # Save the webdriver file to disk
            with open(webdriver_path, 'wb') as file:
                file.write(response.content)
            print(f'Webdriver downloaded successfully for {system}.')
        except Exception as e:
            print(f'Failed to download webdriver: {str(e)}')
    else:
        print(f'The webdriver for {system} already exists.')

    return webdriver_path


path_webdriver = download_webdriver()

if not path_webdriver:
    exit()

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
