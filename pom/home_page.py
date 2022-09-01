import time

from common.base_driver import BaseDriver
# from pom.basepage import Basepage


class HomePage(BaseDriver):
    def __int__(self):
        try:
            text = self.driver.find_element_by_xpath("//android.view.View[@index='1' and @class='android.view.View' and @content-desc='热门新闻']")
            print("当前位置在首页")
        except:
            print("前往首页")
        # 保证页面是在首页
        # 判断当前driver的状态
        # current_activity = self.driver.current_activity
        # print("+++++++++++++++++++++++++++!!",current_activity)
        # if ".ui.activity.LoginActivity" in current_activity:
        #     pass
        # else:
        #     pass
        #     # 打开登录页面
        #     self.__go_home_page()

    def go_to_Benefits(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("福利中心")').click()

    def go_to_points_shop(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("礼包中心")').click()

    def go_to_task_center(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("任务中心")').click()

    def go_to_event_center(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("活动中心")').click()

    def go_to_home(self):
        self.driver.find_element_by_xpath(
            "(//android.widget.ImageView[@index='0' and @class='android.widget.ImageView'])[6]").click()  # 主页

    def go_to_game(self):
        self.driver.find_element_by_xpath(
            "(//android.widget.ImageView[@index='1' and @class='android.widget.ImageView'])[5]").click()  # 游戏

    def go_to_forum(self):
        self.driver.find_element_by_xpath(
            "(//android.widget.ImageView[@index='2' and @class='android.widget.ImageView'])[4]").click()  # 论坛

    def go_to_my(self):
        self.driver.find_element_by_xpath(
            "(//android.widget.ImageView[@index='3' and @class='android.widget.ImageView'])[2]").click()  # 我的

    def go_to_search(self):
        self.driver.find_element_by_xpath(
            "(//android.widget.ImageView[@index='0' and @class='android.widget.ImageView'])[1]").click()  # 搜索

    def go_to_message(self):
        self.driver.find_element_by_xpath(
            "(//android.widget.ImageView[@index='2' and @class='android.widget.ImageView'])[1]").click()  # 消息

    def go_to_news1(self):
        self.driver.find_element_by_xpath("//android.view.View[@index='6' and @class='android.view.View']").click()  # 进入新闻第一个帖子

    def shut_down_verify(self):
        self.driver.find_element_by_xpath("(//android.widget.ImageView[@index='4' and @class='android.widget.ImageView'])[2]").click()#关闭验证弹窗



if __name__ == '__main__':
    hp = HomePage().__int__()
    time.sleep(5)
    # hp.go_to_daily_signin()
    # day_sin_pag = Daily_Singin_Page()
    # singin_txt = day_sin_pag.daily_signin_txt()
    # assert singin_txt == "每日签到"
    # hp.go_to_my()