from pages.test_003_bli_kund_page.test_003_bli_kund_page import bliKundPage
from utilities.teststatus import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class BliKundTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.blikund = bliKundPage(self.driver)
        self.ts = Status(self.driver)

    #@pytest.mark.run(order=1)
    def test_menu(self):
        self.blikund.runTest()
        #result1 = self.blikund.verifyBreadcrumbExists()
        #self.ts.markFinal("test_menu", result1, "breadcrumb is visible")
