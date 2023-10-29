
#### Test Case : 1

# 1. open Web Browser (chrome).
# 2. OPen URL : 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
# 3. Enter Username (admin)
# 4. Enter password (admin123)
# 5. click on login.
# 6. Capture title of the home page.
# 7. Verify the title pf the page: OrangeHRM (Expected)
# 8. close Browser.

#------- code starts ------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    # loading the url
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    driver.implicitly_wait(10)

    # input the credentials
    user_name = driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys('Admin')
    password = driver.find_element(By.XPATH, '//input[@placeholder="Password"]').send_keys('admin123')
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # getting the title of page
    expected_title = 'OrangeHRM'
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
