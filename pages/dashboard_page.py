"""Dashboard page object containing dashboard-related elements and actions."""
from selenium.webdriver.common.by import By
from pages.base import BasePage


class DashboardPage(BasePage):
    """Page object for the dashboard page."""

    # Locators
    USER_DROPDOWN = (By.CLASS_NAME, 'oxd-userdropdown-tab')
    LOGOUT_LINK = (By.XPATH, '//a[text()="Logout"]')
    PIM_MODULE = (By.XPATH, '//a[.//span[text()="PIM"]]')
    USER_NAME_IN_DROPDOWN = (By.CLASS_NAME, 'oxd-userdropdown-name')

    def navigate_to_pim(self) -> None:
        """Navigate to the PIM module."""
        self._click(*self.PIM_MODULE)

    def logout(self) -> None:
        """Perform the logout action."""
        self._click(*self.USER_DROPDOWN)
        self._click(*self.LOGOUT_LINK)

    def is_user_dropdown_visible(self) -> bool:
        """Check if the user dropdown is visible (indicates successful login).

        Returns:
            bool: True if user dropdown is visible, False otherwise
        """
        return self._is_element_visible(*self.USER_DROPDOWN)

    def get_logged_in_user_name(self) -> str:
        """Get the name of the currently logged-in user.

        Returns:
            str: The logged-in user's name
        """
        self._click(*self.USER_DROPDOWN)
        return self._get_text(*self.USER_NAME_IN_DROPDOWN)