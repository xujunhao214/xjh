from selenium import webdriver
import time
import unittest
import HTMLTestRunner

class Login(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()

    def denglu(self,password,name):
        self.driver.get("https://www.cnblogs.com/")
        self.driver.find_element_by_xpath("//SPAN[@id='span_userinfo']/A[1]").click()
        time.sleep(5)
        self.driver.get_screenshot_as_file("../picture/denglu.jpg")
        self.driver.find_element_by_xpath("//INPUT[@id='input1']").send_keys(password)
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/name.jpg")
        self.driver.find_element_by_xpath("//INPUT[@id='input2']").send_keys(name)
        time.sleep(3)
        self.driver.get_screenshot_as_file("../picture/password.jpg")
        self.driver.find_element_by_xpath("//INPUT[@id='signin']").click()

    def test_register_user_null(self):
        self.denglu("","xjh1996@")
        time.sleep(3)
        error_message=self.driver.find_element_by_xpath('//*[@id="tip_input1"]').text
        self.assertEqual(error_message,"请输入登录用户名")
        self.driver.get_screenshot_as_file("../picture/test_register_user_null.jpg")

    def test_register_pwd_null(self):
        self.denglu("xjh214","")
        time.sleep(3)
        error_message=self.driver.find_element_by_xpath('//*[@id="tip_input2"]').text
        self.assertEqual(error_message,"请输入密码")
        self.driver.get_screenshot_as_file("../picture/test_register_pwd_null.jpg")

    def test_register_user_error(self):
        self.denglu("xjh","xjh19960214@")
        time.sleep(3)
        error_message=self.driver.find_element_by_xpath('//*[@id="tip_btn"]').text
        self.assertEqual(error_message,"用户名或密码错误\n\n联系 contact@cnblogs.com")
        self.driver.get_screenshot_as_file("../picture/test_register_user_error.jpg")

    def test_register_pwd_error(self):
        self.denglu("xjh214","xjh1996")
        time.sleep(3)
        error_message=self.driver.find_element_by_xpath('//*[@id="tip_btn"]').text
        self.assertEqual(error_message,"用户名或密码错误\n\n联系 contact@cnblogs.com")
        self.driver.get_screenshot_as_file("../picture/test_register_pwd_error.jpg")

    def test_register_suess(self):
        self.denglu("xjh214","xjh19960214@")
        time.sleep(3)
        suess_message=self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/ul/li[1]/a').text
        self.assertEqual(suess_message,"首页")
        self.driver.get_screenshot_as_file("../picture/test_register_suess.jpg")

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(Login("test_register_user_null"))
    suite.addTest(Login("test_register_pwd_null"))
    suite.addTest(Login("test_register_user_error"))
    suite.addTest(Login("test_register_pwd_error"))
    suite.addTest(Login("test_register_suess"))

    file_name='bokeyuan'+str(time.strftime('%Y%m%d%H%M%S'))+'.html'
    file_path='../test_report/'+file_name
    file_result=open(file_path,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=file_result,title=u'博客园登录测试报告结果：',description=u'用例执行情况：')
    runner.run(suite)
    file_result.close()