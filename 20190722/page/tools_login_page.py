import time
from selenium.webdriver.common.by import By

from tool.Action import Actions


class Tools_login_page(Actions):
    def __init__(self,driver):
        super().__init__(driver)

        self.login_name=(By.XPATH,'//input[@placeholder="姓名"]')
        self.login_pwd=(By.XPATH,'//input[@placeholder="密码"]')
        self.login=(By.XPATH,'//span[text()="登录"]')

    def name_ele(self):
        return self.find_ele(self.login_name)

    def pwd_ele(self):
        return self.find_ele(self.login_pwd)

    def login_ele(self):
        return self.find_ele(self.login)

class LoginAction(Tools_login_page):

    def input_name(self,name):
        self.name_ele().send_keys(name)

    def input_pwd(self,pwd):
        self.pwd_ele().send_keys(pwd)

    def click_login(self):
        self.login_ele().click()

class LoginProxy(LoginAction):

    def login(self,name,pwd):
        self.input_name(name)
        self.input_pwd(pwd)
        time.sleep(1)
        self.click_login()