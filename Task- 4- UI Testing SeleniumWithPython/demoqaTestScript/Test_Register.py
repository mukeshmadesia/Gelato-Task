from demoqaConfig.ReadConfig import ReadConfig as RC
from demoqaTests.BaseTest import BaseTest
from demoqaUtilis.TestDataRead import TestDataRead as td
import pytest
from ddt import data, unpack


class Test_Register(BaseTest):

    # username, password = td.test_data_read()
    # firstname, lastname = td.test_name_read()

    def test_register_page_title(self):

        reg = self.Register(self.driver)
        register_title = self.reg.get_title(RC.getTitle())

        if register_title == RC.getTitle():
            assert True
        else:
            assert False

    @data(*td.read_data_from_csv("../demoqaTestData/testdata.csv"))
    @unpack
    def test_user_registration(self, firstname, lastname, username, password):

        reg = self.Register(self.driver)
        text = self.reg.do_register(firstname, lastname, username, password)

        if text == "User Register Successfully.":
            assert True
        else:
            assert False

    @data(*td.read_data_from_csv("../demoqaTestData/testdata.csv"))
    @unpack
    def test_user_already_register(self, firstname, lastname, username, password):

        reg = self.Register(self.driver)
        text = self.reg.do_register(firstname, lastname, username, password)

        if text == "User exists!":
            assert True
        else:
            assert False




