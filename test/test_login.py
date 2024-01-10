import pytest
#step 1:import selenium
#step 2:import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSaucelogin():

    #step 3:Open browser
    def setup_method(self, method):
        self.vars = {}
        self.browser = webdriver.Chrome()
        #step 4: Open website
        url = "https://www.saucedemo.com/"
        self.browser.get(url)
        assert self.browser.current_url == url
    
    def teardown_method(self, method):
        #step X: Close browser
        self.browser.quit()

    def test_valid_login_logout(self):
        self.browser.find_element(By.ID, "user-name").send_keys("standard_user")
        self.browser.find_element(By.ID, "password").send_keys("secret_sauce")
        self.browser.find_element(By.ID, "login-button").click()
        product_page = "https://www.saucedemo.com/inventory.html"
        assert self.browser.current_url == product_page, self.browser.current_url +' is not equal to ' + product_page
        title = self.browser.find_element(By.XPATH,'//div[contains(text(),"Swag Labs")]').text
        assert title == "Swag Labs", title
        self.browser.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
        WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@id='logout_sidebar_link']")))
        self.browser.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()


    def test_invalid_login_logout(self):
        self.browser.find_element(By.ID, "user-name").send_keys("locked_out_user")
        self.browser.find_element(By.ID, "password").send_keys("secret_sauce")
        self.browser.find_element(By.ID, "login-button").click()
        error_message = self.browser.find_element(By.XPATH,"//h3[@data-test='error']").text
        assert error_message == "Epic sadface: Sorry, this user has been locked out.",error_message
        
        
    