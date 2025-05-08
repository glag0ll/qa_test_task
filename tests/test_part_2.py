# test_part_2.py
from pages.page_1 import ExamplePage
import time


def test_example_page_actions(driver):
    page = ExamplePage(driver)

    title = page.verify_title()
    assert "Example" in title
    print('\nпроверка заголовка успешна')

    page.click_more_info()

    time.sleep(2)

    current_url = page.verify_current_url()
    assert "iana.org/help/example-domains" in current_url
    print('\nпроверка URL успешна')