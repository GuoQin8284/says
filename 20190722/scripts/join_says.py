import json
import unittest

import parameterized

from page.home_page import ToolsProxy
from page.tools_login_page import LoginProxy
from setup_driver.setup_driver import Driver


def data():
    with open(r"F:\Python_code\20190722\data\tools_login_data.json","r",encoding="utf-8") as f:
        # data1=json.load(f).get("login")
        data1 = json.load(f)
        print(data1)
        print(type(data1))
        data2=data1.get("login")
        data_list=[]
        data_list.append(
            (data2.get("name"),
             data2.get("pwd")
             )
        )
    print(data_list)
    return data_list


class JoinSays(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver=Driver().SetupDriver()
        self.driver.get("http://tool.chubanyun.me/square")
        self.login=LoginProxy(self.driver)
        self.tools_says=ToolsProxy(self.driver)

    def tearDown(self):
        pass
    @parameterized.parameterized.expand(data())
    def test01(self,name,pwd):
        self.login.login(name,pwd)

    def test02(self):
        self.tools_says.says_proxy(10)