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
    wb = load_workbook(environ.get("KeamananUAT"))

elif platform.system() == 'Windows':
    sys.path.append(environ.get("WINPARENTDIR"))


from Settings.setup import initDriver, loadDataPath, quit, sleep
from Settings.login import login

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('PortirUAT.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)




sheetrangeIndex = wb['Portir_SearchDataIndex']
print('.')
print('Portir Index, Mau Baris Ke Berapa ?')
index  = input('')

filterColumnindex                            = sheetrangeIndex['B'+str(index)].value
nama_lengkapindex                            = sheetrangeIndex['C'+str(index)].value
nomor_indukindex                             = sheetrangeIndex['D'+str(index)].value
NomorSuratindex                              = sheetrangeIndex['E'+str(index)].value
Pendaftarindex                               = sheetrangeIndex['F'+str(index)].value
semuaindex                                   = sheetrangeIndex['G'+str(index)].value
statusColumnindex                            = sheetrangeIndex['H'+str(index)].value


@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()


@mark.fixture_test()
def test_2_login():
    login(driver)
    Log.info('Login Operator')


@mark.fixture_test()
def test_PTR_001():
    print('Menjalankan PTR-001 - Mengakses halaman Portir dengan memilih modul Keamanan kemudian pilih menu Lalu Lintas lalu pilih submenu Portir')

    driver.implicitly_wait(60)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['LaluLintasPortir']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Portir').click()

    Log.info('(Berhasil PTR-001) Berhasil menampilkan halaman Manajemen Portir')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_PTR_002():
    print('.')
    print('== NEXT == PTR-002 - Melakukan pengecekan filtering data')
    Log.info('Klik Filter Column')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()

    if filterColumnindex == 'semua':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'Semua\')]")))
        driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()
        Log.info(' Memilih Dropdown Semua  ')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        Log.info(' Input kata kunci semua  ')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semuaindex)


        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'nomor induk':
        driver.find_element(By.ID, 'filterColumn').send_keys('induk')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Induk\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomor_indukindex)

        Log.info(' Input kata kunci No induk  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'Nomor Surat Penetapan':
        driver.find_element(By.ID, 'filterColumn').send_keys('Surat')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Surat Penetapan\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NomorSuratindex)

        Log.info(' Input kata kunci Nomor Surat Penetapan  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'Pendaftar':
        driver.find_element(By.ID, 'filterColumn').send_keys('Pendaftar')
        driver.find_element(By.XPATH, '//li[contains(.,\'created_by\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Pendaftarindex)
        Log.info(' Input kata kunci Pendaftar  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'NamaLengkap':
        driver.find_element(By.ID, 'filterColumn').send_keys('Nama WBP')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nama_lengkap > span')))
        driver.find_element(By.CSS_SELECTOR, "#nama_lengkap > span").click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nama_lengkapindex)

    Log.info('Ketik Status Keluar Kemanan')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar keamanan')

    Log.info('Memilih Status Keluar Kemanan')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,\'Keluar Keamanan\')]')))
    driver.find_element(By.XPATH, "//li[contains(.,\'Keluar Keamanan\')]").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    Log.info('Klik Button Search')
    sleep(driver)
    driver.find_element(By.ID, 'searchButton').click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    print('.')
    Log.info('(Berhasil PTR-002) Berhasil menampilkan data sesuai dengan kategori yang dipilih pada dropdown di halaman Manajemen Portir')

    attach(data=driver.get_screenshot_as_png())

    print('.')
    print('Menjalankan PTR-003 - Menampilkan halaman detail data identitas WBP dengan menggunakan button (Detail) pada kolom aksi di tabel data identitas ')
    sleep(driver)

    driver.implicitly_wait(60)
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5")))
    time.sleep(0.1)

    Log.info('Klik Button Detile')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()
    print('.')
    Log.info('(BERHASIL PTR-003) Berhasil menampilkan detail data identitas WBP ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_PTR_003():
    print('.')
    print('Menjalankan PTR-003 - Melakukan konfirmasi keluar portir seorang WBP dengan menekan button Konfirmasi Keluar pada halaman detail')
    sleep(driver)
    print('button konfirmasi siap di klik')
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lihatSurat > span")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmButton > span")))
    Log.info('Klik Button Konfirmasi Keluar Keamanan')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#confirmButton > span").click()
    # driver.find_element(By.CSS_SELECTOR, "#lihatSurat > span").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('.')
    Log.info('Menampilkan alert berhasil kemudian mengubah status portir WBP di halaman Manajemen Portir menjadi “Keluar Portir”')

