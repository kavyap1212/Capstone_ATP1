import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def setup():
    # Initialize Chrome WebDriver with ChromeDriverManager
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Set an implicit wait if needed
    driver.implicitly_wait(10) 
    
    # Navigate to the URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    yield driver  # Provide the driver to the test
    
    driver.quit()  # Close the browser after the test is done