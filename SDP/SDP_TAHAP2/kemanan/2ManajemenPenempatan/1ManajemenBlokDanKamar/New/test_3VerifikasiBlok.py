from Source import *

import logging
Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('Log2KamarTambah.log', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

sheetrange = wb['tambahBlokdanKamar']

@mark.fixture_test()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.fixture_test()
def test_2_login():
    Spv_KeamananSorong(driver)
    Log.info('Login Operator Manajemen Penempatan')

@mark.fixture_test()
def test_3_AksesMenu():

    driver.implicitly_wait(10)
    nav1 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['MainText'])
    ActionChains(driver).move_to_element(nav1).perform()
    element2 = driver.find_element(By.XPATH, pathData['AksesMenu']['Keamanan']['child']['ManajemenPenempatan']['MainText'])
    time.sleep(1)
    ActionChains(driver).move_to_element(element2).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, 'Manajemen Blok dan Kamar').click()
    sleep(driver)
    print('.')
    Log.info('Akses halaman Daftar Lalu Lintas P2U External')
    attach(data=driver.get_screenshot_as_png())

    i = 2
        
    while i <= len(sheetrange['A']):
    
        filterColumn                            = sheetrange['B'+str(i)].value
        namablok                                = sheetrange['C'+str(i)].value
        
        verifikasi                              = sheetrange['S'+str(i)].value
        keterangan                              = sheetrange['S'+str(i)].value
    
    

        try:
            sleep(driver)
            driver.implicitly_wait(10)
            sleep(driver)
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.border:nth-child(1)')))
            driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
            print('.')
            Log.info('Click Button Tambah halaman Pemetaan Block')
            attach(data=driver.get_screenshot_as_png())
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'backButton')))
            
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'searchButton')))
            driver.find_element(By.ID, 'kataKunci').send_keys(namablok)
            driver.find_element(By.ID, 'searchButton').click()
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'searchButton')))
            Log.info('Search Nama Blok')


            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'searchButton')))
            driver.find_element(By.CSS_SELECTOR, '#verifikasiButton-0 .h-5').click()

            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'submitButton')))
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'status_verifikasi')))
            driver.find_element(By.ID, 'status_verifikasi').click()

            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//li[contains(.,\'"+ verifikasi +"')]")))
            driver.find_element(By.XPATH, "//li[contains(.,\'"+ verifikasi +"')]").click()
            
            driver.find_element(By.ID, 'keterangan').send_keys(keterangan)
            
            driver.find_element(By.ID, 'submitButton').click()

        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

def teardown():
    quit(driver)