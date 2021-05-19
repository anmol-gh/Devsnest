from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os


def click_on_accept():
    driver.get('https://www.linkedin.com/mynetwork/')
    sleep(1)
    accept_btns=driver.find_elements_by_class_name('invitation-card__action-btn')
    print(len(accept_btns))
    for btn in accept_btns:
        print(btn)
        print('clicking')
        btn.click()
        print('clicked')
        sleep(1)


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get('https://www.linkedin.com')
sleep(3)
if driver.current_url=='https://www.linkedin.com':
    log_in=driver.find_element_by_id('session_key')
    log_in.send_keys("")      #Confidential
    password=driver.find_element_by_id('session_password')
    password.send_keys('')    #Confidential
    #File handling can also be used to secure Confidentials.
    sign_in_btn=driver.find_element_by_class_name('sign-in-form__submit-button')
    sign_in_btn.click()
    click_on_accept()
elif driver.current_url=='https://www.linkedin.com/feed/':
    click_on_accept()

driver.close()
    
