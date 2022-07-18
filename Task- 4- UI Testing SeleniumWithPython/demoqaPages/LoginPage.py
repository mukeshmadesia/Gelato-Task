from selenium.webdriver.common.by import By
from demoqaConfig.ReadConfig import ReadConfig as RC
from demoqaPages.BasePage import BasePage

"""
This Class is for Actions on Login Page
"""


class LoginPage(BasePage):
    print("--inside loginPage--")
    textbox_username_id = (By.ID, "userName")
    textbox_password_id = (By.ID, "password")
    button_login_id = (By.ID, "login")
    username_value_id = (By.ID, "userName-value")
    invalid_user_id = (By.ID, "name")

    def __init__(self, driver):
        super().__init__(self.driver)
        self.driver.get(RC.getbaseurl()+"/login")

    """ This function is for happy path -
        1. First Enter - username and Password in textbox
        2. Then click login button 
        3. Then return the user_value - to Validate in Test as username
    """

    def do_login(self, username, password):
        self.do_send_keys(self.textbox_username_id, username)
        self.do_send_keys(self.textbox_password_id, password)
        self.do_click(self.button_login_id)
        user_value = self.is_visible(self.username_value_id)

        return user_value

    """ This function is for Negative path -
           1. First Enter - username and Password in textbox
           2. Then click login button 
           3. Then return the invalid - to Validate in Test #Invalid username or password!
    """
    def do_login_invalid(self, username, password):
        self.do_send_keys(self.textbox_username_id, username)
        self.do_send_keys(self.textbox_password_id, password)
        self.do_click(self.button_login_id)
        invalid_value = self.is_visible(self.invalid_user_id)

        return invalid_value




