#from pages.loopMenu.loop_menu_page import loopMenuPage
from pages.loopMenu2.loop_menu2_page import loopMenuPage2
from utilities.teststatus import Status
import unittest
import pytest
from locators.locators import Locators
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoopMenuTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.menus = loopMenuPage2(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_menu(self):
        self.menus.loopMenus()
        result1= self.menus.verifyBreadcrumbExists()
        self.ts.markFinal("test_menu", result1, "breadcrumb is visible")
