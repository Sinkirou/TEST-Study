"""
公共方法模块
"""
from selenium import webdriver
from time import sleep


def get_alert_msg():
    """获取弹窗信息方法"""
    sleep(2)
    # msg = self.driver.find_element_by_class_name('layui-layer-content').text
    # msg = driver.find_element_by_class_name('layui-layer-content').text
    msg = DriverUtil.get_driver().find_element_by_class_name('layui-layer-content').text
    return msg


class DriverUtil(object):
    """浏览器对象管理类"""
    __driver = None  # 浏览器对象变量初始化状态

    @classmethod
    def get_driver(cls):
        """获取浏览器对象方法"""
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome()  # 浏览器类型
            cls.__driver.get('http://127.0.0.1/')  # 项目地址
            cls.__driver.maximize_window()  # 窗口最大化
            cls.__driver.implicitly_wait(10)  # 隐式等待
        return cls.__driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器对象方法"""
        if cls.__driver:
            sleep(3)
            cls.__driver.quit()
            cls.__driver = None


if __name__ == '__main__':
    DriverUtil.get_driver()  # 获取浏览器对象
    sleep(2)
    DriverUtil.quit_driver()  # 退出浏览器对象
