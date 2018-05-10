import unittest
from page.loginpage import loginpage

from selenium import webdriver



class TestNewBug(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.drriver = webdriver.Firefox()
        cls.login = loginpage(cls.drriver)
        cls.newbug = NewBug(cls.drriver)

    def test_new_bug(self):
        self.login.login()# 登录
        self.newbug.click