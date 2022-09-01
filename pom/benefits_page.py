from common.base_driver import BaseDriver


#福利中心页面
class Benefits_center(BaseDriver):

    def click_signin(self):
        windowsize = self.driver.get_window_rect()
        width = windowsize['width']
        height = windowsize['height']
        self.driver.swipe(start_x=1, start_y=height/2, end_x=1, end_y=1)
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="马上签到"]').click()

    def click_sign_know(self):
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="知道了"]').click() #关闭签到弹窗

    #签到断言文案获取
    def sign_success_text(self):
        text = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="知道了"]')

        if text is not None:
            sign_success_text = text.get_attribute(name='content-desc')
        else:
            sign_success_text = ""
        return sign_success_text

    def signed_text(self):
        text=self.driver.find_element_by_xpath('//android.view.View[@index="11" and @class="android.view.View"]')
        if text is not None:
            success_text = text.get_attribute(name='content-desc')
        else:
            success_text = ""
        return success_text

    def go_to_reward(self):
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="转盘活动"]').click()  #进入转盘