from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('promo_num', [1,2,3,4,5,6,7,8,9])
def test_guest_can_add_product_to_basket(browser,promo_num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_correct_success_message()
    page.should_be_correct_basket_price()
