from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pytest_html_reporter import attach
import os, platform, time, pytest
from selenium import webdriver
from os import environ, path
from pathlib import Path
from pytest import mark
import platform
import logging
import sys
from openpyxl import load_workbook

from dotenv import load_dotenv
load_dotenv()

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR")) 
elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))

from Settings.setup import initDriver, loadDataPath
from Settings.login import login, oprupbasanbdg

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('indexp.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@mark.fixture_penempatan
def test_Ossetup():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')

@mark.fixture_penempatan
def test_loggin():
    # login(driver)
    oprupbasanbdg(driver)
    Log.info('Memasukan User name dan Password di halaman Login)')

@mark.fixture_penempatan
def test_akses_menu_penempatan():
    nav = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['menu']['Rupbasan'])
    ActionChains(driver).move_to_element(nav).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Penempatan').click()
    driver.find_element(By. ID, 'kataKunci').click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Menuju Menu penempatan dengan mengarahkan kursor ke navigasi ''Rubasan'' kemudian sub menu ''pemermpatan'')')

# @mark.fixture_penempatan
# def test_sortirdatatabel():
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#     ascending = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['ascenJRB'])
#     ascending.click()
#     WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#     descending = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['descenpatanbar'])
#     descending.click()
#     Log.info('setelah data tabel muncul kemudian melakukan sortir data tabel')

#     attach(data=driver.get_screenshot_as_png())
wb = load_workbook(environ.get("RUPEXEL"))
sheetrange1 = wb['Barangbasan']
j = 3

nama_barang   = sheetrange1['A'+str(j)].value #Nama Barang


@mark.fixture_penempatan
def test_pencariandatatabel():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    driver.find_element(By. ID, "filterColumn").click()
    time.sleep(2)
    driver.find_element(By. ID, "nama_barang").click()

    driver.find_element(By. ID, 'kataKunci').send_keys(nama_barang)

    driver.find_element(By. ID, 'searchButton').click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    attach(data=driver.get_screenshot_as_png())
    Log.info('melakukan pencarian data dengan memilih salah satu dari kategori yang disediakan')

@mark.fixture_penempatan
def test_hapuspencariandatatabel():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    filter = driver.find_element(By. ID, "filterColumn")
    ActionChains(driver).move_to_element(filter).perform()

    elemnthps = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['clearkategori'])
    ActionChains(driver).move_to_element(elemnthps).perform()
    elemnthps.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    attach(data=driver.get_screenshot_as_png())
    Log.info('menghapus field inputan dengan klik clear value button')

# @mark.fixture_penempatan
# def test_pilihhalaman():
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#     Halaman = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['pilihhalmn'])
#     Halaman.click()
#     halaman5 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['5halaman'])
#     halaman5.click()
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#     time.sleep(2)
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#     Halaman = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['pilihhalmn'])
#     Halaman.click()
#     halaman3 = driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['3halaman'])
#     halaman3.click()
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('pengecekan jumlah data perhalaman')

# @mark.fixture_penempatan
# def test_pilihpagetabel():
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
#     pergipage = driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke'])
#     pergipage.clear()
#     pergipage.send_keys('5')
#     pergipage.send_keys(Keys.ENTER)
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

#     attach(data=driver.get_screenshot_as_png())
#     Log.info('Menginputkan nomor halaman lebih dari jumlah halaman yang ada dan yang ditampilkan tetap halaman terakhir')
    
@mark.fixture_penempatan
def test_aksesmenu_detail():
    test_pencariandatatabel()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['aksesdetail']).click()
    time.sleep(2)
    driver.find_element(By.ID, 'backButton').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    attach(data=driver.get_screenshot_as_png())
    Log.info('Membuka halaman Detail dan kembali ke halaman sebelumnya dengan klik button kembali')

@mark.fixture_penempatan
def test_aksesmenu_ubah():
    test_pencariandatatabel()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['aksesubah']).click()
    time.sleep(2)
    driver.find_element(By.ID, 'backButton').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))

    Log.info('Membuka halaman Ubah dan kembali ke halaman sebelumnya dengan klik button kembali')

@mark.fixture_penempatan
def test_cetakBarcode():
    test_pencariandatatabel()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    time.sleep(2)
    driver.find_element(By. ID, 'cetakBarcode').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'cetakBarcode')))
    time.sleep(2)
    Log.info('mencetak barkode perbaris tabel kemudian muncul alert jika berhasil di download')

@mark.fixture_penempatan
def test_aksesmenu_tambah():
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'createButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'backButton').click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    time.sleep(5)
    Log.info('Membuka halaman Tambah dan kembali ke halaman sebelumnya dengan klik button kembali')

@mark.fixture_penempatan
def test_exportPDF():
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'pdfButton').click()
    driver.find_element(By.ID, 'wholeButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'pdfButton')))
    time.sleep(5)
    Log.info('Melakukan cetak PDF')

@mark.fixture_penempatan
def test_exportexcel():
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'excelButton').click()
    driver.find_element(By.ID, 'wholeButton').click()
    time.sleep(2)
    driver.find_element(By.ID, 'thisButton').click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'excelButton')))
    time.sleep(5)
    Log.info('Melakukan cetak EXCEL')

@mark.fixture_penempatan
def test_printdatatable():
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'searchButton')))
    driver.find_element(By.ID, 'printButton').click()
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['printsemua']).click()
    time.sleep(2)
    driver.find_element(By.XPATH, pathData['AksesMenu']['Rupbasan']['elemen']['indexpenempatan']['printinisaja']).click()
    WebDriverWait(driver, 90).until(EC.element_to_be_clickable((By.ID, 'printButton')))
    time.sleep(5)
    Log.info('Melakukan cetak Print data Table')
