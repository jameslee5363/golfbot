from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import date

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)
 
# Set up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the website
driver.get("https://bergencountygolf.cps.golf/onlineresweb/auth/verify-email")

driver.maximize_window()

# Explicitly wait for the username field to be present
try:
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mat-input-0"))
    )
    # Input the username
    username_field.send_keys("9043183")

    # Locate the "Next" button and click it
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(., 'NEXT')]"))
    )
    next_button.click()
    
    # Wait for the password field to be present and input the password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mat-input-1"))  # Adjust the ID if needed
    )
    password_field.send_keys("")

    # Locate the "SIGN IN" button and click it
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(., 'SIGN IN')]"))
    )
    sign_in_button.click()
    
    # If a popup exists 
    try:
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.mat-flat-button[mat-dialog-close]')))

        # Click the button
        button.click()
    except:
        print("No popup")

    '''
    # Selecting the Courses
    wait = WebDriverWait(driver, 10)

    # Locate the element by its ID
    courses = driver.find_element(By.ID, 'mat-select-value-3')

    # Initialize ActionChains
    actions = ActionChains(driver)

    # Move to the element, click it, and keep the mouse hovering over it
    actions.move_to_element(courses).click().perform()

    # Add a short delay to ensure the dropdown is ready
    time.sleep(1)  # Adjust the sleep time as needed

    # Keep the mouse hovering over the element
    actions.move_to_element(courses).perform()
    
    # Deselect all courses
    wait = WebDriverWait(driver, 10)

    # Wait until the element is visible and locate it by its text content
    select_all_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Select All']")))

    # Click the element
    select_all_button.click()
    '''

    # Get today's date
    today = date.today()

    # Get the numerical day of the month
    today_day = today.day

    print(today_day)


except Exception as e:
    print(f"An error occurred: {e}")

# Remember to close the driver when done
# driver.quit()
