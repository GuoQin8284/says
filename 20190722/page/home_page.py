from selenium.webdriver.common.by import By

from tool.Action import Actions


class ToolsLogin(Actions):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.tools_says=By.XPATH,'//*[@id="Duoyue"]/div/div[1]/div/section/div[1]/div[1]/ul/li[2]'
        self.tools_rays=By.XPATH,'//*[@id="Duoyue"]/div/div[1]/div/section/div[1]/div[1]/ul/li[1]'

        self.path='//*[@id="Duoyue"]/div/div[1]/div/section/div[1]/div[1]'
        self.says_list=['/section[1]/ul/li[2]','/section[1]/ul/li[3]','/section[1]/ul/li[4]','/section[1]/ul/li[5]',
                   '/section[2]/ul/li[2]','/section[2]/ul/li[3]','/section[2]/ul/li[4]',
                   '/section[3]/ul/li[2]','/section[3]/ul/li[3]','/section[3]/ul/li[4]','/section[3]/ul/li[5]'
                   ]
    def tools_says_path(self,n):
        return self.path+self.says_list[n+1]

    def tools_says_ele(self):
        return self.find_ele(self.tools_says)

    def tools_rays_ele(self):
        return self.find_ele(self.tools_rays)

    def says_find_element(self,n,):
        return self.find_ele((By.XPATH,self.tools_says_path(n)))

class ToolsAction(ToolsLogin):

    def says_find_element_click(self,n):
        self.says_find_element(n).click()

    def tools_says_ele_click(self):
        self.tools_says_ele().click()

    def tools_rays_ele_click(self):
        self.tools_rays_ele().click()

class ToolsProxy(ToolsAction):
    def says_proxy(self,n):
        self.tools_says_ele_click()
        self.says_find_element_click(n)

    def rays_proxy(self):
        self.tools_rays_ele_click()
