# coding=utf-8
import requests
import unittest


class SendSms(unittest.TestCase):
    def setUp(self):
        print('Start Test')
        pass

    def tearDown(self):
        print('Test End')
        pass


class test_supplier(SendSms):
    """供应商登陆发送短信"""

    def test_supplier1(self):
        """正确手机号码"""
        self.url = 'http://supplier.app.interface.test.youmidou.cn/supplier/login/remote/sendCode'
        self.data = {
            'mobile' : 17628090406
        }
        result = requests.post(url=self.url , data=self.data)
        print(result.text)
        self.assertIn("发送成功", result.text)

    def test_supplier2(self):
        """手机号码为空"""
        self.url = "http://supplier.app.interface.test.youmidou.cn/supplier/login/remote/sendCode"
        self.data = {
            'mobile' : None
        }

        result = requests.post(url=self.url , data=self.data)
        print(result.text)
        self.assertIn("发送成功", result.text)

if __name__ == "__main__":
    unittest.main()