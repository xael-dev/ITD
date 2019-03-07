# from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).teardown()

    def test_register(self):
        selenium = self.selenium #shorthand for command execution

        #Open the link in our chosen browser(s)
        selenium.get('localhost:8000/')

        #Navbar elements
        selenium.find_element_by_css_selector("li.nav-item:nth-child(1) > a:nth-child(1)").click()
        selenium.find_element_by_css_selector("li.nav-item:nth-child(2) > a:nth-child(1)").click()
        selenium.find_element_by_css_selector("li.nav-item:nth-child(3) > a:nth-child(1)").click()
        selenium.find_element_by_css_selector("li.nav-item:nth-child(4) > a:nth-child(1)").click()
        selenium.find_element_by_css_selector(".navbar-brand").click()

