from distutils.archive_util import make_archive
from os import PRIO_PGRP, environ
from re import S, T
from threading import TIMEOUT_MAX
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import platform
from pytest import mark
import time
from pytest_html_reporter import attach
import sys
from pathlib import Path
sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from Settings.setup import quit
from dotenv import load_dotenv
load_dotenv()
import json


@mark.fixture_test()
def test_1_setupOS_Search():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_Search():
    login(driver)

@mark.fixture_test()
def test_3_aksesmenu_Search():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    time.sleep(0.1)
    driver.find_element(By.LINK_TEXT, 'Register H').click()
    print('.')
    print('========== akses menu Register H ==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_4_Kategori_nama_HalPer():  # Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterColumn').send_keys('nama')
    driver.find_element(By.ID, 'filterColumn').click()
    print('.')
    print('Memilih kategori nama')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_Search_Nama():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('')
    print('.')
    print(' Search Nama WBP')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_FilterStatus_Diizinkan():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="diizinkan"]')))
    driver.find_element(By.ID, 'diizinkan').click()
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    print('Filter status di izinkan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_7_Click_ButtonPerpanjangan_HalPer():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, '#perpanjangan0').click()
    print('.')
    print('Click Status Di izinkan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_8_InputNoSurat_HalamanTambah_HalPer():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#detailRegis')))

    driver.implicitly_wait(30)
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').send_keys('srt001/01')
    print('.')
    print('Input Nomor Surat')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_9_InputTanggalSurat_HalamanTambah_HalPer():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'tanggalSurat').send_keys('24/11/2022')
    driver.find_element(By.ID, 'tanggalSurat').send_keys(Keys.ENTER)
    print('.')
    print('Input tanggal Surat')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_10_InputLamaPerasingan_HalamanTambah_HalPer():
    driver.implicitly_wait(30)
    driver.find_element(By.XPATH,'//*[@id="lamaPengasingan"]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys('1')

    print('.')
    print('Input lama perpanjangan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_11_InputAlasan_HalamanTambah_HalPer():
    driver.implicitly_wait(30)
    driver.find_element(By.ID, 'alasan').send_keys('berantem')
    print('.')
    print('Input alasan')
    attach(data=driver.get_screenshot_as_png())

    print('.')
    print('Input alasan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_12_Submit_HalamanTambah():
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    print('.')
    print('Submit data perpanjangan')
    attach(data=driver.get_screenshot_as_png())

def teardown():
    quit(driver)