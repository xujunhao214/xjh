from selenium import webdriver
import unittest
import time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://bbs.51testing.com/forum.php")

    def test_denglu(self):
        self.driver.find_element_by_xpath('//*[@id="lsform"]/div/div[2]/p[1]/a/img').click()
        time.sleep(3)
        iframe=self.driver.find_element_by_xpath('//*[@id="ptlogin_iframe"]')
        self.driver.switch_to_frame(iframe)
        self.driver.find_element_by_xpath('//*[@id="img_out_2535581358"]').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__init__":
    unittest.main()
