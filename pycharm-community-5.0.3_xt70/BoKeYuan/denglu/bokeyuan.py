from selenium import webdriver
import unittest
import time
class Bokeyuan(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://www.cnblogs.com/")
        self.driver.maximize_window()

    def test_login(self):
        self.driver.find_element_by_xpath("//SPAN[@id='span_userinfo']/A[1]").click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("./photograph/denglu.jpg")
        self.driver.find_element_by_xpath("//INPUT[@id='input1']").send_keys("xjh214")
        time.sleep(3)
        self.driver.get_screenshot_as_file("./photograph/name.jpg")
        self.driver.find_element_by_xpath("//INPUT[@id='input2']").send_keys("xjh19960214@")
        time.sleep(3)
        self.driver.get_screenshot_as_file("./photograph/password.jpg")
        self.driver.find_element_by_xpath("//INPUT[@id='signin']").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("./photograph/succeed.jpg")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main___":
    unittest.main()
