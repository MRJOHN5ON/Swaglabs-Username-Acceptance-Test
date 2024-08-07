from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of valid usernames
usernames = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]

# Password for all users
password = "secret_sauce"

# Set up the Chrome WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Function to test login and write results to a file
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
    
    # Check if login was successful by verifying the presence of the inventory page
    try:
        inventory_page = driver.find_element(By.ID, "inventory_container")
        result = f"Login successful for user: {username}\n"
    except:
        result = f"Login failed for user: {username}\n"
    
    file.write(result)
    print(result)

# Open the file in write mode
with open("positive_results.txt", "w") as file:
    # Test login for each username
    for username in usernames:
        test_login(username, password, file)

# Close the browser
driver.quit()
