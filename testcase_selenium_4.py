import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()
    driver.get('https://testautomationpractice.blogspot.com/')
    driver.maximize_window()
    driver.implicitly_wait(5)

    #performing click action on alert

    driver.find_element(By.XPATH, '//button[text()="Alert"]').click()       #clicking on alert button
    get_alert_window = driver.switch_to.alert
    get_alert_window.accept()
    time.sleep(5)

    # performing click action on prompt

    driver.find_element(By.XPATH, '//button[text()="Prompt"]').click()    #clicking on Prompt button
    print('clicked')
    get_alert_window = driver.switch_to.alert
    get_alert_window.send_keys(Keys.BACKSPACE)
    get_alert_window.send_keys('welcome')
    get_alert_window.accept()
    time.sleep(5)

    #interacting with frames/iframes

    driver.execute_script("window.scrollTo(0, 2000)")
    driver.switch_to.frame('frame-one796456169')
    name = driver.find_element(By.CSS_SELECTOR, 'input#RESULT_TextField-0')
    name.send_keys('Anu')
    driver.find_element(By.XPATH, '//label[normalize-space()="Female"]').click()
    dob = driver.find_element(By.CSS_SELECTOR, 'input#RESULT_TextField-2')
    dob.send_keys('01/01/2000')
    element = driver.find_element(By.CSS_SELECTOR, 'select#RESULT_RadioButton-3')
    drop_down = Select(element)
    drop_down.select_by_visible_text("Automation Engineer")
    time.sleep(5)

    #back to page

    driver.switch_to.default_content()
    driver.execute_script("window.scrollTo(0, 0)")
    time.sleep(5)
    driver.find_element(By.XPATH, '//input[@id="name"]').send_keys('Anu')
    driver.find_element(By.XPATH, '//input[@id="email"]').send_keys('Anu@gmail.com')
    driver.find_element(By.XPATH, '//input[@id="phone"]').send_keys('123456789')
    driver.find_element(By.XPATH, '//textarea[@id="textarea"]').send_keys('Delhi')
    driver.find_element(By.XPATH, '//label[@for="female"]').click()
    driver.find_element(By.CSS_SELECTOR, 'input#sunday').click()
    country_ele = driver.find_element(By.XPATH, '//select[@id="country"]')
    country_dropdown = Select(country_ele)
    country_dropdown.select_by_visible_text("India")
    time.sleep(5)

    #search on wikipedia -- switching windows

    wikipedia_search = driver.find_element(By.CSS_SELECTOR, '#Wikipedia1_wikipedia-search-input')
    wikipedia_search.send_keys('selenium')
    driver.find_element(By.XPATH, '//input[@class="wikipedia-search-button"]').click()
    wiki_text = driver.find_elements(By.XPATH, '//div[@id="wikipedia-search-result-link"]')
    current_window = driver.current_window_handle
    link_text = [i.text for i in wiki_text]
    print(link_text)
    for i in link_text:
        driver.find_element(By.LINK_TEXT, i).click()
        print('Id of the current window is : ', driver.current_window_handle)
        print('Title of the current window is : ', driver.title)
        time.sleep(3)
        driver.switch_to.window(current_window)

    driver.quit()


except:
    print("An error occurred")