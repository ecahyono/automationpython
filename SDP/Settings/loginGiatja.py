import platform
import time
from os import environ
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pytest_html_reporter import attach

def Op_Giatja(driver):
    driver.implicitly_wait(10)
    driver.find_element(By.ID, "login").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("op-GiatjaProduksi")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('========== Login ==========')
    
    attach(data=driver.get_screenshot_as_png())

