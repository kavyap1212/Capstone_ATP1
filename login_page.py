from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from conftest import setup
driver = setup
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, 'username')
        self.password_field = (By.NAME, 'password')
        self.login_button = (By.XPATH, '//button[@type="submit"]')
        self.error_message = (By.XPATH, '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]')
        self.forgot_password_link = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
        self.reset_password_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')  
        self.timeout = 10

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")
        except NoSuchElementException:
            raise Exception(f"Element not found: {locator}")
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
        time.sleep(2)
    
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        ).send_keys(password)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
        time.sleep(2)

    def get_error_message(self):
        try:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.error_message)
            ).text
        except:
            return None
    def click_forgot_password(self):
        self.click_element(self.forgot_password_link)

    def reset_password(self, username):
        self.enter_text(self.username_field, username)
        self.click_element(self.reset_password_button)
    
    
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
    def close(self):
        if self.driver:
            self.driver.quit()