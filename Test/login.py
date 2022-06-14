from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from POM.Pages.pagel import Log

class app(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.google.com")
        pag = Log(driver)
        pag.entersearch("hi")
        pag.clicksearch()

    @classmethod
    def tearDown(self):
        self.driver.quit()




