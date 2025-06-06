# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMySuite1():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_myTest1(self):
        self.driver.get("https://trytestingthis.netlify.app/index.html")
        self.driver.set_window_size(1160, 623)
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)").click()
        assert self.driver.switch_to.alert.text == "Press a button!"
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.ID, "uname").click()
        self.driver.find_element(By.ID, "uname").send_keys("John")
        self.driver.find_element(By.ID, "pwd").click()
        self.driver.find_element(By.ID, "pwd").send_keys("Smith")
        self.driver.find_element(By.NAME, "option2").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option']").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option']").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 2']").click()
        self.driver.find_element(By.ID, "favcolor").click()
        self.driver.find_element(By.ID, "day").click()
        self.driver.find_element(By.ID, "day").send_keys("2025-05-28")
        self.driver.find_element(By.ID, "favcolor").click()
        self.driver.find_element(By.ID, "favcolor").send_keys("#cf5ccf")
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").send_keys("1")
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").click()
        element = self.driver.find_element(By.ID, "quantity")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").send_keys("2")
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").send_keys("3")
        self.driver.find_element(By.ID, "quantity").click()
        element = self.driver.find_element(By.ID, "quantity")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "quantity").send_keys("4")
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").send_keys("5")
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.NAME, "message").click()
        self.driver.find_element(By.NAME, "message").send_keys("The cat was playing in the garden.\\nI am typing")
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "uname").click()
        self.driver.find_element(By.ID, "uname").click()
        element = self.driver.find_element(By.ID, "uname")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "uname").send_keys("test")
        self.driver.find_element(By.ID, "pwd").click()
        self.driver.find_element(By.ID, "pwd").click()
        element = self.driver.find_element(By.ID, "pwd")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        self.driver.find_element(By.ID, "pwd").send_keys("test")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".main").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "h2")
        assert len(elements) > 0

