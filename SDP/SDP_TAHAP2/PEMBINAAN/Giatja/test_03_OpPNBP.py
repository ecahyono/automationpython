from source import *


Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_3_OpPNBP.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'Pemasaran'

fake = Faker('id_ID')
akunSetor                                               = ['pendapatan','nihil']
pemasaran                                               = ['#pemasaran0']




@pytest.mark.webtest
def test_TC_GIATJA_015():
    OpKemandirian(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Setup Os')
    sleep(driver)
    MenuPNBP(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman PNBP')

@pytest.mark.webtest
def test_TC_GIATJA_016():
    sleep(driver)
    vars = {}
    vars["x"] = driver.execute_script("return 1")
    condition = True
    while condition:
            
        fake = Faker('id_ID')
        JeniskegiatanPemasaran                                  = ['jenisPemasaran0-opt0','jenisPemasaran0-opt1','jenisPemasaran0-opt2','jenisPemasaran0-opt3']
        pemasaranProdak                                         =  ['#pemasaran0opt0 > span','#pemasaran0opt1 > span']
        for i in range(1):
            TanggalSetorFaker                                   = fake.date_between(start_date='today', end_date='today').strftime('%d/%m/%Y')
            akunSetorFaker                                      = random.choice(akunSetor)
            keteranganFaker                                     = fake.text(max_nb_chars=255)
            pemasaranProdakFaker                                      = random.choice(pemasaranProdak)
            NilaiFaker                                          = fake.random_int(min=100000, max=1000000)
            JeniskegiatanPemasaranFaker                         = random.choice(JeniskegiatanPemasaran)
        


            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
            driver.find_element(By.ID, "createButton").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "backButton")))
            attach(data=driver.get_screenshot_as_png())
            
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "submitButton")))
            driver.find_element(By.ID, "tanggalSetor").click()
            driver.find_element(By.CSS_SELECTOR, "#tanggalSetor").send_keys(TanggalSetorFaker)
            driver.find_element(By.ID, "tanggalSetor").send_keys(Keys.ENTER)

            driver.find_element(By.ID, "akunSetor").click()
            driver.find_element(By.ID, ""+akunSetorFaker+"").click()

            driver.find_element(By.ID, "uploadButton").click()
            time.sleep(1)
            uploadGambar(driver)
            driver.find_element(By.ID, "keterangan").send_keys(keteranganFaker)


            driver.find_element(By.ID, "jenisPemasaran0").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, ""+JeniskegiatanPemasaranFaker+"")))
            driver.find_element(By.ID, ""+JeniskegiatanPemasaranFaker+"").click()
            Log.info('Operator menambahkan data JenisPemasaran')

            driver.find_element(By.ID, "pemasaran0").click()
            # driver.find_element(By.XPATH, "//td[1]/div/div/div/div/div/div/input").click()
            input('pilih pemasaran enter')

            
            # WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ""+pemasaranProdakFaker+"")))
            # driver.find_element(By.CSS_SELECTOR, ""+pemasaranProdakFaker+"").click()

            driver.find_element(By.ID, "jumlah0").send_keys(NilaiFaker)

            driver.find_element(By.ID, "submitButton").click()
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
            attach(data=driver.get_screenshot_as_png())
            Log.info('Operator menambahkan data PNPB')

            vars["x"] = driver.execute_script("return arguments[0]+1", vars["x"])
            condition = driver.execute_script("return (arguments[0]<1)", vars["x"])

@pytest.mark.webtestx
def test_TC_GIATJA_017():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, "#lihat0 > span").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, ".el-dialog__close > svg").click()
    Log.info('Operator melihat bukti setor yang telah di upload')
    attach(data=driver.get_screenshot_as_png())

    Log.info('Operator melihat bukti setor yang telah di upload')
    
@pytest.mark.webtestx
def test_TC_GIATJA_018():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    driver.find_element(By.XPATH, "//tr[1]/td[8]/div/div/div/a/button").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".el-image__inner")))
    driver.find_element(By.CSS_SELECTOR, "#backButton > span").click()
    Log.info('Operator mengakses halaman Detail PNPB')

@pytest.mark.webtestx
def test_TC_GIATJA_019():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#updateButton0 .h-5")))
    driver.find_element(By.CSS_SELECTOR, "#updateButton0 .h-5").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#backButton > span")))

    Log.info('Operator mengakses halaman Ubah PNPB')

@pytest.mark.webtestx
def test_TC_GIATJA_020():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".el-loading-spinner")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "keterangan")))
    driver.find_element(By.ID, "keterangan").send_keys(keteranganFaker)
    driver.find_element(By.CSS_SELECTOR, "#submitButton > span").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))

    Log.info('Operator mengubah data PNPB')

@pytest.mark.webtestx
def test_TC_GIATJA_021():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "createButton")))
    driver.find_element(By.ID, "filterColumn").click()
    driver.find_element(By.XPATH, "//li[@id='semua']").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "buttonSearch")))
    driver.find_element(By.CSS_SELECTOR, ".el-table__row:nth-child(1) .el-space__item > .el-button path").click()
    driver.find_element(By.CSS_SELECTOR, ".el-button--primary > span").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Berhasil Menghapus')]"))).click()
    

    Log.info('Operator menghapus data PNPB')

    quit(driver)








    
    