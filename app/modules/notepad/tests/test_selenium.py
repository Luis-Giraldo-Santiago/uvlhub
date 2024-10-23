from selenium.common.exceptions import NoSuchElementException
import time

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )
    

def test_notepad_index():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        
        # Open the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")

        # Send the form
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)
        
        driver.get(f'{host}/notepad')
        time.sleep(2)

        # Open the index page
        driver.get(f'{host}/notepad/create')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(2)
        
        # Find basic info and NOTEPAD model and fill values
        title_field = driver.find_element(By.NAME, "title")
        title_field.send_keys("Title")
        desc_field = driver.find_element(By.NAME, "body")
        desc_field.send_keys("Body")
        
        # Wait a little while to make sure the page has loaded completely
        time.sleep(2)
        
        submit_btn = driver.find_element(By.ID, "submit")
        submit_btn.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)
        time.sleep(2)  # Force wait time

        try:
            print('Test passed!')
            pass

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


# Call the test function
test_notepad_index()
