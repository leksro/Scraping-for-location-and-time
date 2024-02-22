from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re

# Load CSV file
csv_file_path = ' ' # The root directory where CSV file of AMCA dataset is saved.
#Create a dataframe
df = pd.read_csv(csv_file_path, encoding='utf-8')
# Check for the column name that contains all artists' names and assign
artist_names_column = 'composer'

#Selenium Testing with a simple search in google search bar
chrome_driver_path = '' # change this to the root directory where the driver is saved.
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver.get('https://www.google.com')
search_box = driver.find_element('name', 'q')
search_box.send_keys("Web scraping with Selenium")
search_box.send_keys(Keys.RETURN)
driver.implicitly_wait(5)
print(driver.title)


results = [] # This is where all the info will go. Initially it is a blank set.

# Automation to search all artists
processed_artists = set()

for artist_name in df[artist_names_column]:
    # Check if the artist has already been processed
    if artist_name in processed_artists: 
        continue
    try:
        # Navigate to wikipedia
        driver.get("https://www.wikipedia.org")
        # Find the search bar by name attribute and enter the artist's name
        search_box = driver.find_element('name', 'search')
        search_box.send_keys(artist_name)
        search_box.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        print(driver.title)

        #Born Element
        born_element = driver.find_element(By.XPATH, '//*[contains(text(), "born")]')
       
        print(f'born_element:{born_element}')
        born_info = born_element.text.strip()
        print(f'born_info: {born_info}')
       
        # Extract information following "Born"
        born_info_search = re.search(r'born\s*(.*)', born_info).group(1).strip()
       
        print(f'Artist: {artist_name}, Born Info search: {born_info_search}, Born info: {born_info}')
        results.append({'Artist': artist_name, 'Born Information': born_info_search})

        # Skip already processed artists as there are lot of repetitions in the dataset
        processed_artists.add(artist_name)

        results_df = pd.DataFrame(results)
        
        # Save the DataFrame to a CSV file
        results_df.to_csv('D:/artist_born_info.csv', index=False)

    except Exception as e:
        print(f"no info for the word 'born' found for {artist_name}")
        processed_artists.add(artist_name)

# Close the browser
driver.quit()