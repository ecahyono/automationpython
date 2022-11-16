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
import pyautogui
import sys
from pathlib import Path
#file module
#from module.setup import initDriver, loadDataPath
#from module.login import login

sys.path.append("/Users/will/Documents/work/Automationpython")
from Settings.setup import initDriver, loadDataPath
from Settings.login import login
from dotenv import load_dotenv
load_dotenv()
import json

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

@mark.fixture_test()
def test_2_login_HalamanEdit():
    login(driver)


#AKSES MENU 
@mark.fixture_test()
def test_3_akses_menu_HalamanEdit():
    
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())

# MENAKAN BUTTON UBAH

@mark.fixture_test()
def test_4_sortir_table_cari_nama_cari_identitas():
    driver.implicitly_wait(60)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    time.sleep(0.1)
    print('.')
    print('================================================================================= Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('Wildan Cahyono')
    print('.')
    print('================================================================================= Input Nama  ')

    driver.implicitly_wait(60)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    print('==========Click Button Cari  ==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_5_Click_ButtonUbah_HalamanEdit():
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    time.sleep(5)
    
    print('.')
    print('=================================================================================Click Button Update Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_6_sortir_detil_wbp_HalamanEdit():
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-0"]')))
    WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-0"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-0"]').click()
    driver.find_element(By.XPATH, '//*[@id="tab-1"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-2"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-3"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-4"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-5"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-6"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-7"]').click()

    print('=')
    print(' = Detile WBP')

@mark.fixture_test()
def test_7_detile_perkara_HalamanEdit():

    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tab-registrasi"]')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-registrasi"]')))
    driver.execute_script("window.scrollTo(0,1462.5)")
    driver.find_element(By.XPATH, '//*[@id="tab-registrasi"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-sidang"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-tahanan_rumah"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-meninggal_dunia"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-mutasi_upt"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-pm"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//*[@id="tab-pembebasan"]').click()
    print('=')
    print(' = Detile Perkara')
#MEMUAT ULANG HALAMAN WEB
@mark.fixture_test()
def test_8_Muat_Ulang_HalamanEdit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonReset"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonReset"]').click()
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]').click() 
    time.sleep(10)
    print('.')
    print('=================================================================================Click Button Muat Ulang Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 



@mark.fixture_test()
def test_9_Ubah_NoSk_HalamanEdit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="noSK"]')))
    driver.find_element(By.XPATH, '//*[@id="noSK"]').clear()
    driver.find_element(By.XPATH, '//*[@id="noSK"]').send_keys('SK/001/DIV')
    print('.')
    print('=================================================================================Ubah Deskripsi Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 

@mark.fixture_test()
def test_10_UploadSurat_HalamanEdit():
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="fileSK"]/div[1]/button').click()
    time.sleep(3)
    pyautogui.write(r"///////users/will/Downloads/pdf/rere.pdf")
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.write(r"///////users/will/Downloads/pdf/rere.pdf")
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.hotkey("backspace")
    pyautogui.write(r"///////users/will/Downloads/pdf/rere.pdf")
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
#MENEGEDIT DESKRIPSI
@mark.fixture_test()
def test_11_Ubah_Deskripsi_HalamanEdit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="deskripsi"]')))
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').clear()
    driver.find_element(By.XPATH, '//*[@id="deskripsi"]').send_keys('deskripsi baru')
    print('.')
    print('=================================================================================Ubah Deskripsi Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 


@mark.fixture_test()
def test_12_Input_JenisKeluar_HalamanTambah():
    driver.implicitly_wait(60)
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').send_keys("Diversi")
    driver.find_element(By.XPATH, '//*[@id="Diversi"]').click()
    print('=')
    print(' = Input Jenis Keluar  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()

#MENGEDIT TANGGAL KELUAR
def test_13_Ubah_Tanggal_Keluar_Edit():
    driver.implicitly_wait(10)
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID, "keluarKeamanan")))
    driver.find_element(By.ID, "keluarKeamanan").clear()
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys('24/12/2028')
    driver.find_element(By.ID, "keluarKeamanan").send_keys(Keys.ENTER)
    print('.')
    print('=================================================================================Ubah Tanggal Keluar Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 


#MENGEDIT TANGGAL KEMBALI
@mark.fixture_test()
def test_14_Ubah_Tanggal_kembali_Edit():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').clear()
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys('29/12/2028 12:80:80')
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('.')
    print('=================================================================================Ubah Tanggal Kembali Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png()) 
    time.sleep(10)


@mark.fixture_test()
def test_15_Ubah_Tanggal_kembali_Edit():
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusPendaftaran"]')))
    driver.find_element(By.XPATH, '//*[@id="statusPendaftaran"]').send_keys("Diizinkan")
    driver.find_element(By.XPATH, "//li[contains(.,\'Diizinkan\')]").click()
    print('=')
    print(' = Input Jenis Keluar  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_16_ButtonUbah_HalamanEdit():
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSubmit"]').click()
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    


#CLOSE 
def teardown():
    time.sleep(10)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')

    print('░░▄███▄███▄')
    print('░░█████████')
    print('░░▒▀█████▀░')
    print('░░▒░░▀█▀')
    print('░░▒░░█░')
    print('░░▒░█')
    print('░░░█')
    print('░░█░░░░███████')
    print('░██░░░██▓▓███▓██▒')
    print('██░░░█▓▓▓▓▓▓▓█▓████')
    print('██░░██▓▓▓(◐)▓█▓█▓█')
    print('███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█')
    print('▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█')
    print('░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█')
    print('░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█')
    print('░▒░░▒░░░█▓▓▓█░░░█▓▓▓█')
    print('░▒░░▒░░██▓██░░░██▓▓██')
    driver.close()
    driver.quit()