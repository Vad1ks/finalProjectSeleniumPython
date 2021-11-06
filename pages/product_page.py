from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_correct_success_message(self):
        product_name = self.get_product_name()
        actual_success_message = self.get_success_message()
        assert product_name == actual_success_message, "Success message is incorrect"

    def should_be_correct_basket_price(self):
        actual_basket_price = self.get_basket_price()
        expected_basket_price = self.get_product_price()
        assert actual_basket_price == expected_basket_price, "The  basket price is incorrect"

    def get_success_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text