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

class Test9():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test8(self):
    # Get
    self.driver.get("https://sandbox.moodledemo.net/")
    self.driver.implicitly_wait(10)
    self.driver.set_window_size(1520, 816)
    # Login and change language
    self.driver.find_element(By.CSS_SELECTOR, ".langbutton").click()
    # Some time, when i use moodle, it change to another version 
    # self.driver.find_element(By.CSS_SELECTOR, "ul.navbar-nav > li:last-child").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(103)").click()
    self.driver.find_element(By.LINK_TEXT, "Đăng nhập").click()
    self.driver.find_element(By.CSS_SELECTOR, ".login-wrapper").click()
    self.driver.find_element(By.ID, "username").send_keys("student")
    self.driver.find_element(By.ID, "password").send_keys("sandbox")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    
    # User Information
    self.driver.find_element(By.CSS_SELECTOR, ".userbutton").click()
    self.driver.find_element(By.LINK_TEXT, "Tập tin riêng tư").click()
    self.driver.implicitly_wait(10)
    
    
    # Click Upload
    self.driver.find_element(By.CSS_SELECTOR, ".fa-file-o").click()
    self.driver.find_element(By.LINK_TEXT, "Tải lên một tài liệu").click()
    
    element = self.driver.find_element(By.NAME, "repo_upload_file")
    element.send_keys("C:\\Users\\Admin\\Desktop\\Ftho-Py\\FakeData\\BigFile.mkv")
    
    
    self.driver.find_element(By.CSS_SELECTOR, ".fp-upload-btn.btn-primary.btn").click()
    self.driver.implicitly_wait(30)
    assert self.driver.find_element(By.CSS_SELECTOR, ".moodle-exception-message").text == "The maximum size you can upload is 100MB."
    time.sleep(100)
    
    
    
    
    # time.sleep(10)
  