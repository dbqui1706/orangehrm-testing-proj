"""PIM page object containing employee search and management actions."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base import BasePage
from config import SEARCH_RESULT_WAIT
import logging

logger = logging.getLogger(__name__)


class PIMPage(BasePage):
    """Page object for the PIM (Personal Information Management) page."""
    # Locators
    EMPLOYEE_NAME_INPUT = (By.XPATH, '//label[text()="Employee Name"]/../following-sibling::div//input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    NO_RECORDS_FOUND_MESSAGE = (By.XPATH, '//*[text()="No Records Found"]')
    FIRST_ROW_CELL = (By.CSS_SELECTOR, '.oxd-table-card .oxd-table-row .oxd-table-cell')
    ROWS_ITEMS = (By.CLASS_NAME, 'oxd-table-card')
    
    AUTOCOMPLETE_OPTIONS = (By.CLASS_NAME, "oxd-autocomplete-option")
    LOADING_SPINNER = (By.CLASS_NAME, "oxd-loading-spinner")

    def search_for_employee_by_name(self, employee_name: str) -> None:
        """Search for an employee by their name, handling autocomplete.

        Args:
            employee_name: The name of the employee to search for
        """
        logger.info(f"Searching for employee: {employee_name}")
        self._send_keys(*self.EMPLOYEE_NAME_INPUT, employee_name)
       
        # Wait for and select autocomplete option if available
        try:
            options = self._find_elements(*self.AUTOCOMPLETE_OPTIONS)
            if options:
                for option in options:
                    if employee_name.lower() in option.text.lower():
                        logger.info(f"Selecting autocomplete option: {option.text}")
                        option.click()
                        break
        except TimeoutException:
            logger.info("No autocomplete options found, proceeding with search")

        self._click(*self.SEARCH_BUTTON)

        # Wait for loading spinner to disappear (if present)
        self._wait_for_loading_to_complete()
        

    def _wait_for_loading_to_complete(self, timeout: int = SEARCH_RESULT_WAIT) -> None:
        """Wait for the loading spinner to disappear.

        Args:
            timeout: Maximum time to wait in seconds
        """
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(self.LOADING_SPINNER)
            )
        except TimeoutException:
            logger.debug("No loading spinner detected or already completed")

    def is_no_records_found_message_visible(self) -> bool:
        """Check if the 'No Records Found' message is displayed.

        Returns:
            bool: True if message is visible, False otherwise
        """
        toast_visible = self._is_element_visible(*self.NO_RECORDS_FOUND_MESSAGE) 
        items = self._find_elements(*self.ROWS_ITEMS)
        toast = self._get_text(*self.NO_RECORDS_FOUND_MESSAGE) if toast_visible else ""
        
        logger.info(f"'No Records Found' message visibility: {toast_visible}, text: '{toast}'")
        logger.info(f"Number of search result items found: {len(items)}")
        
        return toast_visible or len(items) == 0

    def get_first_row_text(self) -> str:
        """Get the text content of the first result row.

        Returns:
            str: Text from the first row cell
        """
        return self._get_text(*self.FIRST_ROW_CELL)

    def are_search_results_visible(self) -> bool:
        """Check if search results are visible.

        Returns:
            bool: True if results are visible, False otherwise
        """
        return self._is_element_visible(*self.FIRST_ROW_CELL)