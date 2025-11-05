"""Test cases for PIM (Personal Information Management) functionality."""
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.usefixtures("driver_init")
class TestPIM:
    """Test suite for PIM employee search functionality."""

    @pytest.fixture
    def pim_page(self):
        """Login and navigate to the PIM page.

        Returns:
            PIMPage: Instance of PIMPage after successful login and navigation
        """
        # Login
        login_page = LoginPage(self.driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        # Navigate to PIM
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_pim()

        return PIMPage(self.driver)

    def test_search_employee_by_name(self, pim_page: PIMPage):
        """Test successful employee search with valid employee name.
        Args:
            pim_page (PIMPage): Instance of PIMPage is provided by the fixture from above.
        """
        # Arrange - Get the logged-in user's name
        dashboard_page = DashboardPage(self.driver)
        employee_name = dashboard_page.get_logged_in_user_name()

        # Act
        pim_page.search_for_employee_by_name(employee_name)

        # Assert
        assert not pim_page.is_no_records_found_message_visible(), \
            f"Search failed: 'No Records Found' message shown for employee '{employee_name}'"
        assert pim_page.are_search_results_visible(), \
            f"Search results not displayed for employee '{employee_name}'"

    def test_search_for_nonexistent_employee(self, pim_page: PIMPage):
        """Test employee search with non-existent employee name."""
        # Arrange
        nonexistent_employee = "NonExistentEmployee12345"

        # Act
        pim_page.search_for_employee_by_name(nonexistent_employee)

        # Assert
        assert pim_page.is_no_records_found_message_visible(), \
            f"Expected 'No Records Found' message for non-existent employee '{nonexistent_employee}'"