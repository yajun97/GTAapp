from common.base_driver import BaseDriver


class Daily_Singin_Page(BaseDriver):

    def click_signin(self):
        windowsize = self.driver.get_window_rect()
        width = windowsize['width']
        height = windowsize['height']
        self.driver.swipe(start_x=1, start_y=height/2, end_x=1, end_y=1)
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="马上签到"]').click()


    # def daily_signin_txt(self):
    #     daily_signin_txt = self.driver.find_element_by_xpath('//android.view.View[@index="0"]/android.view.View[@index="1"]').text
    #     print(daily_signin_txt)
    #     return daily_signin_txt