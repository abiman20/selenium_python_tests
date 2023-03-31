from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def login(page,username,password):
    page.get("https://www.saucedemo.com")
    username_txt = page.find_element(By.ID,'user-name')
    password_txt = page.find_element(By.NAME,'password')
    login_btn =page.find_element(By.CLASS_NAME,'submit-button.btn_action')
    username_txt.send_keys(username)
    password_txt.send_keys(password)
    login_btn.click()

# ------------login with correct user-------------
login(driver,'standard_user','secret_sauce')
assert driver.current_url == 'https://www.saucedemo.com/inventory.html',driver.current_url
assert driver.find_element(By.CLASS_NAME,'title').text == 'Products','title is not matching'
time.sleep(2)

# ------------login with incorrect user----------
login(driver,'locked_out_user','secret_sauce')
assert driver.find_element(By.CLASS_NAME,'error-message-container.error').text == 'Epic sadface: Sorry, this user has been locked out.','error text is not matching'
time.sleep(2)

driver.quit()
