from pages.login_page import LoginPage
from tests.base_test import BaseTest
from utilities.test_data import TestData


class TestLogin(BaseTest):

  def test_valid_credentials(self):
    login_page = LoginPage(self.driver)
    login_page.set_email_address(TestData.email)
    login_page.set_password(TestData.password)
    login_page.click_login_button()
    























