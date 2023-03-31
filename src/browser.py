from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.saucedemo.com")

username_txt = driver.find_element(By.ID,'user-name')

password_txt = driver.find_element(By.NAME,'password')

login_btn =driver.find_element(By.CLASS_NAME,'submit-button.btn_action')

username_txt.send_keys('standard_user')

password_txt.send_keys('secret_sauce')

login_btn.click()

assert driver.current_url == 'https://www.saucedemo.com/inventory.html',driver.current_url

assert driver.find_element(By.CLASS_NAME,'title').text == 'Products','title is not matching'

time.sleep(2)

driver.get("https://www.saucedemo.com")

username_txt = driver.find_element(By.ID,'user-name')

password_txt = driver.find_element(By.NAME,'password')

login_btn =driver.find_element(By.CLASS_NAME,'submit-button.btn_action')

username_txt.send_keys('locked_out_user')

password_txt.send_keys('secret_sauce')

login_btn.click()



assert driver.find_element(By.CLASS_NAME,'error-message-container.error').text == 'Epic sadface: Sorry, this user has been locked out.','error text is not matching'

time.sleep(2)

driver.quit()
