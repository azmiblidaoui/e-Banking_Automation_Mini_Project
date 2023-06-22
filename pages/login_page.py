from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
  email_address_field = (By.XPATH, "/html/body/form/table/tbody/tr[1]/td[2]/input")
  password_field = (By.XPATH, "/html/body/form/table/tbody/tr[2]/td[2]/input")
  login_button = (By.NAME, "btnLogin")

  def __init__(self, driver):
    super().__init__(driver)

  def set_email_address(self, email_address):
    self.set(self.email_address_field, email_address)

  def set_password(self, password):
    self.set(self.password_field, password)

  def click_login_button(self):
    self.click(self.login_button)
    

  def log_into_application(self, email, password):
    self.set_email_address(email)
    self.set_password(password)
    self.click_login_button()
    