@mark.fixture_test()
def test_PTR_004():
    print('.')
    print('== NEXT == PTR 004 / Menjalankan PTR-004 -Konfirmasi masuk portir WBP')
    print('== NEXT == KLIK FILTER COLUMN')
    sleep(driver)
    Log.info('Klik Filter Kolom')
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()

    if filterColumnindex == 'semua':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'Semua\')]")))
        driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()
        print('.')
        Log.info(' Memilih Dropdown Semua  ')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semuaindex)

        Log.info(' Input kata kunci semua  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'nomor induk':
        driver.find_element(By.ID, 'filterColumn').send_keys('induk')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Induk\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomor_indukindex)

        Log.info(' Input kata kunci No induk  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'Nomor Surat Penetapan':
        driver.find_element(By.ID, 'filterColumn').send_keys('Surat')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Surat Penetapan\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NomorSuratindex)

        Log.info(' Input kata kunci Nomor Surat Penetapan  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'Pendaftar':
        driver.find_element(By.ID, 'filterColumn').send_keys('Pendaftar')
        driver.find_element(By.XPATH, '//li[contains(.,\'created_by\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Pendaftarindex)
        Log.info(' Input kata kunci Pendaftar  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'NamaLengkap':
        driver.find_element(By.ID, 'filterColumn').send_keys('Nama WBP')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nama_lengkap > span')))
        driver.find_element(By.CSS_SELECTOR, "#nama_lengkap > span").click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nama_lengkapindex)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    time.sleep(1)

    Log.info('Klik Filter Status')
    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('keluar portir')


    Log.info('Memilih Status Keluar Portir')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#statusKeluarPortir')))
    driver.find_element(By.CSS_SELECTOR, "#statusKeluarPortir").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))

    Log.info('Klik Button Search')
    sleep(driver)
    driver.find_element(By.ID, 'searchButton').click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    print('.')
    Log.info('(Berhasil PTR-002) Berhasil menampilkan data sesuai dengan kategori yang dipilih pada dropdown di halaman Manajemen Portir')
    attach(data=driver.get_screenshot_as_png())

    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5")))
    time.sleep(0.1)

    Log.info('Klik Button Detail')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()
    print('(BERHASIL PTR-003) Berhasil menampilkan detail data identitas WBP ')
    attach(data=driver.get_screenshot_as_png())


    print('Masuk Ke halaman Detile')
    sleep(driver)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lihatSurat > span")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#confirmButton > span")))

    Log.info('Klik Button Konfirmasi masuk')
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, "#confirmButton > span").click()
    # driver.find_element(By.CSS_SELECTOR, "#lihatSurat > span").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    Log.info('Menampilkan alert berhasil kemudian mengubah status portir WBP di halaman Manajemen Portir menjadi “Masuk Portir”')

