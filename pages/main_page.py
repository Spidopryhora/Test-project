from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.ID, "login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.ID, 'login_link'), 'Login link is not present'
