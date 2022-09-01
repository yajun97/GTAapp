import time

import pytest
import os,sys,subprocess
from appium import webdriver


@pytest.fixture(scope="session",autouse=True)
def session():
    print("在所有的测试用例执行之前，启动ppium服务")
    #启动appium服务
    start_appium(4723)

    yield #driver

    print("执行所有的用例执行之后的操作，关闭appium服务")
    time.sleep(10)
    # driver.quit()
    stop_appium(4723)


# @pytest.fixture(scope='function',autouse=True)
# def func():
#     print('每个函数执行之前，进入app首页')
#     yield
#     print('每个函数执行之后，截图')


def start_appium(port):
    """
    启动appium 服务
    :param port: 服务的端口号
    :return:
    """
    stop_appium(port)
    cmd = f"appium -p {port}"
    logsdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "appium_logs")
    if not os.path.exists(logsdir):
        os.mkdir(logsdir)

    subprocess.Popen(cmd,shell=True, stdout=open('./appium_logs/'+str(port)+".log",mode='a',encoding="utf8"),
                     stderr=subprocess.PIPE)


def stop_appium(port):
    """
    停止appium
    :param port: 启动的端口号
    :return:
    """
    mac_cmd = f"lsof -i tcp:{port}"
    win_cmd = f"netstat -ano | findstr {port}"
    # 判断操作系统
    os_platform = sys.platform
    if os_platform == "win32":  #windows 系统
        win_p = subprocess.Popen(win_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        for line in win_p.stdout.readlines():
            if line:
                line = line.decode('utf8')
                if "LISTENING" in line:
                    win_pid = line.split("LISTENING")[1].strip()
                    os.system(f"taskkill -f -pid {win_pid}")
    else:                        # unix系统
        p = subprocess.Popen(mac_cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        for line in p.stdout.readlines():
            line = line.decode('utf8')
            # print("line",line)
            if "node" in line:
                stdoutline = line.split(" ")
                print(stdoutline)
                pid = stdoutline[4]
                os.system(f"kill {pid}")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     # 获取用例的执行结果
#     rep = outcome.get_result()
#     # 将执行结果保存到 item 属性中  req.when 执行时
#     setattr(item, "rep_" + rep.when, rep)
#
#
# @pytest.fixture(scope='function',autouse=True)
# def case_run(driver:webdriver,request):
#     """
#     每个测试用例执行完成之后，如果执行失败截图，截图的名称为测试用例名称+时间格式
#     :param request:
#     :return:
#     """
#     yield
#     if request.node.rep_call.failed:
#         import os,time
#         screenshots = os.path.join(os.path.dirname(os.path.abspath(__file__)),'screeshots')
#         if not os.path.exists(screenshots):
#             os.mkdir(screenshots)
#         casename:str = request.node.nodeid
#         print("执行测试用例的名字：",casename)
#         # 测试用例的名字
#         # casename = casename.replace('.py::','_')
#         filename = time.strftime('%Y_%m_%d_%H_%M_%S')+".png"
#         screenshot_file = os.path.join(screenshots,filename)
#         # 保存截图
#         driver.save_screenshot(screenshot_file)


if __name__ == '__main__':
    # start_appium(4723)
    stop_appium(4723)