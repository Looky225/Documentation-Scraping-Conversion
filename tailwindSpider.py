import pdfkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

# Function to sanitize the text for filename
def sanitize_filename(text):
    # Remove special characters
    sanitized_text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with underscores
    sanitized_text = sanitized_text.replace(' ', '_')
    return sanitized_text

# Configure the Selenium WebDriver
driver = webdriver.Chrome()  # Replace with the appropriate WebDriver for your browser
driver.get("https://tailwindcss.com/docs/top-right-bottom-left")

# Add a delay to observe the scrolling
time.sleep(2)

# Initialize an empty list to store the text of all URLs
all_elements_text = []

# Iterate until there are no more "Next" buttons
while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Add a delay to observe the scrolling
    time.sleep(2)

    # Find the element with the specified class
    element = driver.find_element(By.CLASS_NAME, "max-w-3xl.mx-auto.pt-10")
    all_elements_text.append(element.text)

    # Get the text of the h1 element
    h1_text = driver.find_element(By.CSS_SELECTOR, "h1.inline-block.text-2xl").text

    # Sanitize the filename
    file_name = sanitize_filename(h1_text) + ".txt"
    with open(file_name, "w") as file:
        file.write(element.text)
        print(f"Saved text to {file_name}")

    # Click on the next button if it exists
    next_button = driver.find_elements(By.CSS_SELECTOR, "a.group.ml-auto.flex.items-center")
    if len(next_button) == 0:
        break
    else:
        next_button[0].click()

    # Add a delay to observe the scrolling
    time.sleep(2)

    


# Quit the WebDriver
driver.quit()