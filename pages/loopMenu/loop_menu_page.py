import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from time import sleep

class loopMenuPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _menu_list = "//ul[@class='main-menu ng-star-inserted']/li" #xpath

    def getMenus(self):
        return self.getElementList(self._menu_list, locatorType="xpath")




    def loopMenus(self):
        # self.getMenus()



