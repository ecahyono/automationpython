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

@mark.webtest()
def test_1_setupOS():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()
    Log.info('Setup Os')

@mark.webtest()
def test_2_login():
    op_keamanan_mp(driver)
    Log.info('Login Operator Manajemen Penempatan')


@mark.webtest()
def test_3_Input():

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

    sleep(driver)
    driver.implicitly_wait(10)
    sleep(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.border:nth-child(1)')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    print('.')
    Log.info('Click Button Tambah halaman Pemetaan Block')
    attach(data=driver.get_screenshot_as_png())
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'backButton')))

    i = 2
        
    while i <= len(sheetrange['A']):
    
        namablok                                = sheetrange['C'+str(i)].value
        lantai                                  = sheetrange['M'+str(i)].value
        nomorKamar                              = sheetrange['N'+str(i)].value
        kelompokJenisKejahatan                  = sheetrange['O'+str(i)].value
        kapasitasInput                          = sheetrange['P'+str(i)].value
        kondisiRuangan                          = sheetrange['Q'+str(i)].value
    
    

            
            
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'searchButton')))
        driver.find_element(By.ID, 'kataKunci').send_keys(namablok)
        driver.find_element(By.ID, 'searchButton').click()
        Log.info('Search Nama Blok')
        
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'searchButton')))
        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#roomButton0 .h-5')))
        sleep(driver)
        driver.find_element(By.CSS_SELECTOR, '#roomButton0 .h-5').click()
            
   
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'backButton')))
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'lantai_id')))
            driver.execute_script("window.scrollTo(0,244.5)")
            time.sleep(3)
            driver.find_element(By.ID, 'lantai_id').click()
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'lantai-0')))
            driver.find_element(By.ID, "lantai-0").click()
            driver.find_element(By.XPATH, "//li[contains(.,\'"+ lantai +"')]").click()
        
            sleep(driver)
            driver.find_element(By.ID, "nomorKamar").click()
            driver.find_element(By.ID, "nomorKamar").send_keys(nomorKamar)

            driver.find_element(By.ID, "kondisiInput").click()
            driver.find_element(By.XPATH, "//li[contains(.,\'"+ kondisiRuangan +"')]").click()
           

            driver.find_element(By.ID, "kel_jenis_kejahatan_id").click()
            driver.find_element(By.XPATH, "//li[contains(.,\'"+ kelompokJenisKejahatan +"')]").click()
           

            driver.find_element(By.ID, "kapasitasInput").click()
            driver.find_element(By.ID, "kapasitasInput").send_keys(kapasitasInput)


            driver.find_element(By.ID, 'submitButton').click()
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID, 'submitButton')))

            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))

            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, "a > #submitButton > span").click()
      


            

        except TimeoutException:
            print("ERRROR")
            pass
                
        sleep(driver)
        i = i + 1
    print('DONE')

def teardown():
    quit(driver)