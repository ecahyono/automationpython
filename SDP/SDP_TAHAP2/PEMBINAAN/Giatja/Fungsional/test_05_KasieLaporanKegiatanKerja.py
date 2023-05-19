from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_5_KasieLaporan.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)

@pytest.mark.webtest
def test_SetupOs_Kasie():
    global driver, pathData
    driver = initDriver()
    pathData = loadDataPath()  
    Log.info('Setup Os Akses aplikasi SDP')


@pytest.mark.webtest
def test_TC_GIATJA_024():    
    Op_Giatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login Kasie')

@pytest.mark.webtest
def test_TC_GIATJA_025():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kasie mengakses halaman Laporan Kegiatan Kerja dan Produksi')

@pytest.mark.webtest
def test_TC_GIATJA_026():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januarikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Kegiatan Kerja')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuarikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Kegiatan Kerja')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Kegiatan Kerja')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Kegiatan Kerja')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Kegiatan Kerja')
     
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Kegiatan Kerja')
     
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julikegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Kegiatan Kerja')
     
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustuskegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Kegiatan Kerja')
     
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septemberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Kegiatan Kerja')
     
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktoberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Kegiatan Kerja')
     
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novemberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Kegiatan Kerja')
     
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desemberkegiatan-kerja0").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Kegiatan Kerja')

    Log.info('1. Klik status pada bulan / tahun yang akan di verifikasi')

    

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/span[2]/span")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "verifikasi")))
    driver.find_element(By.ID, "verifikasi").click()
    Log.info('2. Pada halaman Laporan Kegiatan Kerja dan Produk, klik button "Verifikasi"')

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "cancel")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "statuVerifikasi")))
    driver.find_element(By.ID, "statuVerifikasi").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'Sudah Verifikasi')]")))
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[contains(.,'Sudah Verifikasi')]").click()
    Log.info('Pilih status verifikasi"')

    driver.find_element(By.ID, "keterangan").send_keys(keteranganFaker)
    Log.info('input Keterangan ')

    driver.find_element(By.ID, "submitButton").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Laporan Berhasil Diperbarui')]")))

    Log.info('4. Klik button Simpan')

    time.sleep(2)
    Log.info('Kasie melakukan verifikasi pada Laporan Kegiatan Kerja dan Produksi yang telah di generate oleh operator')

@pytest.mark.webtest
def test_Exit_Kasie():
    Log.info('Close Browser')
    driver.close()
    
