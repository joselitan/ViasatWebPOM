from pages.loopMenu.loop_menu_page import loopMenuPage
from utilities.teststatus import Status
import unittest
import pytest
from locators.locators import Locators
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoopMenuTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.menus = loopMenuPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_menu(self):
        a = self.menus.loopMenus()
        print(a)
