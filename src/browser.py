from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://tutorialshut.com/demo-website-for-selenium-automation-practice/")

element = driver.find_element(By.ID,"fname")

element.send_keys("abi")

button = driver.find_element(By.ID,"idOfButton")
button.click()

time.sleep(5)
driver.quit()
