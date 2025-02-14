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


from Settings.setup import initDriver, loadDataPath, quit, buttonTambah, buttonSubmit, selectKategoriPegawai, selectKategoriTamuDinas, sleep
from Settings.login import login, loginSPV

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('RegisterH_UAT.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrangeindex = wb['RegisterH_Index']
print(".")
print("Halaman index, masukan baris yang akan dibaca. . .")

index  = input("")

filterColumnindex                                = sheetrangeindex['B'+str(index)].value
NamaWBPindex                                     = sheetrangeindex['C'+str(index)].value
noSuratindex                                     = sheetrangeindex['D'+str(index)].value
lamaPengasinganindex                             = sheetrangeindex['E'+str(index)].value
tanggalMulaiindex                                = sheetrangeindex['F'+str(index)].value
tanggalKembaliindex                              = sheetrangeindex['G'+str(index)].value
semuaIndex                                       = sheetrangeindex['H'+str(index)].value



@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()

                                ############################################################### LOGIN OPERATOR ###############################################################

@mark.fixture_test()
def test_2_login():
    print(' == NEXT == Login Sebagai OPERATOR UPT')
    sleep(driver)
    login(driver)


@mark.fixture_test()
def test_RTH_001():
    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Register H').click()

    Log.info('akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_RTH_002():


    print(' == NEXT ==  - RTH 002 / Melakukan pengecekan filtering data')
    sleep(driver)
    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumnindex == 'NamaWBP':

        Log.info('memilih filter berdasarkan nama ')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('input kata kunci nama')
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(NamaWBPindex)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))


    elif filterColumnindex == 'noSurat':
        Log.info('Memilih Filter Column No surat')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('no')
        driver.find_element(By.XPATH, '//*[@id="noSurat"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('Input No surat')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(noSuratindex)


        Log.info('Search Data Kategori Nomor surat ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "lamaPerasingan":

        driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(lamaPengasinganindex)


        Log.info('Search Data lama perasingan ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "tanggalMulai":
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        sleep(driver)

        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalMulai"]')))
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').send_keys(tanggalMulaiindex)


        Log.info('Search Data Form Kategori Nama ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnindex == 'tanggalKembali':

        time.sleep(1)
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').click()
        sleep(driver)

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalSelesai"]')))
        driver.find_element(By.XPATH, '//*[@id="tanggalSelesai"]').send_keys(tanggalKembaliindex)


        Log.info('Search tanggal kembali ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnindex == 'semua':
        driver.find_element(By.ID, 'filterColumn').send_keys('Semua')
        driver.find_element(By.XPATH, '//*[@id="semua"]').click()
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semuaIndex)


        Log.info('Search Data Form Kategori Semua ')
        attach(data=driver.get_screenshot_as_png())

    Log.info('Klik Button search')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    Log.info('Berhasil menampilkan data sesuai dengan kategori yang dipilih pada dropdown dan kata kunci yang diinputkan di halaman Daftar Pengasingan')
    attach(data=driver.get_screenshot_as_png())
@mark.fixture_test()
def test_RTH_003():

    print(' == NEXT ==  - RTH 003 / Mengakses halaman Cari Identitas dengan menekan button Tambah ')
    sleep(driver)

    driver.implicitly_wait(60)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'createButton')))
    driver.find_element(By.ID, 'createButton').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))
    Log.info(' Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())

    Log.info(' (RTH 003) / Berhasil menampilkan halaman Cari Identitas beserta list data WBP  ')
    attach(data=driver.get_screenshot_as_png())


sheetrangeTambah = wb['RegisterH_Tambah']
print(".")
print("Halaman Tambah, masukan baris yang akan dibaca")

tambah  = input("")

filterColumnTambah                                   = sheetrangeTambah['B'+str(tambah)].value
namaTambah                                           = sheetrangeTambah['C'+str(tambah)].value
jenisKejahatanTambah                                 = sheetrangeTambah['D'+str(tambah)].value
noRegistrasiTambah                                   = sheetrangeTambah['E'+str(tambah)].value
semuaTambah                                          = sheetrangeTambah['F'+str(tambah)].value

noSuratTambah                                         = sheetrangeTambah['G'+str(tambah)].value
tanggalSuratTambah                                    = sheetrangeTambah['H'+str(tambah)].value
tanggalMulaiTambah                                    = sheetrangeTambah['I'+str(tambah)].value
lamaPengasinganTambah                                 = sheetrangeTambah['J'+str(tambah)].value
alasanTambah                                          = sheetrangeTambah['K'+str(tambah)].value


filterStatusVerifikasi                                = sheetrangeTambah['M'+str(tambah)].value
UbahStatusVerifikasi                                  = sheetrangeTambah['N'+str(tambah)].value
keteranganVerifikasi                                  = sheetrangeTambah['O'+str(tambah)].value


@mark.fixture_test()
def test_RTH_004():
    
    print(' == NEXT ==  - ( RTH-004 ) / Melakukan pencarian data identitas WBP lalu mendaftarkannya dengan memilih kategori pencarian kemudian input kata kunci dan klik button Cari')
    driver.implicitly_wait(60)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterColumn')))
    sleep(driver)
    driver.find_element(By.ID, 'filterColumn').click()

    if filterColumnTambah == 'nama':
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('nama')
        Log.info('Klik Search Kategori berdasarkan Nama')
        attach(data=driver.get_screenshot_as_png())

        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="nama"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.ID, 'kataKunci').send_keys(namaTambah)
        Log.info('search Nama')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnTambah == 'jenisKejahatan':
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('jenis')
        Log.info('Klik Search Kategori berdasarkan semua')
        attach(data=driver.get_screenshot_as_png())

        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="jenisKejahatan"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.ID, 'kataKunci').send_keys(jenisKejahatanTambah)
        Log.info('search Jenis Kejahatan')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnTambah == 'noRegistrasi':
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('No')
        Log.info('Klik Search Kategori berdasarkan semua')
        attach(data=driver.get_screenshot_as_png())

        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="nomorReg"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        driver.find_element(By.ID, 'kataKunci').send_keys(noRegistrasiTambah)
        Log.info('search Nomor Registrasi')
        attach(data=driver.get_screenshot_as_png())


    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    Log.info('Klik Button Search')
    attach(data=driver.get_screenshot_as_png())

    Log.info('(BERHASIL RTH-004) / Menampilkan data WBP sesuai kategori yang dipilih dan kata kunci yang diinputkan')

