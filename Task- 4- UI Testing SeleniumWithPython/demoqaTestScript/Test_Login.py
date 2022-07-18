from demoqaConfig.ReadConfig import ReadConfig as RC
from demoqaPages.LoginPage import LoginPage
from demoqaTests.BaseTest import BaseTest
from demoqaUtilis.TestDataRead import TestDataRead as td
import pytest
from ddt import data, unpack


class Test_Login(BaseTest):

    def test_login_page_title(self):

        lp = LoginPage(self.driver)
        login_title = self.lp.get_title(RC.getTitle())

        if login_title == RC.getTitle():
            assert True
        else:
            assert False

    @data(*td.read_data_from_csv("../demoqa.TestData/testData.csv"))
    @unpack
    def test_user_login(self, username, password):
        lp = LoginPage(self.driver)
        user_value = self.lp.do_login(username, password)
        assert user_value == username

    @data(*td.read_data_from_csv("../demoqa.TestData/testData.csv"))
    @unpack
    def test_user_invalid(self, username, password):
        lp = LoginPage(self.driver)
        invalid_value = self.lp.do_login_invalid(username, password)

        assert invalid_value == "Invalid username or password!"

