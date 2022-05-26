# Areli Tirado
# In n Out Automation Framework
# 05/25/2022

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class InnoutAutomation(unittest.TestCase):
    CHROMEDRIVER = "/Users/arelitirado/Drivers/chromedriver"
    URL="https://www.in-n-out.com/"

    def setUp(self):
        self.driver = webdriver.Chrome(self.CHROMEDRIVER)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.driver.get(self.URL)

    def test_social_media_instagram_icon(self):
        self.driver.find_element(By.CLASS_NAME, 'icon-instagram').click()
        assert "In-n-out" or "Instagram" in self.driver.title
    
    def test_view_menu_button_functionality(self):
        self.driver.find_element(By.ID, 'view-menu').click()
        assert "Menu" in self.driver.find_element(By.ID, 'menu-nav').text
    
    def test_gift_card_in_navigation(self):
        assert "GIFT CARDS" in self.driver.find_element(By.CLASS_NAME, 'nav-sub-content').text

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()