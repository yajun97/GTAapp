from pom.benefits_page import Benefits_center


"""
转盘页面
"""
class Wheel_activity(Benefits_center):

    """
    抽奖
    """
    def click_lottery(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView[@index='12' and @class='android.widget.ImageView']").click()

    # 关闭弹窗
    def click_know(self):
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="知道了"]').click()

    #断言文案获取
    def lottery_success_text(self):

        text = self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="知道了"]')

        if text is not None:
            success_text = text.get_attribute(name='content-desc')
        else:
            success_text = ""
        return success_text