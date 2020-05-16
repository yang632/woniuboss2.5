# -*- encoding: utf-8 -*-
# File    : service
# Author  : yang
# Email   : yang@163.com
# Software: PyCharm
# Time    : 2020/5/14 13:10
from tools.utility import Utility


class Service:
    @classmethod
    def send_input(cls, ele, value):
        ele.click()
        ele.clear()
        ele.send_keys(value)

    # 打开开始页面
    @classmethod
    def open_startpage(cls, driver, base_conf_path):
        pass

    # 打开页面
    @classmethod
    def openpage(cls, driver, menu_name):
        driver.find_element_by_partial_link_text(menu_name).click()

    # 判断某个元素是否存在
    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    # 截图操作
    @classmethod
    def get_png(cls, driver, path):
        import time
        time.sleep(2)
        driver.get_screenshot_as_file(path)

    # 出现缺陷或错误后的截图方法
    # '2020-03-23_15-17-30'
    @classmethod
    def get_error_png(cls, driver):
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        screenshot_path = '..\\screenshot\\fail%s.png' % (ctime)
        cls.get_png(driver, screenshot_path)

    # 打开页面
    @classmethod
    def openpage(cls, driver, menu_name):
        driver.find_element_by_partial_link_text(menu_name).click()

    # 下拉操作
    @classmethod
    def select_value(cls, ele, value):
        from selenium.webdriver.support.select import Select
        Select(ele).select_by_visible_text(value)

    # 忽略登录过程
    @classmethod
    def ignore_login(cls, driver):
        pass

