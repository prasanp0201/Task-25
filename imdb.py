from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException   # Import TimeoutException
import time  # Import the time module

# Set up the WebDriver
driver = webdriver.Chrome()

# Go to the IMDb search name page
driver.get("https://www.imdb.com/search/name/")

# Wait for the cookie consent banner and accept cookies if present
wait = WebDriverWait(driver, 40)
try:
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Accept']")))
    accept_cookies_button.click()
except Exception as e:
    print("Cookies consent button not found or already accepted")

# Fill in the name input box
name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='nameTextAccordion']/div[1]/label/span[1]/div")))
name_input.click()
name_textbox = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Name']")))
name_textbox.send_keys("Tom Hanks")

# Select an award from the drop-down menu
awards_select = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='awardsAccordion']/div[1]/label/span[1]/div")))
awards_select.click()
awards_select = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='accordion-item-awardsAccordion']/div/section/button[2]")))
awards_select.click()

# Select an page topics from the drop-down menu
# page_topics_select = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='pageTopicsAccordion']/div[1]/label/span[1]/div")))
# page_topics_select.click()
# page_topics_select = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='accordion-item-pageTopicsAccordion']/div/div/section/button[1]/span")))
# page_topics_select.click()

# # # Select the gender from the drop-down menu
# gender_identity = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='genderIdentityAccordion']/div[1]/label/span[1]/div")))
# gender_identity.click()
# gender_identity = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='accordion-item-genderIdentityAccordion']/div/section/button[1]/span")))
# gender_identity.click()

# Perform the search by clicking the search button
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[1]/button")))
search_button.click()

# Wait for the search results to load
time.sleep(5)  # Additional delay to ensure the page has loaded fully
print("Waiting for search results...")

# Additional wait for the container of results
try:
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".lister-list")))
    search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h3[@class='lister-item-header']/a")))
    for result in search_results:
        print(result.text)
except TimeoutException:
    print("Search results did not load within the given time.")

# Close the browser
driver.quit()