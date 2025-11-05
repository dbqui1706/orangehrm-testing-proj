"""Base page class containing common methods for all page objects."""
import logging
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import DEFAULT_WAIT_TIMEOUT

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BasePage:
    """Base page class with common methods for interacting with web elements."""

    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_WAIT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)

    def _find_element(self, by: str, value: str) -> WebElement:
        """Find an element safely with explicit wait.

        Args:
            by: The locator strategy (e.g., By.ID, By.XPATH)
            value: The locator value

        Returns:
            WebElement: The found element

        Raises:
            TimeoutException: If element is not found within timeout
        """
        try:
            logger.info(f"Finding element: {by}={value}")
            return self.wait.until(EC.visibility_of_element_located((by, value)))
        except TimeoutException:
            logger.error(f"Element not found: {by}={value}")
            raise

    def _find_elements(self, by: str, value: str) -> list[WebElement]:
        """Find multiple elements safely with explicit wait.

        Args:
            by: The locator strategy
            value: The locator value

        Returns:
            list[WebElement]: List of found elements
        """
        try:
            logger.info(f"Finding elements: {by}={value}")
            return self.wait.until(EC.presence_of_all_elements_located((by, value)))
        except TimeoutException:
            logger.warning(f"Elements not found: {by}={value}")
            return []

    def _click(self, by: str, value: str) -> None:
        """Click on an element.

        Args:
            by: The locator strategy
            value: The locator value
        """
        element = self._find_element(by, value)
        logger.info(f"Clicking element: {by}={value}")
        self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def _send_keys(self, by: str, value: str, text: str) -> None:
        """Send keys to an element after clearing it.

        Args:
            by: The locator strategy
            value: The locator value
            text: The text to send
        """
        element = self._find_element(by, value)
        logger.info(f"Sending keys to element: {by}={value}")
        element.clear()
        element.send_keys(text)

    def _get_text(self, by: str, value: str) -> str:
        """Get the text of an element.

        Args:
            by: The locator strategy
            value: The locator value

        Returns:
            str: The element's text content
        """
        element = self._find_element(by, value)
        return element.text

    def _is_element_visible(self, by: str, value: str, timeout: int = 5) -> bool:
        """Check if an element is visible within a specific timeout.

        Args:
            by: The locator strategy
            value: The locator value
            timeout: Custom timeout in seconds (default: 5)

        Returns:
            bool: True if element is visible, False otherwise
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except (TimeoutException, NoSuchElementException):
            logger.debug(f"Element not visible: {by}={value}")
            return False

    def _wait_for_element_to_disappear(self, by: str, value: str, timeout: int = 10) -> bool:
        """Wait for an element to disappear from the page.

        Args:
            by: The locator strategy
            value: The locator value
            timeout: Timeout in seconds

        Returns:
            bool: True if element disappeared, False otherwise
        """
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            logger.warning(f"Element did not disappear: {by}={value}")
            return False