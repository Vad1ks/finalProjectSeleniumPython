from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

    def should_be_correct_success_message(self):
        expected_success_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text \
     + " has been added to your basket."
        actual_success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert expected_success_message == actual_success_message, "Success message is incorrect"

    def should_be_correct_basket_price(self):
        actual_basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        expected_basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert actual_basket_price == expected_basket_price, "The  basket price is incorrect"