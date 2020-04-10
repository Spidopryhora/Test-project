from pages.product_page import ProductPage
import time
import pytest


@pytest.mark.parametrize('promo_offer', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail),
                                         '8', '9'])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f'http://selenium1py.pythonanywhere.com/uk/catalogue/coders-at-work_207/?promo=offer{promo_offer}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.verify_book_title_in_success_message()
    page.verify_book_price_in_cart()
