from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of valid usernames
valid_usernames = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]

# List of incorrect passwords
incorrect_passwords = [
    "password",
    "secret sauce",          # Space instead of an underscore
    "SECRET_SAUCE",          # All caps
    "Secret_sauce",          # Capital S at the start
    " secret_sauce",         # Space at the beginning
    "secret_sauce "         # Trailing space
]

# Valid password for reference
valid_password = "secret_sauce"

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
    # Test login for each combination of valid username and incorrect password
    for username in valid_usernames:
        for password in incorrect_passwords:
            test_login(username, password, file)

# Close the browser
driver.quit()
