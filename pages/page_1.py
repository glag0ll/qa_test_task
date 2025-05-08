from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExamplePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    # Локаторы элементов
    more_info = (By.CSS_SELECTOR, "body > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)")

    def verify_title(self):
        self.wait.until(EC.title_contains("Example"))
        return self.driver.title

    def click_more_info(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.more_info)
        )
        element.click()
        print('\nклик успешен')

    def verify_current_url(self):
        self.wait.until(EC.url_contains("iana.org/help/example-domains"))
        print('\nпереход на другую страницу успешен')
        return self.driver.current_url