from appium import webdriver
from common.operator_file import operator_yaml
import os
import logging
import logging.config
from common.get_dir import *
log_config = os.path.join(LOGS_DIR,'log.config')
logging.config.fileConfig(log_config)
logging = logging.getLogger()
data = operator_yaml()
app_path =os.path.join( APP_DIR,data['app'])

def android_driver():

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['uuid'] = data['uuid']
    desired_caps['app'] = app_path
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivate'] = data['appActivate']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    desired_caps['newCommandTimeout'] = data['newCommandTimeout']

    url = 'http://'+data['host']+':'+data['port']+'/wd/hub'
    # print(url)
    driver = webdriver.Remote(url,desired_caps)
    driver.implicitly_wait(5)
    return driver
if __name__ == '__main__':
    print(app_path,type(app_path))
    logging.info('test')
    # andr oid_driver()