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
  
### Negative Results Summary
- Total Tests Expected to Fail: `50`

- Tests that Did Not Run as Expected: `1`
  #### Total Bugs:
- 1 Bug: For the username standard_user (with a leading space) and the password secret_sauce. The discrepancy here is that this test case succeeded, whereas it was expected to fail.

### Positive Results Summary
- Total Tests Expected to Succeed: `5`
- Tests that Did Not Run as Expected: `1`
  #### Total Bugs:
- 1 Bug (for locked_out_user) The discrepancy with locked_out_user failing when it should have succeeded is noted as a bug.


## Tools Used
- Python
- Selenium
- Chrome WebDriver
- WebDriver Manager
