"""
定义基础类
"""
import time
from appium import webdriver


class BaseDriver:

    DRIVER = None

    def __init__(self):

        desired_caps = {
            'platformName': 'Android',  # 平台
            'automationName': "UiAutomator2",
            "diviceName": "127.0.0.1:62001",#127.0.0.1:60189
            'noReset': False,  # 不要重置手机状态
            'fullReset': False,  # 重置所有的状态和数据
            "appPackage": "com.gtarcade.osapp",  # 启动app的包名
            "appActivity": ".MainActivity"  # 启动页名
        }
        #当二次被初始化的时候，保证driver唯一
        if BaseDriver.DRIVER == None:
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
            print("=============")
            BaseDriver.DRIVER = self.driver
        # 保证同一个driver 都为一个driver
        self.driver = BaseDriver.DRIVER
        self.driver.implicitly_wait(3)
        # self.android_uiautomator = 'new UiSelector().'

    #自定义滑屏方法
    def swipe_by_custorm(self, dirction):
        windowsize = self.driver.get_window_rect()
        # print(windowsize)
        width = windowsize['width']
        height = windowsize['height']
        if dirction == 'left':
            # 从左往右滑动
            self.driver.swipe(start_x=1, start_y=height / 2, end_x=width - 1, end_y=height / 2)
        elif dirction == 'right':
            # 从右往左滑动
            self.driver.swipe(start_x=width - 1, start_y=height / 2, end_x=1, end_y=height / 2)
        elif dirction == 'up':
            # 从下往上滑动
            self.driver.swipe(start_x=1, start_y=height / 2, end_x=1, end_y=1)
        elif dirction == 'down':
            # 从上往下滑动
            self.driver.swipe(start_x=1, start_y=1, end_x=1, end_y=height / 2)
            self.driver.current_url


if __name__ == '__main__':
    driver = BaseDriver()
    time.sleep(2)
    # swip_by_left = driver.swipe_by_custorm("up")


