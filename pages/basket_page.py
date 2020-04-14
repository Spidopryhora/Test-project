from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_CART)

    def should_be_text_basket_is_empty(self):
        url = self.browser.current_url
        language = url.split('/')[1]
        text_basket_is_empty = self.browser.find_element(*BasketPageLocators.EMPTY_CART_MESSAGE).text
        if 'en' in language:
            assert 'Your basket is empty.' in text_basket_is_empty, f'Expected  "Your basket is empty." got ' \
                                                                    f'{text_basket_is_empty}'
        elif 'fr' in language:
            assert 'Votre panier est vide.' in text_basket_is_empty, f'Expected  "Votre panier est vide." got ' \
                                                                    f'{text_basket_is_empty}'
        elif 'uk' in language:
            assert 'Ваш кошик пустий.' in text_basket_is_empty, f'Expected  "Ваш кошик пустий." got ' \
                                                                     f'{text_basket_is_empty}'
        elif 'ru' in language:
            assert 'Ваша корзина пуста' in text_basket_is_empty, f'Expected  "Ваша корзина пуста" got ' \
                                                                f'{text_basket_is_empty}'
