"""Pytest configuration file containing fixtures and hooks."""
import pytest
import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from config import SCREENSHOTS_DIR

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress WebDriver Manager logs to speed up initialization
logging.getLogger('WDM').setLevel(logging.ERROR)


@pytest.fixture(scope="function")
def driver_init(request):
    """Initialize the WebDriver with proper configuration.

    Args:
        request: Pytest request object

    Yields:
        WebDriver: Configured Chrome WebDriver instance
    """
    logger.info("Initializing WebDriver")

    # Configure Chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")

    # Uncomment for headless mode
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")

    # Initialize driver - WebDriver Manager will cache automatically
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Implicit wait
    driver.implicitly_wait(10)

    # Attach driver to test class
    request.cls.driver = driver

    logger.info("WebDriver initialized successfully")
    yield driver

    logger.info("Quitting WebDriver")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on test failure.

    Args:
        item: The test item
        call: The test call
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        logger.warning(f"Test failed: {item.name}")

        try:
            # Get driver from test class
            driver = item.cls.driver

            # Create screenshots directory if it doesn't exist
            if not os.path.exists(SCREENSHOTS_DIR):
                os.makedirs(SCREENSHOTS_DIR)
                logger.info(f"Created screenshots directory: {SCREENSHOTS_DIR}")

            # Generate unique filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_filename = f"{item.name}_{timestamp}_failure.png"
            screenshot_path = os.path.join(SCREENSHOTS_DIR, screenshot_filename)

            # Save screenshot
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved: {screenshot_path}")

            # Add screenshot to HTML report if pytest-html is installed
            if hasattr(report, 'extra'):
                try:
                    import pytest_html
                    report.extra.append(pytest_html.extras.image(screenshot_path))
                except ImportError:
                    logger.debug("pytest-html not installed, skipping report attachment")

        except Exception as e:
            logger.error(f"Failed to capture screenshot: {str(e)}")
