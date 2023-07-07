from selenium.common.exceptions import NoSuchElementException
from common.get_driver import android_driver
from selenium.webdriver.common.by import By

driver = android_driver()
def check_agree_into_app():

    driver.find_element(By.ID,'com.ccbhome.lanhai:id/btn_sure')

