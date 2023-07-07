
class DriverBase():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def swipe(self,start_x,start_y,end_x,end_y,duration=1000):
        self.driver.swipe(self, start_x, start_y, end_x, end_y, duration=1000)
