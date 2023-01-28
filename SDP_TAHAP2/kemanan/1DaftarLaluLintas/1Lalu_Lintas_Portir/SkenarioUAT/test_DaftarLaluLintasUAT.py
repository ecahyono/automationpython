from distutils.archive_util import make_archive
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
from os import environ, path
from dotenv import load_dotenv
load_dotenv()
from openpyxl import load_workbook

if platform.system() == 'Darwin':
    sys.path.append(environ.get("MACPARENTDIR"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import login, loginOperator

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('DaftarLaluLintasUAT.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

wb = load_workbook(environ.get("KeamananUAT"))
sheetrange = wb['DaftarLaluLintas_Index']
print('.')
print('Mau Baris Ke Berapa ?')
index  = input('')

filterColumnindex                          = sheetrange['B'+str(index)].value
namaLengkapindex                           = sheetrange['C'+str(index)].value
nomorIndukindex                            = sheetrange['D'+str(index)].value





@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    loginOperator(driver)
    Log.info('Login')


@mark.fixture_test()
def test_DLP_001():
    print('.')
    print('== NEXT == (DLP-001) - Akses halaman Daftar Lalu Lintas ')

    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Akses P2U Internal').click()
    sleep(driver)
    print('.')
    Log.info('(DLP-001 SUKSES) Akses halaman Daftar Lalu Lintas - Mengakses halaman Daftar Lalu Lintas dengan memilih modul Keamanan kemudian pilih menu Lalu Lintas lalu pilih submenu Daftar Lalu Lintas')
    attach(data=driver.get_screenshot_as_png())


                                ########## HALAMAN CARI IDENTITAS WBP ##########

sheetrangeCariIdentitas = wb['DaftarLaluLintas_CariIdentitas']
print('.')
print('Masuk Ke halaman Cari,Mau Baris Ke Berapa ?')
cari  = input('')

filterColumncari                          = sheetrangeCariIdentitas['B'+str(cari)].value
nomorRegcari                              = sheetrangeCariIdentitas['C'+str(cari)].value
Namacari                                  = sheetrangeCariIdentitas['D'+str(cari)].value
jenisKejahatancari                        = sheetrangeCariIdentitas['E'+str(cari)].value

@mark.fixture_test()
def test_DLP_002():
    print('.')
    print('== NEXT ==  DLP-002 / Pencarian data identitas WBP')
    sleep(driver)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))


    print('== NEXT == Pilih Dropdown Nama')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    time.sleep(0.4)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    Log.info(' Memilih Dropdown Nama  ')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

    print('== NEXT == Input kata kunci nama')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Namacari)
    # driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('Wildan Cahyono')
    Log.info(' Input Nama  ')

    print('== NEXT == Klik Button Search')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    Log.info(' Click Button Cari  ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.CSS_SELECTOR, ".h-5 > path").click()
    print('.')
    Log.info(' Click Button Update  ')
    attach(data=driver.get_screenshot_as_png())

sheetrangeInput = wb['DaftarLaluLintas_Input']
print('.')
print('Halaman Input data, Mau Baris Ke Berapa ?')
Halinput = input('')

NamaInput                                  = sheetrangeInput['B'+str(Halinput)].value
JenisKeluarInput                           = sheetrangeInput['C'+str(Halinput)].value
TanggalKeluarInput                         = sheetrangeInput['D'+str(Halinput)].value
TanggalHarusKembaliInput                   = sheetrangeInput['E'+str(Halinput)].value
deskripsiInput                             = sheetrangeInput['F'+str(Halinput)].value
PengwalInternalInput                       = sheetrangeInput['G'+str(Halinput)].value
PengwalExternalInput                       = sheetrangeInput['H'+str(Halinput)].value

sheetrangeUbah = wb['DaftarLaluLintas_Edit']
print('.')
print('Halaman Ubah, Mau Baris Ke Berapa ?')
HalUbah = input('')

NamaEditUbah                                    = sheetrangeUbah['B'+str(HalUbah)].value
noSKUbah                                        = sheetrangeUbah['C'+str(HalUbah)].value
JenisKeluarEditUbah                             = sheetrangeUbah['D'+str(HalUbah)].value
TanggalKeluarEditUbah                           = sheetrangeUbah['E'+str(HalUbah)].value
TanggalHarusKembaliEditUbah                     = sheetrangeUbah['F'+str(HalUbah)].value
deskripsiEditUbah                               = sheetrangeUbah['G'+str(HalUbah)].value
PengwalInternalEditUbah                         = sheetrangeUbah['H'+str(HalUbah)].value
PengwalExternalEditUbah                         = sheetrangeUbah['I'+str(HalUbah)].value


                                        ########## MASUK KE HALAMAN TAMBAH ##########
@mark.fixture_test()
def test_DLP_003():
    print('.')
    print('== NEXT == DLP-003 / Pengecekan tampilan detail data identitas WBP')
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    print('.')
    Log.info(' Click Button Tambah WBP  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_004():
    print('.')
    print('== NEXT == DLP-004 / Pengecekan data yang telah dibuat')
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenisKeluar"]')))
    driver.find_element(By.XPATH, '//*[@id="jenisKeluar"]').click()

    if JenisKeluarInput == 'Asimilasi':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi\')]").click()
        print('.')
        Log.info(' Input Jenis Keluar Asimilasi  ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Pembebasan Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Pembebasan Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Pembebasan Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Pembebasan bersyarat ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Anak Kembali ke Orang Tua':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Anak Kembali ke Orang Tua')
        driver.find_element(By.XPATH, "//li[contains(.,\'Anak Kembali ke Orang Tua\')]").click()
        print('.')
        Log.info(' Input Jenis Anak Kembali ke Orang Tua ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Cuti Bersyarat':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Bersyarat')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Bersyarat\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Bersyarat ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarInput == 'Asimilasi di Rumah':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Asimilasi di Rumah')
        driver.find_element(By.XPATH, "//li[contains(.,\'Asimilasi di Rumah\')]").click()
        print('.')
        Log.info(' Input Jenis Asimilasi di Rumah ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarInput == 'Bebas Biasa':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Biasa')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Biasa\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Biasa ')
        attach(data=driver.get_screenshot_as_png())


    elif JenisKeluarInput == 'Bebas dari Dakwaan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas dari Dakwaan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas dari Dakwaan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas dari Dakwaan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Bebas Dari Tuntutan':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Bebas Dari Tuntutan')
        driver.find_element(By.XPATH, "//li[contains(.,\'Bebas Dari Tuntutan\')]").click()
        print('.')
        Log.info(' Input Jenis Bebas Dari Tuntutan ')
        attach(data=driver.get_screenshot_as_png())

    elif JenisKeluarInput == 'Cuti Menjelang Bebas':
        driver.find_element(By.ID, 'jenisKeluar').send_keys('Cuti Menjelang Bebas')
        driver.find_element(By.XPATH, "//li[contains(.,\'Cuti Menjelang Bebas\')]").click()
        print('.')
        Log.info(' Input Jenis Cuti Menjelang Bebas ')
        attach(data=driver.get_screenshot_as_png())
    
    driver.find_element(By.ID, 'noSK').click()
    driver.find_element(By.ID, 'noSK').clear()
    driver.find_element(By.ID, 'noSK').send_keys(noSKUbah)

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keluarKeamanan"]')))
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(TanggalKeluarInput)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').send_keys(Keys.ENTER)

    print('.')
    Log.info(' Input Tanggal Keluar  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    driver.execute_script("window.scrollTo(0,1462.5)")
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#deskripsi')))
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").click()
    driver.find_element(By.CSS_SELECTOR, "#deskripsi").send_keys(deskripsiInput)
    print('.')
    Log.info(' Input Deskripsi Behasil ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalKembali"]')))
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(TanggalHarusKembaliInput)
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').send_keys(Keys.ENTER)
    print('.')
    Log.info(' Input Tanggal Harus Kembali  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="addPengawal"]').click()
    print('.')
    Log.info(' Input tambah pengawal  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis0"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis0"]').click()
    driver.find_element(By.XPATH, "//li[@id='Internal0']").click()
    print('.')
    Log.info(' Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawalInternal0"]').send_keys(PengwalInternalInput)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="optionPengawal00"]')))
    driver.find_element(By.XPATH, '//*[@id="optionPengawal00"]').click()
    print('.')
    Log.info(' Input nama pengawal Internal  ')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="jenis1"]')))
    driver.find_element(By.XPATH, '//*[@id="jenis1"]').click()
    driver.find_element(By.CSS_SELECTOR, "#Eksternal1").click()
    print('.')
    Log.info(' Input tambah Jenis pengawal  ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').click
    driver.find_element(By.XPATH, '//*[@id="pengawal1"]').send_keys(PengwalExternalInput)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//td[contains(.,'operator')]")))
    time.sleep(0.4)
    driver.find_element(By.XPATH, "//td[contains(.,'operator')]").click()
    print('.')
    Log.info(' Input nama pengawal Enternal  ')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSubmit"]').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    Log.info(' Menekan Button Submit  ')
    attach(data=driver.get_screenshot_as_png())