@mark.fixture_test()
def test_RTH_005():
    print(' == NEXT ==  - ( RTH-005 ) / Mendaftarkan WBP untuk ditambahkan pengasingannya dengan menekan button Daftarkan pada kolom aksi di tabel ')
    sleep(driver)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'view0').click()

    Log.info('(RTH-005) / Menampilkan halaman Tambah Pengasingan')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_RTH_006():
    print(' == NEXT == ( RTH-006 ) / Menambahkan data pengasingan WBP dengan menginputkan data pengasingan lalu submit data ')
    sleep(driver)


    print(' == NEXT == Input No surat')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'detailRegis')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'noSurat')))
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').send_keys(noSuratTambah)
    Log.info('Input Nomor Surat')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Input Tanggal Surat')
    sleep(driver)
    driver.find_element(By.ID, 'tanggalSurat').send_keys(tanggalSuratTambah)
    driver.find_element(By.ID, 'tanggalSurat').send_keys(Keys.ENTER)
    Log.info('Input Tanggal Surat')
    attach(data=driver.get_screenshot_as_png())


    print(' == NEXT == Input Tanggal Mulai')
    sleep(driver)
    driver.find_element(By.ID, 'tanggalMulai').send_keys(tanggalMulaiTambah)
    driver.find_element(By.ID, 'tanggalMulai').send_keys(Keys.ENTER)
    Log.info('Input Tanggal Mulai')
    attach(data=driver.get_screenshot_as_png())


    print(' == NEXT == Input Lama Perasingan')
    sleep(driver)
    driver.find_element(By.XPATH,'//*[@id="lamaPengasingan"]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys('3')
    Log.info('Input Lama Perasingan')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Input Alasan')
    sleep(driver)
    driver.find_element(By.ID, 'alasan').send_keys(alasanTambah)
    Log.info('Input Alasan')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Click Button Submit')
    sleep(driver)
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Click Button Submit')
    attach(data=driver.get_screenshot_as_png())

    Log.info('(RTH-006) / Menampilkan alert berhasil kemudian data ditampilkan pada tabel Halaman Daftar Pengasingan')
    attach(data=driver.get_screenshot_as_png())

                            ############################################################### LOGIN SUPERVISOR ###############################################################

@mark.fixture_test()
def test_RTH_007():

    global driver, pathData
    print(' == NEXT == OPEN NEW BROSWSER UNTUK SUPERVISOR')
    sleep(driver)
    driver = initDriver()
    pathData = loadDataPath()

    print(' == NEXT == Login Sebagai SUPERVISOR')
    sleep(driver)
    loginSPV(driver)
    Log.info('(RTH-007) / Login SPV berhasil')

    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Register H').click()

    Log.info('akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    sleep(driver)
    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumnTambah == 'nama':

        Log.info('memilih filter berdasarkan nama ')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('input kata kunci nama')
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(namaTambah)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))


    elif filterColumnindex == 'noSurat':
        Log.info('Memilih Filter Column No surat')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('no')
        driver.find_element(By.XPATH, '//*[@id="noSurat"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('Input No surat')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(noSuratindex)

        Log.info('Search Data Kategori Nomor surat ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "lamaPerasingan":

        driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(lamaPengasinganindex)

        Log.info('Search Data lama perasingan ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "tanggalMulai":
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        sleep(driver)

        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalMulai"]')))
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').send_keys(tanggalMulaiindex)

        Log.info('Search Data Form Kategori Nama ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnindex == 'tanggalKembali':

        time.sleep(1)
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').click()
        sleep(driver)

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalSelesai"]')))
        driver.find_element(By.XPATH, '//*[@id="tanggalSelesai"]').send_keys(tanggalKembaliindex)

        Log.info('Search tanggal kembali ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnTambah == 'semua':
        driver.find_element(By.ID, 'filterColumn').send_keys('Semua')
        driver.find_element(By.XPATH, '//*[@id="semua"]').click()
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semuaTambah)

        Log.info('Search Data Form Kategori Semua ')
        attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'filterStatus')))
    driver.find_element(By.ID, 'filterStatus').click()
    if filterStatusVerifikasi == 'dalamproses':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
        driver.find_element(By.XPATH, "//li[@id=\'dalamProses\']").click()
        Log.info(' Filter status Dalam Proses ')
        attach(data=driver.get_screenshot_as_png())
    elif filterStatusVerifikasi == 'perbaikan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="perbaikan"]')))
        driver.find_element(By.XPATH, "//li[@id=\'perbaikan\']").click()
        Log.info('.')
        Log.info(' Filter status Dalam Proses ')
        attach(data=driver.get_screenshot_as_png())

    Log.info('Klik Button search')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="modalButton0"]')))
    driver.find_element(By.XPATH, '//*[@id="modalButton0"]').click()
    Log.info('.')
    Log.info('Click Button Status Dalam Proses')
    attach(data=driver.get_screenshot_as_png())

    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="statusVerifikasiModal"]')))
    driver.find_element(By.XPATH, '//*[@id="statusVerifikasiModal"]').click()
    if UbahStatusVerifikasi == 'diizinkan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'diizinkan\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'diizinkan\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Izinkan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatusVerifikasi == 'perbaikan':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'perbaikan\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'perbaikan\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di perbaikan')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatusVerifikasi == 'ditolak':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'ditolak\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'ditolak\'])[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Di Tolak')
        attach(data=driver.get_screenshot_as_png())
    elif UbahStatusVerifikasi == 'dalamProses':
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "(//li[@id=\'dalamProses\'])[2]")))
        driver.find_element(By.XPATH, "(//li[@id=\'dalamProses\']/span)[2]").click()
        Log.info('.')
        Log.info('Ubah Status Menjadi Dalam Proses')
        attach(data=driver.get_screenshot_as_png())



    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "keterangan").click()
    driver.find_element(By.ID, "keterangan").send_keys(keteranganVerifikasi)
    Log.info('.')
    Log.info('Input Keterangan')
    attach(data=driver.get_screenshot_as_png())



    sleep(driver)
    driver.implicitly_wait(60)
    driver.find_element(By.ID, "simpanVerifikasi").click()
    WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    Log.info('.')
    Log.info('Button Simpan Verifikasi')
    attach(data=driver.get_screenshot_as_png())


    print('== NEXT == Cek data hasil verifikasi')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="diizinkan"]')))
    driver.find_element(By.XPATH, "//li[@id=\'diizinkan\']").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    Log.info(' cek status sudah menjadi dizinkan ')
    attach(data=driver.get_screenshot_as_png())



                            ############################################################### LOGIN OPERATOR ###############################################################

