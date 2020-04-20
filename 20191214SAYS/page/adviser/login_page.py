import time
from selenium.webdriver.common.by import By

from page.Base import Base_page, Base_handle


class LoginPage(Base_page):

    def __init__(self,url):
        print("url",url)
        super().__init__(url)

        self.loginName=(By.NAME,'username')
        self.loginPwd=(By.NAME,'password')
        self.loginBtn=(By.XPATH,'//*[@id="App"]/div/div[2]/div/div/section[2]/div/section/form/button')
        self.loginOutBtn=(By.XPATH,'//*[@id="App"]/div/div[2]/main/div[1]/div[2]/div[3]/ul/li')
        self.loginLogo=(By.XPATH,'//*[@id="App"]/div/div[2]/main/div[1]/div[2]/div[3]/div/span')
        self.confirm=(By.XPATH,'//*[@id="App"]/div/div[2]/div/div[2]/div[2]/button[2]')

    def ele_loginName(self):
        return self.find_element(self.loginName)

    def ele_loginPwd(self):
        return self.find_element(self.loginPwd)

    def ele_loginBtn(self):
        return self.find_element(self.loginBtn)

    def ele_loginOutBtn(self):
        return self.find_element(self.loginOutBtn)

    def ele_loginLogo(self):
        return self.find_element(self.loginLogo)

    # 确认退出
    def ele_confirm(self):
        return self.find_element(self.confirm)


class LoginHandle(Base_handle):

    def __init__(self,url):
        self.loginPage=LoginPage(url)

    def inputName(self,name):
        self.Input_text(self.loginPage.ele_loginName(),name)

    def inputPwd(self,pwd):
        self.Input_text(self.loginPage.ele_loginPwd(),pwd)

    def clickLogin(self):
        self.Click(self.loginPage.ele_loginBtn())

    def clickLoginOut(self):
        self.Click(self.loginPage.ele_loginOutBtn())

    def hover_logo(self):
        self.loginPage.Hover(self.loginPage.ele_loginLogo()).perform()

    def clickConfirm(self):
        self.Click(self.loginPage.ele_confirm())


class loginProxy():

    def __init__(self,url):
        self.loginhandle=LoginHandle(url)
    # 登录
    def login(self,name,pwd):
        self.loginhandle.inputName(name)
        self.loginhandle.inputPwd(pwd)
        self.loginhandle.clickLogin()

    # 退出登录
    def loginOut(self):
        self.loginhandle.hover_logo()
        time.sleep(1)
        self.loginhandle.clickLoginOut()
        self.loginhandle.clickConfirm()