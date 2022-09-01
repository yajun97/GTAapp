"""
运行项目文件
"""
import os

import pytest

# 创建测试报告目录
allure_reports = os.path.join(os.path.dirname(os.path.abspath(__file__)),'allure_reports')
print(allure_reports)
if not os.path.exists(allure_reports):
    os.mkdir(allure_reports)

if __name__ == '__main__':
    print("q")
    pytest.main(['testcase','-s','-v',f'--alluredir={allure_reports}'])
    os.system("allure generate --clean allure_reports")

