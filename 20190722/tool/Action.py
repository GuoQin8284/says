class Actions():

    def __init__(self,driver):
        self.driver=driver

    def find_ele(self,ele):
        return self.driver.find_element(ele[0],ele[1])