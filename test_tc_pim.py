import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from login_page import LoginPage
from pim_page import PIMPage
import time
from conftest import setup


class Test_Pim:

    def test_TC_PIM_01(self, setup): #adding new employee
        driver = setup
        login_page = LoginPage(driver)

        # Explicit credentials
        username = "Admin"
        password = "admin123"

        # Login
        print("Logging in with username and password")
        login_page.login(username, password)

        # Wait for the page to load
        time.sleep(3)

        # Click on PIM from menu options and validate title
        print("Clicking on 'PIM' from menu options")
        pim_page = PIMPage(driver)
        try:
            # Assuming the 'PIM' menu item is not a link but a span element
            admin_menu = pim_page.find_element((By.XPATH, "//span[text()='PIM']"))
            admin_menu.click()
            time.sleep(2)  # Wait for the Admin page to load
        
            pim_page.add_new_employee('John', 'Doe')
            print("New employee added successfully.")
        except Exception as e:
            print(f"An error occurred in TC_PIM_01: {e}")
        finally:
            login_page.close()

    def test_TC_PIM_02(self, setup): #Editing existing Employee
        driver = setup
        login_page = LoginPage(driver)

        # Explicit credentials
        username = "Admin"
        password = "admin123"

        # Login
        print("Logging in with username and password")
        login_page.login(username, password)

        # Wait for the page to load
        time.sleep(3)

        # Click on PIM from menu options and validate title
        print("Clicking on 'PIM' from menu options")
        pim_page = PIMPage(driver)
        try:
            # Assuming the 'Admin' menu item is not a link but a span element
            admin_menu = pim_page.find_element((By.XPATH, "//span[text()='PIM']"))
            admin_menu.click()
            time.sleep(2)  # Wait for the Admin page to load
        
            pim_page.edit_employee('John Doe', 'Jane', 'Doe')
            print("employee Edited successfully.")
        except Exception as e:
            print(f"An error occurred in TC_PIM_02: {e}")
        finally:
            login_page.close()

    def test_TC_PIM_03(self, setup): #Deleting existing Employee
        driver = setup
        login_page = LoginPage(driver)

        # Explicit credentials
        username = "Admin"
        password = "admin123"

        # Login
        print("Logging in with username and password")
        login_page.login(username, password)

        # Wait for the page to load
        time.sleep(3)

        # Click on PIM from menu options and validate title
        print("Clicking on 'PIM' from menu options")
        pim_page = PIMPage(driver)
        try:
            # Assuming the 'Admin' menu item is not a link but a span element
            admin_menu = pim_page.find_element((By.XPATH, "//span[text()='PIM']"))
            admin_menu.click()
            time.sleep(2)  # Wait for the Admin page to load
        
            pim_page.delete_employee('Jahn Doe')
            print("employee Deleted successfully.")
        except Exception as e:
            print(f"An error occurred in TC_PIM_03: {e}")
        finally:
            login_page.close()

