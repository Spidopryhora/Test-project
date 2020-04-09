from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def verify_book_title_in_success_message(self):
        product_title_text = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        title_book_success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_title_text == title_book_success_message, f'Expected {product_title_text}, ' \
                                                                 f'got {title_book_success_message}'

    def verify_book_price_in_cart(self):
        product_price_value = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_price_value = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert product_price_value in cart_price_value, f'Expected {product_price_value}, ' \
                                                                            f'got {cart_price_value}'
