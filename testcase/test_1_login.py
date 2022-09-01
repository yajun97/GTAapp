import os, time, pytest, allure
from pom.login_page import LoginPage
from pom.home_page import HomePage
from pom.main_page import MyPage
from common.base_driver import BaseDriver


@allure.epic('登录模块'.center(30, '*'))
@allure.feature('测试模块-登录模块')
@allure.suite('测试套件-登录')
class TestLogin():

    @pytest.fixture(autouse=True)
    def before_runcase(self):
        print("用例执行前的操作")

        yield
        print("用例执行后")
        # 定义每个用例运行完成之后进行截图操作
        # 1. 设置截图目录
        screenshots = os.path.join(os.path.dirname(__file__), '../screenshots')
        # 2. 创建截图目录
        if not os.path.exists(screenshots):
            os.mkdir(screenshots)
        # 3. 截图文件名
        filename = time.strftime('%Y_%m_%d_%H_%M_%S')
        # 4. 设置文件路径
        filepath = os.path.join(screenshots, filename + '.png')
        print(filepath)
        # 截图操作
        LoginPage().driver.save_screenshot(filepath)
        LoginPage().driver.back()
        LoginPage().driver.back()

    @allure.story('app用户登录模块')
    @allure.title('用例标题：密码输入错误，验证登录失败')
    @allure.description('测试步骤：输入用户名、错误的密码，点击登录')
    @allure.testcase('D:\pythonProject1\screenshots')
    @allure.tag('登录失败')
    def test_login_failed(self):
        lp = LoginPage()
        lp.login_with_username("chenyu@uuzu.com", "11123456")
        print("使用用户名密码登录，错误的密码，登录失败")
        time.sleep(1)
        login_failed_text = lp.login_faild_txt()
        assert login_failed_text == "账号或密码错误"

    @allure.story('app用户登录模块')
    @allure.title('用例标题：输入正确的用户名和密码登录，验证登录成功')
    @allure.description('测试步骤：输入用户名、正确的的密码，点击登录')
    @allure.testcase('D:\pythonProject1\screenshots')
    @allure.tag('登录成功')
    def test_login_success(self):
        lp = LoginPage()
        lp.login_with_username("171113015@qq.com", "xiao123456")
        hp = HomePage()
        time.sleep(3)
        hp.go_to_my()
        mp = MyPage()
        time.sleep(1)
        login_success_txt = mp.login_success_text()
        assert login_success_txt == "个人主页>"