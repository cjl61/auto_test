from common.get_driver import android_driver
import logging
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.driver_base import DriverBase


driver = DriverBase(android_driver())

def check_agree_btn():
    try:
        agree_btn = driver.find_element(By.ID,'com.ccbhome.lanhai:id/btn_sure')
    except NoSuchElementException:
        pass
    else:
        agree_btn.click()
def check_agree_send_msg():
    try:
        agree_send_msg_no = driver.find_element(By.ID,'com.android.permissioncontroller:id/permission_deny_button')
        # com.android.permissioncontroller: id / permission_allow_button  允许
    except NoSuchElementException:
        pass
    else:
        agree_send_msg_no.click()
def check_swipe_page():
    try:
        agree_send_msg_no = driver.find_element(By.ID,'com.ccbhome.lanhai:id/guide_view_pager')
    except NoSuchElementException:
        pass
    else:
        driver.swipe()

