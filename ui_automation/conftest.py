import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# pytest的装饰器，多个测试用例共用
@pytest.fixture(scope="module")
def driver():
    # 启动浏览器
    driver = webdriver.Edge()
    # 窗口最大化
    driver.maximize_window()
    # 等待十秒
    driver.implicitly_wait(10)

    yield driver
    driver.quit()