"""
@mark.fixture_test()
def test_DLP_005():
    #belum
    print('.')
    print('== next == DLP-005 / Pengecekan cetak surat')
    sleep(driver)
    print('Mencetak surat')
    #belum
    Log.info('Mencetak surat data yang berstatus “Dalam Proses” dengan ceklis data yang akan dicetak suratnya pada checkbox lalu klik button Cetak Surat')


                                                    ########## masuk ke halaman ubah ##########




@mark.fixture_test()
def test_DLP_006():
    print('.')
    print('== NEXT == DLP-006 / Pengecekan tambah surat penempatan dan ubah status pendaftaran (Verifikasi Diziinkan)')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    time.sleep(0.1)
    print('.')
    Log.info('Memilih Dropdown Nama')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaEditUbah)
    Log.info(' Input Nama  ')

    sleep(driver)

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "dalamProses")))
    driver.find_element(By.ID, 'dalamProses').click()
    sleep(driver)


    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    Log.info('Click Button Cari')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    time.sleep(10)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    time.sleep(3)

    print('.')
    Log.info('Click Button Update')
    attach(data=driver.get_screenshot_as_png())

    time.sleep(5)
    sleep(driver)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    
    
    print('.')
    Log.info('Ubah No SK Berhasil')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@id=\'fileSK\']/div/button/span").click()
    time.sleep(3)
    pyautogui.write("///////users/will/Downloads/pdf/rere.pdf")
    time.sleep(2)
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.press('enter')
    time.sleep(1)
    print('Pilih PDF')
    sleep(driver)

    Log.info('Upload PDF')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusPendaftaran"]')))
    driver.find_element(By.XPATH, '//*[@id="statusPendaftaran"]').send_keys("Diizinkan")
    driver.find_element(By.XPATH, "//li[contains(.,\'Diizinkan\')]").click()
    print('klik button search')
    sleep(driver)
    driver.find_element(By.ID, 'buttonSubmit').click()
    print('.')
    Log.info('ubah status pendaftaran')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_007():
    print('.')
    print('== NEXT == DLP-007 / Pengecekan tambah surat penempatan dan ubah status pendaftaran (Verifikasi Ditolak)')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//li[contains(.,\'Nama\')]").click()
    time.sleep(0.1)
    print('.')
    Log.info('Memilih Dropdown Nama')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaEditUbah)
    Log.info(' Input Nama  ')

    sleep(driver)

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5 > path")))
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "dalamProses")))
    driver.find_element(By.ID, 'dalamProses').click()
    sleep(driver)


    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    print('.')
    Log.info('Click Button Cari')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    driver.implicitly_wait(30)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    time.sleep(10)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    time.sleep(3)

    print('.')
    Log.info('Click Button Update')
    attach(data=driver.get_screenshot_as_png())

    time.sleep(5)
    sleep(driver)
    driver.implicitly_wait(10)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSubmit"]')))
    
    driver.find_element(By.ID, 'noSK').click()
    driver.find_element(By.ID, 'noSK').clear()
    driver.find_element(By.ID, 'noSK').send_keys(noSKUbah)
    print('.')
    Log.info('Ubah No SK Berhasil')
    attach(data=driver.get_screenshot_as_png())


    sleep(driver)
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@id=\'fileSK\']/div/button/span").click()
    time.sleep(3)
    pyautogui.write("///////users/will/Downloads/pdf/rere.pdf")
    time.sleep(2)
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.hotkey("backspace")
    pyautogui.press('enter')
    time.sleep(1)
    print('Pilih PDF')
    sleep(driver)

    Log.info('Upload PDF')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusPendaftaran"]')))
    driver.find_element(By.XPATH, '//*[@id="statusPendaftaran"]').send_keys("Di")
    driver.find_element(By.XPATH, "//li[contains(.,\'Ditolak\')]").click()
    print('klik button search')
    sleep(driver)
    driver.find_element(By.ID, 'buttonSubmit').click()
    print('.')
    Log.info('ubah status pendaftaran')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_DLP_008():
    print('.')
    print('== NEXT == DLP-008 CARI DATA WBP TADI / Pengecekan tampilan detail data Lalu Lintas ')
    sleep(driver)
    driver.implicitly_wait(30)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-blue-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-blue-500 .h-5").click()
    time.sleep(3)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr/td[1]/div/button')))
    driver.find_element(By.ID, 'backButton').click()
    Log.info('Membuka Halaman Detail  ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_009():
    print('.')
    print('== NEXT == DLP-009 / Pengecekan cetak data lalu lintas dengan format Excel')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/button').click()
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info('Export Excel')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_DLP_010():
# Melakukan export data tabel ke pdf
    print('.')
    print('== NEXT == DLP-010 / Pengecekan cetak data lalu lintas dengan format PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/button').click()
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/button[2]').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    print('.')
    Log.info('Export PDF')
    attach(data=driver.get_screenshot_as_png())
    
@mark.fixture_test()
def test_DLP_011():
    print('.')
    print('== NEXT == DLP-011 / Pengecekan cetak data lalu lintas dengan format PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#printButton > #printButton").click()
    driver.find_element(By.CSS_SELECTOR, '#printButton .el-button:nth-child(2) > span').click()
    print('.')
    Log.info('Cetak')
    attach(data=driver.get_screenshot_as_png())
"""

@mark.fixture_test()
def test_exit():
    quit(driver)