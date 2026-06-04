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
        driver.find_element(by=By.ID, value="keywords").send_keys("12388888888")
        driver.find_element(by=By.NAME, value="password").send_keys("A123123")

        #点击登录
        driver.find_element(by=By.CLASS_NAME, value="login-btn").click()

        #等待
        time.sleep(3)

        # 断言登录成功的手机号
        user_phone = driver.find_element(By.XPATH, "//*[text()='12388888888']").text
        assert "12388888888" == user_phone, f"登录后显示的账号 {user_phone} 与预期不一致"

        #等待
        time.sleep(3)

        # 点击品质理财——个人借款
        driver.find_element(by=By.XPATH, value='//*[contains(text(),"品质理财")]').click()
        # driver.find_element(by=By.XPATH, value='//*[contains(text(),"个人借款")]').click()

        #等待
        time.sleep(3)

        # 额度已申请，额度审核已通过，直接借款，假设借信用标
        driver.find_element(By.LINK_TEXT, "立即借款").click()

        # 进入借款页面，若额度不够则点击申请额度
        # driver.find_element(By.LINK_TEXT, "【申请额度】").click()

        # 额度够则填写借款信息
        # 选择个人借款
        driver.find_element(by=By.NAME, value="005").click()

        # 填写借款标题
        driver.find_element(by=By.NAME, value="name").send_keys("借款人一号借款30000元买房")

        # 选择借款用途，下拉列表选择
        driver.find_element(by=By.NAME, value='use').click()
        driver.find_element(by=By.XPATH, value='//select[@name="use"]/option[@value="1"]').click()

        # 填写借款金额amount
        driver.find_element(by=By.NAME, value="amount").send_keys("30000")

        # 填写年利率
        driver.find_element(by=By.NAME, value="apr").send_keys("5.00")

        # 选择借款期限单位
        driver.find_element(by=By.XPATH, value='//input[@name="period_type" and @value="month"]').click()

        # 选择还款方式repay_type,下拉列表
        driver.find_element(by=By.NAME, value='repay_type').click()
        driver.find_element(by=By.XPATH, value='//select[@name="repay_type"]/option[@value="1"]').click()

        # 选择借款期限period，下拉列表
        driver.find_element(by=By.NAME, value='period').click()
        driver.find_element(by=By.XPATH, value='//select[@name="period"]/option[@value="3"]').click()

        # 选择筹标期限validate
        driver.find_element(by=By.NAME, value='validate').click()
        driver.find_element(by=By.XPATH, value='//select[@name="validate"]/option[@value="3"]').click()

        # 选择最低投资金额tender_amount_min
        driver.find_element(by=By.NAME, value='tender_amount_min').click()
        driver.find_element(by=By.XPATH, value='//select[@name="tender_amount_min"]/option[@value="1"]').click()

        # 选择最高投资金额tender_amount_max
        driver.find_element(by=By.NAME, value='tender_amount_max').click()
        driver.find_element(by=By.XPATH, value='//select[@name="tender_amount_max"]/option[@value="2"]').click()

        # 填写借款投资密码，可写可不写

        # 填写借款描述borrow_contents
        driver.find_element(by=By.ID, value="borrow_contents").send_keys("借款人一号借款30000元买房")

        # 上传项目材料图片，如果有需要就上传
        # driver.find_element(by=By.XPATH, value='//input[@value="编辑"]').click()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value='//input[contains(@value,"提交")]')

        # 输入验证码
        driver.find_element(by=By.NAME, value='valicode').send_keys('8888')

        # 点击提交
        driver.find_element(by=By.ID, value='borrowForm').click()

        time.sleep(2)
        # 断言提交成功
        title_text = driver.find_element(By.XPATH, '//a[contains(text(),"借款人一号")]').text
        assert "借款人一号" in title_text

        money = driver.find_element(By.XPATH, '//td[contains(text(),"30,000.00")]').text
        assert money == "30,000.00"

        status = driver.find_element(By.XPATH, '//span[text()="发标待审"]').text
        assert status == "发标待审"