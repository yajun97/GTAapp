import time, allure

import pytest
from pom.home_pagebf import HomePage
from pom.daily_signin_page import Daily_Singin_Page
from common.base_driver import BaseDriver


@allure.epic('测试签到'.center(30, '*'))
@allure.feature('测试模块-签到模块')
@allure.suite('测试套件-签到')
class TestSignin():

    @pytest.fixture(autouse=True)
    def before_runcase(self):
        print("用例执行前，app回到首页")
        try:
            text = HomePage().driver.find_element_by_xpath("//android.view.View[@index='1' and @class='android.view.View' and @content-desc='热门新闻']")
            print("当前位置在首页")
        except:
            print("前往首页")
            HomePage().driver.start_activity(app_package="com.gtarcade.osapp",
                                   app_activity='.MainActivity')
            time.sleep(3)
            # HomePage().driver.find_element_by_xpath('//android.widget.ImageView[@index="0"]').click()

        yield
        print("用例执行后")

    @allure.story('app福利中心签到')
    @allure.title('用例标题：福利中心签到')
    @allure.description('测试步骤：app首页，进入福利中心，点击签到')
    @allure.testcase('D:\pythonProject1\screenshots')
    @allure.tag('签到成功')
    def test_signin(self):
        hp = HomePage()
        hp.go_to_daily_signin()
        time.sleep(3)
        sp = Daily_Singin_Page()
        sp.click_signin()