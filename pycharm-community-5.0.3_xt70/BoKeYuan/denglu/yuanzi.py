from selenium import webdriver
import time
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.get("https://www.cnblogs.com/")

    def test_yuanzi(self):
        self.driver.find_element_by_xpath('//*[@id="span_userinfo"]/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="input1"]').send_keys("xjh214")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="input2"]').send_keys("xjh19960214@")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="signin"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="txt_ing"]').send_keys("测试数据")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="ing_type_private"]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="btn_ing_publish"]').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
