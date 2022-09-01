from common.base_driver import BaseDriver


class ForumPage(BaseDriver):

    def click_community(self, community_name):
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="GTarcade Discussion Forum"]').click()