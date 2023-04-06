import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def driver():
    # Setup
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    # Teardown
    driver.quit()

def test_login_correct_user(driver):
    # Arrange
    login(driver, 'standard_user', 'secret_sauce')

    # Act
    url = driver.current_url
    title = driver.find_element(By.CLASS_NAME, 'title')
    title_txt = title.text

    # Assert
    assert url == 'https://www.saucedemo.com/inventory.html'
    assert title_txt == 'Products'


def test_login_incorrect_user(driver):
    # Arrange
    login(driver, 'locked_out_user', 'secret_sauce')

    # Act
    error_message = driver.find_element(By.CLASS_NAME, 'error-message-container.error').text

    # Assert
    assert error_message == 'Epic sadface: Sorry, this user has been locked out.'


def login(page,username,password):
    page.get("https://www.saucedemo.com")
    username_txt = page.find_element(By.ID,'user-name')
    password_txt = page.find_element(By.NAME,'password')
    login_btn =page.find_element(By.CLASS_NAME,'submit-button.btn_action')
    username_txt.send_keys(username)
    password_txt.send_keys(password)
    login_btn.click()