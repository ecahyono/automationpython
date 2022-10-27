from re import T
from socket import send_fds
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

@mark.fixture_test()
def test_setup():
    global driver
    swin = Service(r'C:/Users/user/Documents/TRCH/chromedriver.exe')
    smac = Service('/Users/will/Downloads/chromedriver')
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(service=smac)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif platform.system() == 'Windows':
        driver = webdriver.Chrome(service=swin)
        driver.get("http://192.168.2.11:32400/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    print('.')
    print('==========setup OS berhasil==========')

@mark.fixture_test()
def test_login():
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div/span").click()
    # ini masuk ke form input username
    driver.find_element(By.ID, "username").click()
    driver.find_element(By.ID, "username").send_keys("test-user")
    driver.find_element(By.ID, "password").send_keys("password")
    # click button login
    driver.find_element(By.ID, "kc-login").click()
    WebDriverWait(driver, 10)
    print('.')
    print('==========Login berhasil==========')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_akses_menu():
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul/li[2]/div')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()

    element2 = driver.find_element(By.XPATH, "//div[4]/div/ul/li/div")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Daftar Lalu Lintas').click()
    print('.')
    print('==========akses menu daftar lalu lintas==========')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_search_data_kategori_nama(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('nama')
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="namaLengkap"]').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('EYONO BIN CAS')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    print('.')
    print('=================================================================================Search Data Form Kategori Nama Berhasil')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_search_data_kategori_NoInduk(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('induk')
    driver.find_element(By.XPATH, '//*[@id="nomorInduk"]').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('50120220819000')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    print('.')
    print('================================================================================= Search Data Form Kategori No Induk Berhasil ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_search_data_kategori_Jenis(): #Melakukan pencarian data berdasarkan kategori dengan memilih kategori dan menginputkan kata kunci lalu data table yang ditampilkan sesuai
    driver.implicitly_wait(20)
    time.sleep(1)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('jenis')
    driver.find_element(By.XPATH, ' //*[@id="deskripsiDr"]').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('Anak Kembali ke Orang Tua')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    
    print('.')
    print('================================================================================= Search Data Form Kategori No Induk Berhasil')
    attach(data=driver.get_screenshot_as_png())

"""
@mark.fixture_test()
def test_search_data_kategori_tglkeluar():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('keluar')
    driver.find_element(By.XPATH, '//*[@id="keluarKeamanan"]').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('20/10/2022')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    print('.')
    print('=================================================================================Search Data Form Kategori No Induk Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_search_data_kategori_tglkembali():
    driver.implicitly_wait(20)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="filterColumn"]')))
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').click()
    driver.find_element(By.XPATH, '//*[@id="filterColumn"]').send_keys('induk')
    driver.find_element(By.XPATH, ' //*[@id="tanggalKembali"]').click()
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="kataKunci"]')))
    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('21/10/2022')
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button').click()
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    print('.')
    print('=================================================================================Search Data Form Kategori No Induk Berhasil ')
    attach(data=driver.get_screenshot_as_png())
"""

@mark.fixture_test()
def test_clik_clear_value(): #Mengosongkan kata kunci dan kategori dengan klik button clear value
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, '//*[@id="filterColumn"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-select__caret:nth-child(2) > svg").click()
    print('.')
    print('=================================================================================Click Clear Value Button filter Colum Berhasil ')
    attach(data=driver.get_screenshot_as_png())

    driver.find_element(By.XPATH, '//*[@id="kataKunci"]').send_keys('tessssst')
    time.sleep(0.5)
    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, '//*[@id="kataKunci"]')
    actions = ActionChains(driver)
    actions.move_to_element(nav1).perform()
    element2 = driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg")
    time.sleep(1)
    actions2 = ActionChains(driver)
    actions2.move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".el-input__clear > svg").click()
    print('.')
    print('================================================================================= Click Clear Value Button Kata Kunci Berhasil ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_sortir_data_table():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//span/i[2]").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[3]/div/span").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[4]/div").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[5]/div/span/i").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, "//th[6]/div/span/i").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    #5 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'5/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    
    time.sleep(1)
    #10 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'10/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
    
     #20 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'20/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
   
    #50 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'50/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
    #100 HALAMAN
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/span[2]/div/div/div/input').click()
    driver.find_element(By.XPATH, "//li[contains(.,\'100/halaman\')]").click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys(Keys.BACKSPACE)
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[4]/div/span[3]/div/input').send_keys('2')
    time.sleep(1)
    print('.')
    print('================================================================================= Menampilkan 5, 10, 20, 50, 100 Berhasil ')
    attach(data=driver.get_screenshot_as_png())



"""




@mark.fixture_test()
def test_jumlah_perhalaman():
    driver.implicitly_wait(10)

@mark.fixture_test()
def test_data_table_sesudah_dan_sebelum():
    driver.implicitly_wait(10)

@mark.fixture_test()
def test_input_lebih_dari_jumlah_halaman():
    driver.implicitly_wait(10)

@mark.fixture_test()
def test_export_dan_cetak():
    driver.implicitly_wait(10)

@mark.fixture_test()
def test_membuka_halaman_tambah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    print('=================================================================================Click Button Tambah Berhasil=================================================================================')
    attach(data=driver.get_screenshot_as_png())

@mark.fixture_test()
def test_membuka_halaman_detail():
    driver.implicitly_wait(10)

@mark.fixture_test()
def test_membuka_halaman_ubah():
    driver.implicitly_wait(10)
    WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-green-500 .h-5")))
    driver.find_element(By.CSS_SELECTOR, ".text-green-500 .h-5").click()
    print('.')
    print('=================================================================================Click Button Update Berhasil================================================================================= ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_back_to_top():
    driver.implicitly_wait(10)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]').click()
    print('.')
    print('=================================================================================Click Button Back To Top Berhasil=================================================================================')
    attach(data=driver.get_screenshot_as_png())
"""
@mark.fixture_test()
def test_export_exel():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    print('================================================================================= Export Excel Berhasil  ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_export_pdf():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/button').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[2]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    print('================================================================================= Export PDF Berhasil   ')
    attach(data=driver.get_screenshot_as_png())


@mark.fixture_test()
def test_cetak():
    driver.implicitly_wait(10)
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div/div/button')))
    driver.find_element(By.XPATH, '//*[@id="printButton"]').click()
    driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[1]/div[2]/div/div/div[5]/div[3]/div/div/div/div[2]/div/button[2]').click()
    print('.')
    print('================================================================================= Cetak Berhasil   ')
    attach(data=driver.get_screenshot_as_png())




def teardown():
    time.sleep(20)
    driver.close()
    driver.quit()