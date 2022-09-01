import time, allure

import pytest
from pom.home_page import HomePage
from pom.benefits_page import Benefits_center
from pom.wheel_page import Wheel_activity


@allure.epic('测试福利中心'.center(30, '*'))
@allure.feature('测试模块-福利中心模块')
@allure.suite('测试套件-福利中心')
class TestSigning():

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

        # HomePage().driver.back()  #返回一次

    # 进行抽奖
    @allure.story('app福利中心转盘抽奖')
    @allure.title('用例标题：福利中心转盘抽奖')
    @allure.description('测试步骤：app首页，进入福利中心，进入转盘，点击抽奖')
    @allure.testcase('D:\pythonProject1\screenshots')
    @allure.tag('抽奖成功')
    def test_go_rewad(self):
        hp = HomePage()
        hp.go_to_Benefits()
        time.sleep(3)
        sp = Benefits_center()
        sp.go_to_reward()
        time.sleep(3)
        wl = Wheel_activity()
        wl.click_lottery()
        time.sleep(10)
        lottery_success = wl.lottery_success_text()
        assert lottery_success == "知道了"
        wl.click_know()
        Benefits_center().driver.back()

    # 进行签到
    @allure.story('app福利中心签到')
    @allure.title('用例标题：福利中心签到')
    @allure.description('测试步骤：app首页，进入福利中心，点击签到')
    @allure.testcase('D:\pythonProject1\screenshots')
    @allure.tag('签到成功')
    def test_signin(self):
        hp = HomePage()
        hp.go_to_Benefits()
        time.sleep(3)
        sp = Benefits_center()
        sp.click_signin()
        login_success_txt = sp.sign_success_text()
        assert login_success_txt == "知道了"
        sp.click_sign_know()
        Benefits_center().driver.back()