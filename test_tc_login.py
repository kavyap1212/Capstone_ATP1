import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from login_page import LoginPage
from selenium.webdriver.common.by import By
import time
from conftest import setup


class Test_Login:
         
    def test_TC_Login_01(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        try:
            login_page.login('Admin', 'admin123')
            time.sleep(2)
            print("Logged in successfully (if no error message is displayed)")
        finally:
            login_page.close()

    def test_TC_Login_02(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        try:
            login_page.login('Admin', 'InvalidPassword')
            time.sleep(2)
            error_message = login_page.get_error_message()
            if error_message:
                print(f"Error message displayed: {error_message}")
            else:
                print("No error message displayed.")
        except Exception as e:
            print(f"An error occurred in TC_Login_02: {e}")
        finally:
            login_page.close()