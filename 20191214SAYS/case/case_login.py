import unittest

import time

from page.adviser.login_page import loginProxy

def data():
    with open('./data/loginInfo.txt') as f:


class Login(unittest.TestCase):

    def test_01(self):
        url="https://adviser.osid.org.cn/"
        self.login=loginProxy(url)
        self.login.login('15549080517','Aa1234')
        time.sleep(3)
        self.login.loginOut()