from selenium import webdriver
import time
import unittest

class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        # time.sleep(3)
        self.driver.maximize_window()
        # time.sleep(3)
        self.driver.get("http://xmwa1709117.php.hzxmnet.com/Admin/Index/index.html")

    def test_denglu(self):
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("admin")
        time.sleep(3)
        self.driver.get_screenshot_as_file('../photograph/username.jpg')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("admin12345")
        time.sleep(3)
        self.driver.get_screenshot_as_file('../photograph/userpassword.jpg')
        self.driver.find_element_by_xpath('//*[@id="remember"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="LoginForm"]/div[4]/div/input[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('/html/body/header/div/div/nav[1]/ul/li[2]/a').click()
        time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="menu-article"]/dt').click()
        # time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="menu-article"]/dd/ul/li/a').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()