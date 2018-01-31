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
        # 园子
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[1]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/yuanzi.jpg")
        self.driver.back()
        # 新闻
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[2]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/xinwen.jpg")
        self.driver.back()
        # 博问
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[3]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/bowen.jpg")
        self.driver.back()
        # 闪存
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[4]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/shancun.jpg")
        self.driver.back()
        # 小组
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[5]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/xiaozu.jpg")
        self.driver.back()
        # 收藏
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[6]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/shoucang.jpg")
        self.driver.back()
        # 招聘
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[7]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/zhaop.jpg")
        self.driver.back()
        # 班级
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[8]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/banji.jpg")
        self.driver.back()
        # 找找看
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="nav_menu"]/a[9]').click()
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/zhaozhaokan.jpg")
        self.driver.back()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
