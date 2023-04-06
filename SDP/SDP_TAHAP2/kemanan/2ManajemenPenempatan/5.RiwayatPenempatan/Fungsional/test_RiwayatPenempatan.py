from distutils.archive_util import make_archive
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
import platform
from pytest import mark
import time
from pytest_html_reporter import attach
import pyautogui

import sys
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))
    wb = load_workbook(environ.get("KeamananUAT"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.loginkeamanan import loginOperatorSumedang, Op_Keamanan_p2u, SpvRutanBdg, op_keamanan_mp
from Settings.Page.keamanan import manajemenpenghunibaru
from Settings.Page.keamanan import riwayatpenempatan

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('LogSuratMutasi.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

i = 2
Verifikasi = wb['ManajemenKamar']

Nama                                    = Verifikasi['A'+str(i)].value
NoSurat                                 = Verifikasi['H'+str(i)].value


@mark.fixture_test()
def test_1_loginSPV():

    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')
    SpvRutanBdg(driver)
    Log.info('Login Spv Manajemen Penempatan')


@mark.fixture_test()
def test_2_AksesMenu():
    sleep(driver)
    riwayatpenempatan(driver)
    print('.')
    Log.info('Akses halaman Manajemen Penghuni Baru')
    attach(data=driver.get_screenshot_as_png())
    Log.info('Akses Menu Riwayat Penempatan Kamar')


@mark.fixture_test()
def test_3_SearchSemua():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    Log.info("Click Search Button")
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "semua").click()
    driver.find_element(By.ID, "kataKunci").click()
    driver.find_element(By.ID, "kataKunci").send_keys("KADIR")
    driver.find_element(By.ID, "searchButton").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, "#detailButton0 .h-5").click()
    sleep(driver)
    driver.find_element(By.ID, "backButton").click()
    Log.info('Cek Filter Data Berdasarkan semua')

@mark.fixture_test()
def test_4_SearchNoreg():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "nmr_reg_gol").click()
    driver.find_element(By.ID, "kataKunci").click()
    driver.find_element(By.ID, "kataKunci").send_keys("1")
    driver.find_element(By.ID, "searchButton").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, "#detailButton0 .h-5").click()
    sleep(driver)
    driver.find_element(By.ID, "backButton").click()
    Log.info('Cek Filter Data Berdasarkan Nomor Registrasi')

@mark.fixture_test()
def test_5_SearchNamaLengkap():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "nama_lengkap").click()
    driver.find_element(By.ID, "kataKunci").click()
    driver.find_element(By.ID, "kataKunci").send_keys("kadir")
    driver.find_element(By.ID, "searchButton").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.CSS_SELECTOR, "#detailButton0 .h-5").click()
    sleep(driver)
    driver.find_element(By.ID, "backButton").click()
    Log.info('Cek Filter Data Berdasarkan Nama Lengkap')
    
@mark.fixture_test()
def test_6_SearchPidana():
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.ID, "pidana").click()
    driver.find_element(By.ID, "kataKunci").click()
    driver.find_element(By.ID, "kataKunci").send_keys("kesusilaan")
    driver.find_element(By.ID, "searchButton").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    driver.find_element(By.CSS_SELECTOR, "#detailButton0 .h-5").click()
    sleep(driver)
    driver.find_element(By.ID, "backButton").click()
    Log.info('Cek Filter Data Berdasarkan Pidana')

@mark.fixture_test()
def test_7_exit():
    quit(driver)













