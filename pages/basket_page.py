from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_have_no_items(self):
        elements_counter = len(self.browser.find_elements(*BasketPageLocators.CONTENT_INNER))
        assert elements_counter == 1, "Basket is expected to be empty, but it is not"
    
    def should_have_items(self):
        elements_counter = len(self.browser.find_elements(*BasketPageLocators.CONTENT_INNER))
        assert elements_counter > 1, "Basket is to have items, but it is empty"