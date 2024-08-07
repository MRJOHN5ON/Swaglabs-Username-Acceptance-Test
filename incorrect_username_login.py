from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of invalid usernames
invalid_usernames = [
    "sstandard_user",       # Duplicate letter
    "lloocked_out_user",    # Duplicate letter
    "pprroblem_user",       # Duplicate letter
    "ppeerrformance_glitch_user",  # Duplicate letter
    "eerror_user",          # Duplicate letter
    "vvisual_user",         # Duplicate letter
    "пользователь",         # Russian Cyrillic
    "учетнаязапись",        # Russian Cyrillic
    "1234567890",           # All numbers
    "!@#$%^&*()",           # All symbols
    "standard user",        # Space instead of underscore
    "locked out user",      # Space instead of underscore
]

# List of valid usernames with different capitalizations and spaces
valid_usernames_with_variations = [
    "standard_user",        # Correct username
    "Standard_user",        # First letter capitalized
    "STANDARD_USER",        # All letters capitalized
    " standard_user",       # Space at the beginning
    "standard_user ",       # Space at the trailing end
]

# Password for all users
password = "secret_sauce"

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
        result = f"Login failed as expected for user: {username}\n"
    except:
        result = f"Login unexpectedly succeeded for user: {username}\n"
    
    file.write(result)
    print(result)

# Open the file in append mode
with open("negative_results.txt", "a") as file:
    # Test login for each invalid username
    for username in invalid_usernames:
        test_login(username, password, file)
    
    # Test login for each valid username with different capitalizations and spaces
    for username in valid_usernames_with_variations:
        test_login(username, password, file)

# Close the browser
driver.quit()
