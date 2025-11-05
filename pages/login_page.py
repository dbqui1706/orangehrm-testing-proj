"""Login page object containing login-related elements and actions."""
from selenium.webdriver.common.by import By
from pages.base import BasePage
from config import BASE_URL


class LoginPage(BasePage):
    """Page object for the login page."""

    # Locators
    USERNAME_INPUT = (By.NAME, 'username')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    INVALID_CREDENTIALS_MESSAGE = (By.CSS_SELECTOR, 'p.oxd-alert-content-text')

    def __init__(self, driver):
        """Initialize the login page and navigate to it.

        Args:
            driver: WebDriver instance
        """
        super().__init__(driver)
        self.driver.get(BASE_URL)

    def login(self, username: str, password: str) -> None:
        """Perform the login action.

        Args:
            username: Username for login
            password: Password for login
        """
        self._send_keys(*self.USERNAME_INPUT, username)
        self._send_keys(*self.PASSWORD_INPUT, password)
        self._click(*self.LOGIN_BUTTON)

    def get_invalid_credentials_message(self) -> str:
        """Get the error message for invalid credentials.

        Returns:
            str: The error message text
        """
        return self._get_text(*self.INVALID_CREDENTIALS_MESSAGE)

    def is_on_login_page(self) -> bool:
        """Check if currently on the login page.

        Returns:
            bool: True if on login page, False otherwise
        """
        return "login" in self.driver.current_url.lower()
