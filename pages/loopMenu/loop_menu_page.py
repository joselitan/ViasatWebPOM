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
    _menu_path = "//ul/li[contains(text(),'{0}')]"
    _breadcrumb = "//app-breadcrumb//span[@class='last-element']"
    _breadcrumb2 ="//app-breadcrumb//span[contains(text(),'{0}')]"

    def getMenus(self):
        menu = [a.text for a in self.getElementList(self._menu_list, locatorType="xpath") if a.text not in '']
        #self.log.info(menu)
        #self.log.info(type(menu))
        return menu


    def clickMenus(self):

        for i in self.getMenus():
            # self.waitForElement(self._menu_path.format(i), locatorType="xpath", timeout=0.9)
            self.isElementDisplayed(self._menu_path.format(i), locatorType="xpath")
            self.elementClick(self._menu_path.format(i), locatorType="xpath")
            #self.log.info(self.getTitle())

    def listMenus(self):

        self.log.info(self.getMenus())

    def loopMenus(self):
        self.getMenus()
        self.listMenus()
        self.clickMenus()

    # def verifyBreadcrumbExists(self):
    #
    #     for i in self.getMenus():
    #         print("#####", i)
    #         result = self.isElementPresent(self._breadcrumb2.format(i),
    #                                             locatorType="xpath")
    #         print("#####", result)
    #         return result

    def verifyBreadcrumbExists(self):

        result = self.isElementPresent(self._breadcrumb2.format("Tv-guide"),
                                            locatorType="xpath")
        return result




