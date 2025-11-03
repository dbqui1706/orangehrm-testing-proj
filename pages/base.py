import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Base:
    """Base class for page objects."""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open_url(self, url):
        """Open a URL in the browser."""
        self.driver.get(url)
        time.sleep(1)
        
    def find_element(self, locator):
        """Find a single element on the page."""
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )
        
    def find_elements(self, locator):
        """Find multiple elements on the page."""
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )
        
    def click(self, locator):
        """Click on an element."""
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        ) # Wait until the element is clickable
        element.click()
    
    def click_js(self, locator):
        """
        Click on an element using JavaScript. 
        Useful for elements that are not easily clickable.
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        
    def input_text(self, locator, text):
        """Input text into a text field."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        """Get text from an element."""
        element = self.find_element(locator)
        return element.text 
    
    def is_displayed(self, locator):
        """Check if an element is displayed."""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
        
    def scroll_to_view(self, locator):
        """Scroll the page to bring the element into view."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)        
        time.sleep(0.5)
        
    def take_screenshot(self, file_name):
        """Take a screenshot of the current page."""
        self.driver.save_screenshot(
            f"screenshots/{file_name}.png"
        )
        
    def get_page_title(self):
        """Get the title of the current page."""
        return self.driver.title
    
    def select_dropdown_by_text(self, locator, text):
        """Select an option from a dropdown by visible text."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
        
    def select_dropdown_by_value(self, locator, value):
        """Select an option from a dropdown by value."""
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
    