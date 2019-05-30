import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from time import sleep

class bliKundPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _bli_kund = "//li[contains(text(),'Bli kund')]"
    _section_premium_packages_block = "//div[@class='section premium-packages-block']//div[@class='promotion']/div"
    _section_expanded_promotion_container = \
        "//div[@class='section expanded-promotion-container']//app-linked-image[@class='item-image-set ng-star-inserted']"
    _visa_som_lista = "//div[@class='section expanded-promotion-container']//button"
    _section_films_section = "//div[@class='section films-section']//app-linked-image"
    _section_button = "//div[@class='section']//button[contains(text(),'Beställ bredband')]"
    _section_price = "//div[@class='section section-price']//div[@class='promotion']//app-promotion-info"
    _section_packages = "//div[@class='section packages-section']//div[@class='promotion']/div"

    def goToBliKund(self):
        self.elementClick(self._bli_kund, locatorType='xpath')

    def runTest(self):
        self.goToBliKund()

    def verifyPremiumPackageSection(self):
        pass

