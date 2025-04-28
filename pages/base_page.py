from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    def find_element(self, locator):
        """Find a single element on the page using a locator."""
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Find multiple elements on the page using a locator."""
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Click on an element located by the locator."""
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        """Enter text into an input field located by the locator."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
