"""End-to-end test cases for the complete user workflow."""
import pytest
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.usefixtures("driver_init")
class TestEndToEnd:
    """Test suite for end-to-end user workflows."""

    def test_e2e_login_search_and_logout(self):
        """Test complete workflow: Login -> Navigate to PIM -> Search Employee -> Logout."""
        # Step 1: Login
        login_page = LoginPage(self.driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        dashboard_page = DashboardPage(self.driver)
        assert dashboard_page.is_user_dropdown_visible(), \
            "Login failed: User dropdown not visible on dashboard"

        # Step 2: Navigate to PIM
        dashboard_page.navigate_to_pim()
        pim_page = PIMPage(self.driver)

        # Step 3: Search for employee
        employee_name = dashboard_page.get_logged_in_user_name()
        pim_page.search_for_employee_by_name(employee_name)

        assert not pim_page.is_no_records_found_message_visible(), \
            f"Employee search failed: 'No Records Found' for '{employee_name}'"
        assert pim_page.are_search_results_visible(), \
            f"Employee search failed: No results displayed for '{employee_name}'"

        # Step 4: Logout
        dashboard_page.logout()

        # Verify user is redirected to login page
        assert login_page.is_on_login_page(), \
            "Logout failed: User not redirected to login page"
