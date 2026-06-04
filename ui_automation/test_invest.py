import pytest
from selenium.webdriver.common.by import By
import time

# 主业务的冒烟测试
class TestLoanSmoke:

    def test_login_and_apply_loan(self, driver):
        # 打开网页
        driver.get("http://121.43.169.97:8081/")

        # 点击跳转登录页面
        driver.find_element(by=By.CLASS_NAME, value='login').click()

        #等待
        time.sleep(3)

        # 账号已注册，已开户成功，直接登录
        # 登录
        driver.find_element(by=By.ID, value="keywords").send_keys("12399999999")
        driver.find_element(by=By.NAME, value="password").send_keys("A123123")

        #点击登录
        driver.find_element(by=By.CLASS_NAME, value="login-btn").click()

        #等待
        time.sleep(3)

        # 断言登录成功的手机号
        user_phone = driver.find_element(By.XPATH, "//*[text()='12399999999']").text
        assert "12399999999" == user_phone, f"登录后显示的账号 {user_phone} 与预期不一致"

        #等待
        time.sleep(3)

        # 点击品质理财——个人借款
        driver.find_element(by=By.XPATH, value='//*[contains(text(),"智能投顾	")]').click()
        time.sleep(2)

        # 点击投标
        driver.find_element(By.XPATH, '//a[contains(@class,"btn-blue") and text()="马上投标"]').click()

        # 输入金额，最低100，填100即可
        driver.find_element(By.ID, "money").send_keys("100")

        # 按按钮文本
        driver.find_element(By.XPATH, '//input[@value="确认投标"]').click()
        time.sleep(3)

        # 切入页面iframe
        driver.switch_to.frame(0)
        time.sleep(3)

        # 首选ID定位
        driver.find_element(By.XPATH,'//input[@value="马上投标"]').click()

        # 切出
        driver.switch_to.default_content()
        time.sleep(2)
        old_handle = driver.current_window_handle
        driver.switch_to.window(old_handle)
        # driver.back()
        time.sleep(2)

        # 点击操作已完成
        driver.find_element(By.CLASS_NAME, "closeWinow").click()

        # 等待列表加载
        time.sleep(2)

        driver.find_element(By.XPATH, '//span[text()="投资记录"]/parent::li').click()

        # 查找包含“成功”的元素，获取文本做断言
        success_text = driver.find_element(By.XPATH,'//td[contains(text(),"成功")]').text
        assert "成功" in success_text, "投标未成功，页面无成功字样"
