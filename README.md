# Swaglabs Username & Password Acceptance Test

**Test URL**: [Sauce Demo Login](https://www.saucedemo.com/)

## Test Files

### Python Scripts
- `positive_login_tests.py`: Tests valid usernames with the correct password.
- `incorrect_username_login.py`: Tests invalid usernames, including those with duplicate letters, Cyrillic characters, numbers, symbols, or spaces.
- `incorrect_password_login.py`: Tests valid usernames with incorrect passwords, including variations like extra spaces or capitalization.
- `empty_field_test.py`: Tests scenarios with blank username or password fields.

### Results Files
- `positive_results.txt`: Logs results from positive username tests.
- `negative_results.txt`: Logs results from negative username, blank fields, and incorrect password tests.

## Tools Used
- Python
- Selenium
- Chrome WebDriver
- WebDriver Manager
