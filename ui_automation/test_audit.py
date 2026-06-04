import pytest
from selenium.webdriver.common.by import By
import time

# 主业务的冒烟测试
class TestLoanSmoke:

    def test_login_and_apply_loan(self, driver):
        # 打开网页
        driver.get("http://121.43.169.97:8082/")

        #等待
        time.sleep(3)

        # 账号已注册，已开户成功，直接登录
        # 登录
        driver.find_element(by=By.ID, value="username").send_keys("admin")
        driver.find_element(by=By.NAME, value="password").send_keys("HM_2023_test")
        driver.find_element(by=By.ID, value="valicode").send_keys("8888")

        #点击登录
        driver.find_element(by=By.CLASS_NAME, value="login-button").click()

        #等待
        time.sleep(3)

        # 断言登录成功的用户名
        user_name = driver.find_element(By.XPATH, "//*[text()='admin']").text
        assert "admin" == user_name, f"登录后显示的账号 {user_name} 与预期不一致"

        #等待
        time.sleep(3)

        # 点击初审管理 → 初审标
        driver.find_element(By.XPATH, '//span[contains(text(),"初审管理")]').click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value='//a[@rel="loan/verify/list"]').click()
        time.sleep(2)

        # 切入iframe
        driver.get("http://121.43.169.97:8082/loan/verify/list")
        # iframe = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "iframe_box")))
        # driver.switch_to.frame(iframe)
        time.sleep(2)

        # 选择审核数据
        driver.find_element(By.XPATH, '//tbody/tr[1]').click()
        time.sleep(1)

        # 点击审核
        driver.find_element(By.XPATH, '//a[normalize-space()="审核"]').click()
        time.sleep(2)

        # 切换到内嵌框架
        driver.switch_to.frame(0)
        time.sleep(1)

        # 选择通过
        driver.find_element(By.XPATH, '//span[text()="通过"]/preceding-sibling::input').click()

        # 输入标签
        driver.find_element(By.XPATH, '//input[@name="marker_type"]').send_keys("测试标签")

        # 输入审核备注
        driver.find_element(By.XPATH, '//textarea').send_keys("审核通过，准许上架募资")

        # 输入验证码
        driver.find_element(By.XPATH, '/html/body/div[2]/form/table/tbody/tr[6]/td[2]/div/ul/li[1]/input').send_keys("8888")

        # 点击保存
        driver.find_element(By.XPATH, '//input[@value="保存"]').click()

        # 切出
        driver.switch_to.default_content()

