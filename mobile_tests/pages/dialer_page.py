import re
from appium.webdriver.common.appiumby import AppiumBy


class DialerPage:
    def __init__(self, driver):
        self.driver = driver

    def open_keypad(self):
        keypad = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='key pad')
        if keypad.is_displayed():
            keypad.click()

    def enter_number(self, number):
        digit_map = {
            "1": "1,", "2": "2,ABC", "3": "3,DEF",
            "4": "4,GHI", "5": "5,JKL", "6": "6,MNO",
            "7": "7,PQRS", "8": "8,TUV", "9": "9,WXYZ"
        }
        for digit in number:
            self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=digit_map[digit]).click()

    def get_entered_number(self):
        phone_number_field = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/digits')
        return re.sub(r'\D', '', phone_number_field.text)  # Elimina todos los caracteres no numéricos