@mark.fixture_test()
def test_RTH_008():
    print(' == NEXT == ( RTH-010 ) / Melakukan Perpanjangan Pengasingan Login sebgai Operator upt ')
    global driver, pathData
    sleep(driver)
    driver = initDriver()
    pathData = loadDataPath()

    print(' == NEXT == / Login ')
    sleep(driver)
    login(driver)

    driver.implicitly_wait(30)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    time.sleep(0.5)
    ActionChains(driver).move_to_element(nav1).perform()
    driver.find_element(By.LINK_TEXT, 'Register H').click()

    Log.info('akses menu daftar lalu lintas')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == / Memilih Filter Column untuk filter data ')
    sleep(driver)
    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumnTambah == 'nama':

        Log.info('memilih filter berdasarkan nama ')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('input kata kunci nama')
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(namaTambah)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))


    elif filterColumnindex == 'noSurat':
        Log.info('Memilih Filter Column No surat')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('no')
        driver.find_element(By.XPATH, '//*[@id="noSurat"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('Input No surat')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(noSuratindex)

        Log.info('Search Data Kategori Nomor surat ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "lamaPerasingan":

        driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        Log.info('Input Lama Perasingan')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(lamaPengasinganindex)

        Log.info('Search Data lama perasingan ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "tanggalMulai":
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        print(' == NEXT == Input Tangal mulai')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalMulai"]')))
        Log.info('input Tanggal Mulai')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').send_keys(tanggalMulaiindex)

        Log.info('Search Data Form Kategori Nama ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnindex == 'tanggalKembali':
        print(' == NEXT == Input Tanggal Kembali')

        time.sleep(1)
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').click()
        Log.info('Input tanggal kembali')
        sleep(driver)

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalSelesai"]')))
        driver.find_element(By.XPATH, '//*[@id="tanggalSelesai"]').send_keys(tanggalKembaliindex)

        Log.info('Search tanggal kembali ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnTambah == 'semua':
        driver.find_element(By.ID, 'filterColumn').send_keys('Semua')
        driver.find_element(By.XPATH, '//*[@id="semua"]').click()
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semuaTambah)

        Log.info('Search Data Form Kategori Semua ')
        attach(data=driver.get_screenshot_as_png())

    print('== NEXT == Klik filter status dalam proses')
    sleep(driver)
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
    driver.find_element(By.ID, 'dalamProses').click()
    Log.info(' Filter status Dalam Proses ')
    attach(data=driver.get_screenshot_as_png())

    Log.info('Klik Button search')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()

    Log.info('klik Perpanjangan Perasingan')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, '#perpanjangan0').click()

    Log.info('Click Status Di izinkan')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Input No surat')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'detailRegis')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'noSurat')))
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').send_keys(noSuratTambah)
    Log.info('Input Nomor Surat')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Input Tanggal Surat')
    sleep(driver)
    driver.find_element(By.ID, 'tanggalSurat').send_keys(tanggalSuratTambah)
    driver.find_element(By.ID, 'tanggalSurat').send_keys(Keys.ENTER)
    Log.info('Input Tanggal Surat')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Input Lama Perasingan')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys('3')
    Log.info('Input Lama Perasingan')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Input Alasan')
    sleep(driver)
    driver.find_element(By.ID, 'alasan').send_keys(alasanTambah)
    Log.info('Input Alasan')
    attach(data=driver.get_screenshot_as_png())

    print(' == NEXT == Click Button Submit')
    sleep(driver)
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    Log.info('Click Button Submit')
    attach(data=driver.get_screenshot_as_png())


    Log.info('(RTH-006) / Menampilkan alert berhasil kemudian data ditampilkan pada tabel Halaman Daftar Pengasingan')
    attach(data=driver.get_screenshot_as_png())
    



sheetrangeEdit = wb['RegisterH_Edit']
print(".")
print("Halaman Edit, masukan baris yang akan dibaca . . . .")

edit  = input('')

noSuratEdit                                         = sheetrangeEdit['B'+str(edit)].value
tanggalSuratEdit                                    = sheetrangeEdit['C'+str(edit)].value
tanggalMulaiEdit                                    = sheetrangeEdit['D'+str(edit)].value
lamaPengasinganEdit                                 = sheetrangeEdit['E'+str(edit)].value
alasanEdit                                          = sheetrangeEdit['F'+str(edit)].value


@mark.fixture_test()
def test_RTH_009_searhdata():
    print(' == NEXT == (RTH - 009)  / Pengecekan data Pengasingan WBP yang telah diubah')
    sleep(driver)

    print(' == NEXT == / Memilih Filter Column untuk filter data ')
    sleep(driver)
    driver.find_element(By.ID, 'filterColumn').click()
    if filterColumnTambah == 'nama':
        
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('input kata kunci nama')
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(namaTambah)
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
        Log.info('memilih filter berdasarkan nama ')


    elif filterColumnindex == 'noSurat':
        Log.info('Memilih Filter Column No surat')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('no')
        driver.find_element(By.XPATH, '//*[@id="noSurat"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))

        Log.info('Input No surat')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(noSuratindex)

        Log.info('Search Data Kategori Nomor surat ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "lamaPerasingan":

        driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
        Log.info('Input Lama Perasingan')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(lamaPengasinganindex)

        Log.info('Search Data lama perasingan ')
        attach(data=driver.get_screenshot_as_png())

    elif filterColumnindex == "tanggalMulai":
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        print(' == NEXT == Input Tangal mulai')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').click()
        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalMulai"]')))
        Log.info('input Tanggal Mulai')
        sleep(driver)
        driver.find_element(By.XPATH, '//*[@id="tanggalMulai"]').send_keys(tanggalMulaiindex)

        Log.info('Search Data tanggal mulai ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnindex == 'tanggalKembali':
        print(' == NEXT == Input Tanggal Kembali')
        sleep(driver)

        time.sleep(1)
        driver.find_element(By.ID, 'filterColumn').send_keys('tgl')
        driver.find_element(By.XPATH, '//*[@id="tanggalKembali"]').click()
        Log.info('Input tanggal kembali')

        WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tanggalSelesai"]')))
        driver.find_element(By.XPATH, '//*[@id="tanggalSelesai"]').send_keys(tanggalKembaliindex)

        Log.info('Search tanggal kembali ')
        attach(data=driver.get_screenshot_as_png())
    elif filterColumnTambah == 'semua':

        print(' == NEXT == semua')
        sleep(driver)
        driver.find_element(By.ID, 'filterColumn').send_keys('Semua')
        driver.find_element(By.XPATH, '//*[@id="semua"]').click()
        driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys(semuaTambah)

        Log.info('Search Data Form Kategori Semua ')
        attach(data=driver.get_screenshot_as_png())
    
    
    print('== NEXT == Klik filter status dalam proses')
    sleep(driver)
    driver.find_element(By.ID, 'filterStatus').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dalamProses"]')))
    driver.find_element(By.ID, 'dalamProses').click()
    Log.info(' Filter status Dalam Proses ')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == Klik button search')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, '//*[@id="buttonSearch"]').click()
    Log.info('Klik Button search')




@mark.fixture_test()
def test_RTH_009_editData():

    print('== NEXT == Click Button Edit')
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="update0"]')))
    time.sleep(0.5)
    driver.find_element(By.XPATH,'//*[@id="update0"]').click()
    Log.info(' (RTH - 011) / saearch data wbp yang akan di edit berhasil')

    print('== NEXT == Ubah No Surat')
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').clear()
    driver.find_element(By.XPATH, '//*[@id="noSurat"]').send_keys(noSuratEdit)
    Log.info('Berhasil merubah No Surat')
    attach(data=driver.get_screenshot_as_png())


    print('== NEXT == Edit Tanggal Surat')
    sleep(driver)
    driver.find_element(By.ID, 'tanggalSurat').clear()
    driver.find_element(By.ID, 'tanggalSurat').send_keys(tanggalSuratEdit)
    driver.find_element(By.ID, 'tanggalSurat').send_keys(Keys.ENTER)
    Log.info('Edit Tangal Surat berhasil')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == Edti Tangal Mulai')
    sleep(driver)
    driver.find_element(By.ID, 'tanggalMulai').send_keys(tanggalMulaiEdit)
    driver.find_element(By.ID, 'tanggalMulai').send_keys(Keys.ENTER)
    Log.info('Edit tanggal Mulai Berhasil')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == Edit lama perasingan')
    sleep(driver)
    driver.find_element(By.XPATH,'//*[@id="lamaPengasingan"]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="lamaPengasingan"]/div/input').send_keys(lamaPengasinganEdit)
    Log.info(' Edit lama persingan berhasil')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == Edit Alasan')
    sleep(driver)
    driver.find_element(By.ID, 'alasan').clear()
    driver.find_element(By.ID, 'alasan').send_keys(alasanEdit)
    Log.info('Edit alasan berhasil')
    attach(data=driver.get_screenshot_as_png())

    print('== NEXT == Click Button Edit')
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Diperbaharui\')]')))
    Log.info('Click Button Submit Berhasil')
    attach(data=driver.get_screenshot_as_png())

    Log.info(' (RTH - 011) / Menampilkan alert berhasil kemudian data pada tabel Daftar Pengasingan diperbaharui')

@mark.fixture_test()
def test_RTH_010():
    print(' == NEXT == (RTH - 010)  / Pengecekan tampilan detail data Pengasingan WBP ')
    sleep(driver)

    test_RTH_009_searhdata()

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="view0"]')))
    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="view0"]').click()
    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="backButton"]')))

    sleep(driver)
    driver.find_element(By.XPATH, '//*[@id="backButton"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))

    print('.')
    Log.info(' Membuka Halaman Tambah  ')
    attach(data=driver.get_screenshot_as_png())

    Log.info(' (RTH - 010) / ')


@mark.fixture_test()
def test_RTH_011():

    print('== NEXT == (RTH - 011)  / Pergi ke halaman paling belakang / Pengecekan total halaman')
    sleep(driver)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, pathData['Other Search Index']['Pergi Ke']).send_keys('100')  
    time.sleep(1)

    Log.info(' (RTH - 011) / Berhasil menampilkan jumlah halaman data yang ditampilkan pada main grid')
    attach(data=driver.get_screenshot_as_png())



