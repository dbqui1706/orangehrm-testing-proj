"""Config base for pytest fixtures."""
import pytest
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from utils.helpers import get_screenshot_name

@pytest.fixture(scope="function")
def driver(request):
    """Initialize and return a WebDriver instance."""
    
    # Chorme options
    options = Options()
    # options.add_argument("--headless")  
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    
    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown
    driver.quit()
    
    
@pytest.fixture(scope="function")
def screenshot_on_failure(request, driver):
    """Take a screenshot if a test fails."""
    yield
    # Check if the test has failed
    if request.node.rep_call.failed:
        test_name = request.node.name
        screenshot_name = get_screenshot_name(test_name)
        screenshot_path = os.path.join("screenshots", screenshot_name)
        driver.save_screenshot(screenshot_path)
        print(f"\n📸 Screenshot saved: {screenshot_path}")
        
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook để lưu test result"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"report_{rep.when}", rep)