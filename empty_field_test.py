from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Valid username and password for reference
valid_username = "standard_user"
valid_password = "secret_sauce"

# List of invalid username-password combinations
invalid_combinations = [
    {"username": "", "password": valid_password},  # Blank username
    {"username": valid_username, "password": ""},  # Blank password
]

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_login(username, password, file):
    driver.get("https://www.saucedemo.com/")
    
    # Locate the username and password fields and the login button
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    # Clear the fields and input the credentials
    username_field.clear()
    password_field.clear()
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Click the login button
    login_button.click()
    
    time.sleep(2)  # Wait for the page to load
    
    # Check if login failed by verifying the presence of the error message
    try:
        error_message = driver.find_element(By.XPATH, "//*[@data-test='error']")
        result = f"Login failed as expected for username: '{username}', password: '{password}'\n"
    except Exception as e:
        result = f"Login unexpectedly succeeded for username: '{username}', password: '{password}'\nException: {e}\n"
    
    file.write(result)

# Open the file in append mode
with open("negative_results.txt", "a") as file:
    # Test login for each invalid combination
    for combo in invalid_combinations:
        test_login(combo["username"], combo["password"], file)

# Close the browser
driver.quit()
