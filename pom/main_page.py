import time
from common.base_driver import BaseDriver


class MyPage(BaseDriver):

    def login_success_text(self):
        # t = self.driver.find_element_by_accessibility_id("我的消息").text
        # print(t)
        text = self.driver.find_element_by_accessibility_id('个人主页>')
        if text is not None:
            # print(text.get_attribute(name='content-desc') + '======1')  # 我的消息======1
            # print(text.get_attribute('name') + '======2')  # text中的内容======2
            # print(text.text + '======3')  # text中的内容======3
            # print('OK')
            success_text = text.get_attribute(name='content-desc')
        else:
            success_text = ""
            # print('False')

        return success_text

        # assert success_text == "我的消息"

        # return self.driver.find_element_by_xpath('//android.widget.ImageView[]').text


if __name__ == '__main__':
    mp = MyPage()
    time.sleep(3)
    mp.login_success_text()