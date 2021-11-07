from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inv")
    BASKET = (By.XPATH, "//a[contains(@href, 'basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    CONTENT_INNER = (By.CSS_SELECTOR, "#content_inner")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")
    ICON_REG_SUCCESSFULL = (By.CSS_SELECTOR, ".icon-ok-sign")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR , ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p")
    BASKET_PRICE = (By.XPATH, "//*[@id='messages']/div[3]/div/p/strong")