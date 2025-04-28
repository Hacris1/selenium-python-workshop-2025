from selenium.webdriver.common.by import By
import time
from .base_page import BasePage

class IntuLogin(BasePage):
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'loginbtn')
    ERROR_MSG = (By.XPATH, '/html/body/div[6]/div/div/section/div/div/div/div/div/div/div[2]/div')

    def login(self, username, password):
        self.enter_text(self.USERNAME_FIELD, username)
        self.enter_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def isElementPresent(self):
        elemento = self.find_element(self.ERROR_MSG)
        texto = elemento.text
        return texto