@mark.fixture_test()
def test_RTH_012():

    print(' == NEXT == (RTH - 012)  / Pengecekan navigasi button halaman ')
    sleep(driver)

    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.XPATH, pathData['Other Search Index']['Dropdown Halaman']).click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    sleep(driver)

    Log.info(' (RTH - 012) ')



@mark.fixture_test()
def test_RTH_013():
    print(' == NEXT == (RTH - 013) / Menampilkan halaman sebelumnya dan selanjutnya menggunakan navigasi button ')

    sleep(driver)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, ".btn-next svg").click()
    Log.info('menekan button selanjutanya')

    print(' == NEXT == (RTH - 013) /Menakan Button Sebelumnya ')
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    sleep(driver)
    driver.find_element(By.CSS_SELECTOR, ".btn-prev svg").click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    Log.info('Menekan button sebelumnya')
    Log.info('(RTH - 013) / Berhasil menampilkan halaman sebelumnya dan selanjutnya')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_RTH_014():

    print(' == NEXT == (RTH - 014)  / Mencetak data akses pintu otomatis (sesuai dengan jumlah halaman) dengan menekan Button Export Excel ')
    sleep(driver)

    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, '#excelButton span').click()
    driver.find_element(By.CSS_SELECTOR, '#thisButton > span').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    Log.info('(RTH-014) / Mencetak data portir sesuai dengan total halaman yang dipilih dengan format Excel (.xlsx) kemudian tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_RTH_015():

    print(' == NEXT == (RTH - 015) / Mencetak data Register H (sesuai dengan jumlah halaman) dengan menekan Button Export PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, '#pdfButton > .el-button').click()
    driver.find_element(By.CSS_SELECTOR, '#pdfButton #thisButton').click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil mengunduh file\')]')))
    Log.info('(BERHASIL (RTH - 015) / Berhasil mencetak data Register H otomatis sesuai dengan total halaman yang dipilih dengan format Excel (.xlsx) kemudian tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_RTH_016():

    print('== NEXT == Menjalankan RTH - 016 / Pengecekan cetak data akses pintu otomatis dengan format PDF')
    sleep(driver)
    driver.implicitly_wait(30)
    time.sleep(1)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="buttonSearch"]')))
    driver.find_element(By.CSS_SELECTOR, "#printButton > #printButton").click()
    driver.find_element(By.CSS_SELECTOR, '#printButton .el-button:nth-child(2) > span').click()

    print('.')
    Log.info('(BERHASIL RTH - 016) / Menampilkan halaman preview lalu setelah berhasil mencetak data, tampil alert berhasil')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_exit():

    print(' == NEXT ==  EXIT')
    sleep(driver)
    quit(driver)
