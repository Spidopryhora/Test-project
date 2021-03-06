from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inv')
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a.btn-default')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCTS_IN_CART = (By.CSS_SELECTOR, 'div.basket-items')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner p')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_REPEAT_PASS = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner strong')
    CART_PRICE = (By.CSS_SELECTOR, 'div.basket-mini')
