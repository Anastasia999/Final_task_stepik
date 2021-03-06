from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        #self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    #def should_be_login_url(self):
        #assert self.browser.correct_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Incorrect page" # реализуйте проверку на корректный url адрес
        #assert True

    def should_be_login_form(self):
        assert self.should_be_login_form(*LoginPageLocators.LOGIN_FORM), "Missing login form" # реализуйте проверку, что есть форма логина
        #assert True

    def should_be_register_form(self):
        assert self.should_be_register_form(*LoginPageLocators.REGISTER_FORM), "Missing register form"# реализуйте проверку, что есть форма регистрации на странице
        #assert True