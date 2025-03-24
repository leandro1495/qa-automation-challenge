from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.web_tests.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.NAME, "search")
    SEARCH_BUTTON = (By.XPATH, "//i[contains(@data-jsl10n,'search-input-button')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.wikipedia.org/")

    def search(self, keyword):
        self.find_element(self.SEARCH_BOX).send_keys(keyword)
        self.find_element(self.SEARCH_BUTTON).click()

class SearchResultsPage(BasePage):
    FIRST_HEADING = (By.ID, "firstHeading")

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_heading(self):
        return self.find_element(self.FIRST_HEADING).text