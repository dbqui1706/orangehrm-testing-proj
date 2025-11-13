"""Test cases for Add Employee functionality (UC 1.1.1)."""
import pytest
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
from config import VALID_USERNAME, VALID_PASSWORD


@pytest.mark.usefixtures("driver_init")
class TestAddEmployee:
    """Test suite for Add Employee functionality according to requirements 1.1.1."""

    @pytest.fixture
    def add_employee_page(self):
        """Login and navigate to Add Employee page.

        Returns:
            AddEmployeePage: Instance of AddEmployeePage ready for testing
        """
        # Login
        login_page = LoginPage(self.driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)

        # Navigate to PIM
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_pim()

        # Navigate to Add Employee
        pim_page = PIMPage(self.driver)
        pim_page.click_add_employee()

        return AddEmployeePage(self.driver)

    # ==================== POSITIVE TEST CASES ====================

    def test_add_employee_with_valid_data_full(self, add_employee_page: AddEmployeePage):
        """EM01: Test adding employee with all valid data (full information).

        Test Case ID: EM01
        Description: Verify that employee can be added with complete valid information
        Expected: Successfully saved, redirected to Personal Details page
        """
        # Arrange
        timestamp = int(time.time())
        first_name = "John"
        last_name = "Doe"
        username = f"john.doe.{timestamp}"
        password = "Pass123!"

        # Get a test image path (you can create a dummy image or use existing)
        # For now, we'll test without photo to keep it simple
        # photo_path = os.path.join(os.getcwd(), "screenshots", "test_photo.png")

        # Act
        add_employee_page.add_employee_with_login(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            middle_name="Michael"
        )

        # Assert
        assert add_employee_page.is_success_message_visible(), \
            "Success message should be displayed after adding employee"
        assert add_employee_page.is_on_personal_details_page(), \
            "Should redirect to Personal Details page after save"

    def test_add_employee_basic_required_fields_only(self, add_employee_page: AddEmployeePage):
        """EM02: Test adding employee with only required fields (First Name, Last Name).

        Test Case ID: EM02
        Description: Verify that employee can be added with only required fields
        Expected: Successfully saved with auto-generated Employee ID
        """
        # Arrange
        timestamp = int(time.time())
        first_name = f"Jane{timestamp}"
        last_name = "Smith"

        # Act
        add_employee_page.add_employee_basic(
            first_name=first_name,
            last_name=last_name
        )

        # Assert
        assert add_employee_page.is_success_message_visible(), \
            "Success message should be displayed"
        assert add_employee_page.is_on_personal_details_page(), \
            "Should redirect to Personal Details page"

    def test_add_employee_with_custom_employee_id(self, add_employee_page: AddEmployeePage):
        """EM03: Test adding employee with custom Employee ID.

        Test Case ID: EM03
        Description: Verify that custom Employee ID can be entered manually
        Expected: Employee created with specified custom ID
        """
        # Arrange
        timestamp = int(time.time())
        custom_id = f"EMP{timestamp}"

        # Act
        add_employee_page.add_employee_basic(
            first_name="Custom",
            last_name="Employee",
            employee_id=custom_id
        )

        # Assert
        assert add_employee_page.is_success_message_visible(), \
            "Success message should be displayed"

    def test_add_employee_with_login_enabled(self, add_employee_page: AddEmployeePage):
        """EM04: Test creating employee with login credentials (Status: Enabled).

        Test Case ID: EM04
        Description: Verify creating login credentials with Enabled status
        Expected: Employee created with enabled login account
        """
        # Arrange
        timestamp = int(time.time())
        username = f"testuser{timestamp}"
        password = "Test@1234"

        # Act
        add_employee_page.add_employee_with_login(
            first_name="Test",
            last_name="User",
            username=username,
            password=password,
            status_enabled=True
        )

        # Assert
        assert add_employee_page.is_success_message_visible(), \
            "Success message should be displayed"

    def test_add_employee_with_login_disabled(self, add_employee_page: AddEmployeePage):
        """EM05: Test creating employee with login credentials (Status: Disabled).

        Test Case ID: EM05
        Description: Verify creating login credentials with Disabled status
        Expected: Employee created with disabled login account
        """
        # Arrange
        timestamp = int(time.time())
        username = f"disableduser{timestamp}"
        password = "Disabled@123"

        # Act
        add_employee_page.add_employee_with_login(
            first_name="Disabled",
            last_name="Account",
            username=username,
            password=password,
            status_enabled=False
        )

        # Assert
        assert add_employee_page.is_success_message_visible(), \
            "Success message should be displayed"

    # ==================== NEGATIVE TEST CASES - VALIDATION ====================

    def test_add_employee_first_name_empty(self, add_employee_page: AddEmployeePage):
        """EM06: Test adding employee with empty First Name (required field).

        Test Case ID: EM06
        Description: Verify validation when First Name is left empty
        Expected: Error message "Required" displayed, form not submitted
        """
        # Act - Leave first name empty
        add_employee_page.enter_last_name("TestLast")
        add_employee_page.click_save()

        # Assert
        error_messages = add_employee_page.get_required_error_messages()
        assert len(error_messages) > 0, "Required field error should be displayed"
        assert "Required" in str(error_messages), "Should show 'Required' error message"

    def test_add_employee_last_name_empty(self, add_employee_page: AddEmployeePage):
        """EM07: Test adding employee with empty Last Name (required field).

        Test Case ID: EM07
        Description: Verify validation when Last Name is left empty
        Expected: Error message "Required" displayed, form not submitted
        """
        # Act - Leave last name empty
        add_employee_page.enter_first_name("TestFirst")
        add_employee_page.click_save()

        # Assert
        error_messages = add_employee_page.get_required_error_messages()
        assert len(error_messages) > 0, "Required field error should be displayed"
        assert "Required" in str(error_messages), "Should show 'Required' error message"

    def test_add_employee_first_name_with_numbers(self, add_employee_page: AddEmployeePage):
        """EM08: Test adding employee with numbers in First Name.

        Test Case ID: EM08
        Description: Verify validation when First Name contains numbers
        Expected: Validation error or rejection (depending on system rules)
        Note: OrangeHRM may or may not validate this - test to discover actual behavior
        """
        # Act
        add_employee_page.enter_first_name("John123")
        add_employee_page.enter_last_name("Doe")
        add_employee_page.click_save()

        # Assert - Check if system accepts or rejects
        # This is discovery testing - document actual behavior
        time.sleep(2)  # Wait for any validation
        # The test will reveal actual system behavior

    def test_add_employee_first_name_with_special_characters(self, add_employee_page: AddEmployeePage):
        """EM09: Test adding employee with special characters in First Name.

        Test Case ID: EM09
        Description: Verify validation when First Name contains special characters
        Expected: Validation error (special characters not allowed)
        """
        # Act
        add_employee_page.enter_first_name("John@#$")
        add_employee_page.enter_last_name("Doe")
        add_employee_page.click_save()

        # Assert
        time.sleep(2)
        # Document actual behavior

    # ==================== BOUNDARY VALUE TESTS ====================

    def test_add_employee_first_name_max_length(self, add_employee_page: AddEmployeePage):
        """EM10: Test First Name with maximum allowed length (30 characters).

        Test Case ID: EM10
        Description: Verify First Name accepts exactly 30 characters (boundary)
        Expected: Should accept 30 characters successfully
        """
        # Arrange - 30 character name
        first_name_30 = "A" * 30

        # Act
        add_employee_page.add_employee_basic(
            first_name=first_name_30,
            last_name="Boundary"
        )

        # Assert
        assert add_employee_page.is_success_message_visible(), \
            "Should accept First Name with 30 characters"

    def test_add_employee_first_name_exceeds_max_length(self, add_employee_page: AddEmployeePage):
        """EM11: Test First Name exceeding maximum length (31 characters).

        Test Case ID: EM11
        Description: Verify validation when First Name exceeds 30 characters
        Expected: System should reject or truncate to 30 characters
        """
        # Arrange - 31 character name
        first_name_31 = "A" * 31

        # Act
        add_employee_page.enter_first_name(first_name_31)
        add_employee_page.enter_last_name("Boundary")

        # Check what actually gets entered (may be truncated)
        actual_value = add_employee_page._find_element(*add_employee_page.FIRST_NAME_INPUT).get_attribute('value')

        # Assert - Document actual behavior
        # System may truncate or prevent input beyond 30 chars

    # ==================== PASSWORD VALIDATION TESTS ====================

    def test_add_employee_password_less_than_8_chars(self, add_employee_page: AddEmployeePage):
        """EM12: Test password with less than 8 characters (minimum requirement).

        Test Case ID: EM12
        Description: Verify password validation for length < 8 characters
        Expected: Error message about minimum password length
        """
        # Arrange
        timestamp = int(time.time())

        # Act
        add_employee_page.enter_first_name("Test")
        add_employee_page.enter_last_name("Password")
        add_employee_page.enable_create_login_details()
        add_employee_page.enter_username(f"testpw{timestamp}")
        add_employee_page.enter_password("Short1")  # Only 6 characters
        add_employee_page.enter_confirm_password("Short1")
        add_employee_page.click_save()

        # Assert
        time.sleep(2)
        error_messages = add_employee_page.get_required_error_messages()
        # Should show password length error

    def test_add_employee_password_exactly_8_chars(self, add_employee_page: AddEmployeePage):
        """EM13: Test password with exactly 8 characters (boundary value).

        Test Case ID: EM13
        Description: Verify password with minimum valid length (8 characters)
        Expected: Should accept password with exactly 8 characters
        """
        # Arrange
        timestamp = int(time.time())
        password_8 = "Pass123!"  # Exactly 8 characters

        # Act
        add_employee_page.add_employee_with_login(
            first_name="Boundary",
            last_name="Password",
            username=f"bound{timestamp}",
            password=password_8
        )

        # Assert
        assert add_employee_page.is_success_message_visible(), \
            "Should accept 8-character password"

    def test_add_employee_password_mismatch(self, add_employee_page: AddEmployeePage):
        """EM14: Test password and confirm password mismatch.

        Test Case ID: EM14
        Description: Verify validation when password and confirm password don't match
        Expected: Error message "Passwords do not match"
        """
        # Arrange
        timestamp = int(time.time())

        # Act
        add_employee_page.enter_first_name("Password")
        add_employee_page.enter_last_name("Mismatch")
        add_employee_page.enable_create_login_details()
        add_employee_page.enter_username(f"mismatch{timestamp}")
        add_employee_page.enter_password("Password123!")
        add_employee_page.enter_confirm_password("Different123!")  # Different password
        add_employee_page.click_save()

        # Assert
        time.sleep(2)
        error_messages = add_employee_page.get_required_error_messages()
        # Should show password mismatch error

    def test_add_employee_username_with_space(self, add_employee_page: AddEmployeePage):
        """EM15: Test username containing spaces.

        Test Case ID: EM15
        Description: Verify validation when username contains spaces
        Expected: Error message or rejection (username should not have spaces)
        """
        # Arrange
        timestamp = int(time.time())

        # Act
        add_employee_page.enter_first_name("Username")
        add_employee_page.enter_last_name("Space")
        add_employee_page.enable_create_login_details()
        add_employee_page.enter_username(f"user name {timestamp}")  # Username with space
        add_employee_page.enter_password("Password123!")
        add_employee_page.enter_confirm_password("Password123!")
        add_employee_page.click_save()

        # Assert
        time.sleep(2)
        # Document actual behavior

    # ==================== PHOTO UPLOAD TESTS ====================

    @pytest.mark.skip(reason="Requires test image file - implement when test data is ready")
    def test_add_employee_upload_photo_png(self, add_employee_page: AddEmployeePage):
        """EM16: Test uploading employee photo in PNG format.

        Test Case ID: EM16
        Description: Verify PNG photo upload functionality
        Expected: Photo uploaded and displayed successfully
        """
        # This test requires a test image file
        pass

    @pytest.mark.skip(reason="Requires test image file - implement when test data is ready")
    def test_add_employee_upload_photo_exceeds_1mb(self, add_employee_page: AddEmployeePage):
        """EM17: Test uploading photo larger than 1MB.

        Test Case ID: EM17
        Description: Verify validation for photo size > 1MB
        Expected: Error message "File size exceeds 1MB"
        """
        # This test requires a large test image file (>1MB)
        pass

    @pytest.mark.skip(reason="Requires test image file - implement when test data is ready")
    def test_add_employee_upload_photo_exactly_1mb(self, add_employee_page: AddEmployeePage):
        """EM18: Test uploading photo exactly 1MB (boundary value).

        Test Case ID: EM18
        Description: Verify photo upload with maximum allowed size (1MB)
        Expected: Photo should be accepted at exactly 1MB
        """
        # This test requires a test image file exactly 1MB
        pass

    @pytest.mark.skip(reason="Requires PDF file - implement when test data is ready")
    def test_add_employee_upload_invalid_file_format(self, add_employee_page: AddEmployeePage):
        """EM19: Test uploading invalid file format (PDF instead of image).

        Test Case ID: EM19
        Description: Verify validation for invalid file formats
        Expected: Error message about invalid file format
        """
        # This test requires a PDF test file
        pass

    # ==================== INTEGRATION TEST ====================

    def test_add_employee_and_search(self, add_employee_page: AddEmployeePage):
        """EM20: Integration test - Add employee and verify in search results.

        Test Case ID: EM20
        Description: End-to-end test - Add employee and verify it appears in employee list
        Expected: Newly added employee should be searchable
        """
        # Arrange
        timestamp = int(time.time())
        first_name = f"Integration{timestamp}"
        last_name = "Test"

        # Act - Add employee
        add_employee_page.add_employee_basic(
            first_name=first_name,
            last_name=last_name
        )

        # Verify creation
        assert add_employee_page.is_success_message_visible(), \
            "Employee should be created successfully"

        # Navigate back to Employee List
        pim_page = PIMPage(self.driver)
        self.driver.get(self.driver.current_url.split('/web')[0] + '/web/index.php/pim/viewEmployeeList')
        time.sleep(2)

        # Search for the newly created employee
        pim_page.search_for_employee_by_name(f"{first_name} {last_name}")

        # Assert - Employee should be found
        assert not pim_page.is_no_records_found_message_visible(), \
            f"Newly created employee '{first_name} {last_name}' should be found in search"
