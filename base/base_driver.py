import os,sys
sys.path.append(os.getcwd())
from appium import webdriver

def init_driver():
    # server启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = '127.0.0.1:62025'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = 'Settings bnds'
    # 支持中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver

if __name__ == '__main__':
    init_driver()