@mark.fixture_test()
def test_PTR_005():
    print('.')
    print('== NEXT == PTR-005/ Pengecekan tampilan detail data Portir dan Riwayat Portir')
    sleep(driver)

    print('=== NEXT === FILTER COLUMN')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    Log.info('Memilih Filter Status Column')

    if filterColumnindex == 'semua':

        print('=== NEXT === Memilih Filter Semua')
        sleep(driver)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,\'Semua\')]")))
        driver.find_element(By.XPATH, "//li[contains(.,\'Semua\')]").click()
        Log.info(' Memilih Dropdown Semua  ')
        attach(data=driver.get_screenshot_as_png())

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semuaindex)

        Log.info(' Input kata kunci semua  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'nomor induk':

        print('=== NEXT === Nomor Induk')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('induk')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Induk\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nomor_indukindex)

        Log.info(' Input kata kunci No induk  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'Nomor Surat Penetapan':

        print('=== NEXT === Nomor surat')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('Surat')
        driver.find_element(By.XPATH, '//li[contains(.,\'Nomor Surat Penetapan\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NomorSuratindex)

        Log.info(' Input kata kunci Nomor Surat Penetapan  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'Pendaftar':

        print('=== NEXT === Pendaftar')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('Pendaftar')
        driver.find_element(By.XPATH, '//li[contains(.,\'created_by\')]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(Pendaftarindex)
        Log.info(' Input kata kunci Pendaftar  ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == 'NamaLengkap':

        print('=== NEXT === Nama Lengkap')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('Nama WBP')
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nama_lengkap > span')))
        driver.find_element(By.CSS_SELECTOR, "#nama_lengkap > span").click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(nama_lengkapindex)

    print('=== NEXT === Masuk Portir')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="statusColumn"]').send_keys('masuk portir')
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#statusMasukPortir')))
    driver.find_element(By.CSS_SELECTOR, "#statusMasukPortir").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    Log.info('Memilih Status Masuk Portir')

    print('=== NEXT === Search Button')
    sleep(driver)
    driver.find_element(By.ID, 'searchButton').click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    Log.info('Klik Button Search')
    print('.')
    Log.info('(Berhasil PTR-006)/ Berhasil menampilkan data portir dan riwayat portir WBP yang dipilih dengan sesuai')

    attach(data=driver.get_screenshot_as_png())


    print('=== NEXT === Klik Button Search')
    sleep(driver)
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".h-5")))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".h-5")))
    time.sleep(0.1)
    print('.')
    driver.find_element(By.CSS_SELECTOR, ".h-5").click()
    attach(data=driver.get_screenshot_as_png())
    Log.info('Click Button Detile')

    print('.')
    print('menunggu halaman ditampilkan')
    sleep(driver)
    time.sleep(2)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#lihatSurat > span")))
    Log.info('(BERHASIL PTR-006) Berhasil menampilkan detail data identitas WBP ')

    print('== NEXT == / Klik Back Button untuk kembali ke halaman Index')
    sleep(driver)
    driver.find_element(By.ID, 'backButton').click()

@mark.fixture_test()
def test_PTR_006():
    print('== NEXT == PTR - 006 / Mencetak data portir (sesuai dengan jumlah halaman) dengan menekan Button Export Excel')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, '#excelButton span').click()
    driver.find_element(By.CSS_SELECTOR, '#thisButton > span').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    Log.info('(PTR-006) / Mencetak data portir sesuai dengan total halaman yang dipilih dengan format Excel (.xlsx) kemudian tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_PTR_007():
    # Melakukan export data tabel ke pdf
    print('== NEXT == PTR - 011 / Mencetak data portir (sesuai dengan jumlah halaman) dengan menekan Button Export PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR,'#pdfButton span').click()
    driver.find_element(By.CSS_SELECTOR,'#pdfButton #thisButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    Log.info('(PTR-11) / Mencetak data portir sesuai dengan total halaman yang dipilih dengan format PDF (.pdf) kemudian tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_PTR_008():
    print('=== NEXT == PTR-012 / Mencetak data portir (sesuai dengan jumlah halaman) yang terhubung langsung dengan perangkat tambahan (printer)')
    sleep(driver)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    driver.find_element(By.CSS_SELECTOR, "#printButton > #printButton").click()
    driver.find_element(By.CSS_SELECTOR, '#printButton .el-button:nth-child(2) > span').click()
    Log.info('(PTR-012) / Menampilkan halaman preview lalu setelah berhasil mencetak data, tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_exit():
    quit(driver)