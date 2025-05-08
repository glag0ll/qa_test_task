import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    options.add_experimental_option("detach", True)

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    driver.maximize_window()
    driver.get("https://example.com")

    yield driver

    driver.quit()