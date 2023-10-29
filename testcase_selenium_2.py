#### Test Case : 2

# 1. open Web Browser (chrome).
# 2. OPen URL : 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'
# 3. Clear the username & password present
# 3. Enter Username (admin@yourstore.com)
# 4. Enter password (admin)
# 5. click on login.
# 6. Capture title of the home page.
# 7. Verify the title pf the page: Dashboard / nopCommerce administration (Expected)
# 8. close Browser.

# import required libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

#------- code starts ------------------

try:
    # loading the url
    driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'Email').clear()
    user_name = driver.find_element(By.ID, 'Email').send_keys('admin@yourstore.com')

    driver.find_element(By.ID, 'Password').clear()
    password = driver.find_element(By.ID, 'Password').send_keys('admin')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # getting the title of page
    expected_title = 'Dashboard / nopCommerce administration'
    actual_title = driver.title

    # checking the title
    if actual_title == expected_title:
        print('Test Successful')
    else:
        print(f'Test failed as the title found is {actual_title} ')
    driver.quit()

except Exception as e:
    print('Exception occurred during Testing')
    driver.quit()