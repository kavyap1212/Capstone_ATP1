from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # Default timeout for waits

    def find_element(self, locator, timeout=None):
        timeout = timeout or self.timeout
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")
        except NoSuchElementException:
            raise Exception(f"Element not found: {locator}")

    def click_element(self, locator, timeout=None):
        element = self.find_element(locator, timeout)
        element.click()
    
    def enter_text(self, locator, text, timeout=None):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)