from selenium import webdriver

class Driver:
    @classmethod
    def SetupDriver(cls):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(15)
        return driver