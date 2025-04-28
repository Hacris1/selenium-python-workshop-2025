from selenium.webdriver.common.by import By
from .base_page import BasePage

class MercadoLibreSearchPage(BasePage):
    SEARCH_BOX = (By.NAME, 'as_word')
    SEARCH_BUTTON = (By.CLASS_NAME, 'nav-search-btn')
    RESULT_TITLES = (By.XPATH, '/html/body/main/div/div[2]/aside/div[1]/ol/li[3]/a/span')

    def open_homepage(self):
        self.driver.get('https://www.mercadolibre.com.co')

    def search_product(self, query):
        self.enter_text(self.SEARCH_BOX, query)
        self.click(self.SEARCH_BUTTON)

    def verify_results(self, expected_text):
        results = self.find_elements(self.RESULT_TITLES)
        return any(expected_text.lower() in result.text.lower() for result in results)