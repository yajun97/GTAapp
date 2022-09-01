import time
# from appium.webdriver.webdriver import WebDriver
from common.base_driver import BaseDriver


class LoginPage(BaseDriver):
    # def __int__(self, driver:WebDriver):
    #     # 保证页面是在登录页面上
    #     # 判断当前driver的状态
    #     current_activity = self.driver.current_activity
    #     if ".ui.activity.LoginActivity" in current_activity:
    #         pass
    #     else:
    #         pass
    #         # 打开登录页面
    #         self.__go_login_page()

    def login_with_username(self, username, password):

        self.driver.find_element_by_class_name("android.widget.EditText").click()
        dicts = {'0': 7, '1': 8, '2': 9, '3': 10, '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16,
                 'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36, 'i': 37, 'j': 38, 'k': 39,
                 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44, 'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49, 'v': 50,
                 'w': 51, 'x': 52, 'y': 53, 'z': 54,
                 ',': 55, '.': 56, '`': 68, '[': 71, ']': 72, '\\': 73, ';': 74, "'": 75,
                 '*': 17, '#': 18, '-': 69, '=': 70, '/': 76, '@': 77, '+': 81, '(': 162, ')': 163
                 }
        try:
            self.driver.find_element_by_xpath('//android.widget.EditText[@index="0"]/android.widget.Button[@index="0"]').click()
            self.driver.find_element_by_class_name("android.widget.EditText").click()
            print("清空账号输入框#######################################")
        except:
            print("输入框为空")

        # self.driver.f
        # self.driver.find_element_by_xpath('//android.widget.EditText[@index="1"]').clear()

        for i in username:
            for num in dicts:
                if i == num:
                    self.driver.press_keycode(dicts.get(f"{num}"))

        self.driver.find_element_by_accessibility_id("下一步").click()

        try:
            self.driver.find_element_by_xpath('//android.widget.EditText[@index="2"]/android.widget.Button[@index="1"]').click()
            self.driver.find_element_by_xpath('//android.widget.EditText[@index="2"]').click()
        except:
            print("密码框为空")

        for n in password:
            for num2 in dicts:
                if n == num2:
                    self.driver.press_keycode(dicts.get(f"{num2}"))
            # self.driver.find_element_by_class_name("android.widget.EditText").send_keys("2541615941@qq.com")

        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="登录"]').click()

    def __go_login_page(self):
        """
        导航到loginpage
        :return:
        """
        # 清空app的状态 如果已经登录，去掉登录状态
        self.driver.reset()
        # 打开登录页
        self.driver.start_activity(app_package='com.gtarcade.osapp', app_activity='.MainActivity')

    def forgot_password(self):
        pass

    def login_faild_txt(self):
        # pass
        ele = self.driver.find_element_by_xpath('//*[@class="android.widget.Toast"]')
        # self.driver
        print(ele.text)
        return ele.text


if __name__ == '__main__':
    l = LoginPage()
    l.login_with_username("2541615941@qq.com","123456")
    # login_faild_text = l.login_faild_txt()
    # assert login_faild_text == "用户名或密码错误"
    # hp = HomePage()
    # hp.go_to_my()
    # mp = MyPage()
    # success_txt = mp.success_text()
    #
    # assert success_txt == "我的消息"
