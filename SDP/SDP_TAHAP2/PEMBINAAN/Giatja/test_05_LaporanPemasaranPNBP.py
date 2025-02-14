from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/Log_5_LaporanPemasaranPNBP.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtestOperator
def test_TC_GIATJA_030():
    sleep(driver)   
    OpKemandirian(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Setup Os')

@pytest.mark.webtestOperator
def test_TC_GIATJA_031():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Laporan Kegiatan Kerja dan pemasaran-pnbpsi')

@pytest.mark.webtestOperator
def test_TC_GIATJA_032():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Sarana')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Sarana')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Sarana')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Sarana')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Sarana')
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Sarana')
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Sarana')
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustuspemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Sarana')
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Sarana')
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktoberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Sarana')
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Sarana')
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Sarana')

    print("Menunggu Loading")
    print("Click Button OK")
    driver.find_element(By.XPATH, "//span[contains(.,'OK')]").click()
    Log.info('Operator mengklik button OK')

    print("Menunggu Loading")
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Membuat Laporan Berhasil !')]")))
    # WebDriverWait(driver, 50).until(EC.invisibility_of_element((By.ID, ".circular")))
    
    time.sleep(2)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "Aprilpemasaran-pnbp1")))
    Log.info('Operator membuat Laporan Kegiatan Kerja dan pemasaran-pnbpsi')
    LogOut(driver)

@pytest.mark.webtestKasie
def test_TC_GIATJA_033():
    print("Login")
    sleep(driver)   
    KasieGiatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Setup Os')

@pytest.mark.webtestKasie
def test_TC_GIATJA_034():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kasie mengakses halaman Laporan Pemasaran PNBPsi')

@pytest.mark.webtestKasie
def test_TC_GIATJA_035():
    sleep(driver)
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Sarana')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Sarana')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Sarana')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Sarana')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Sarana')
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Sarana')
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Sarana')
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustuspemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Sarana')
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Sarana')
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktoberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Sarana')
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Sarana')
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Sarana')
    
    Log.info('1. Klik status pada bulan / tahun yang akan di verifikasi')


    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".circular")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//div[2]/span[2]/span")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "verifikasi")))
    time.sleep(3)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "verifikasi")))
    driver.find_element(By.ID, "verifikasi").click()
    Log.info('2. Pada halaman Laporan Pemasaran PNBP, klik button "Verifikasi"')

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
    Log.info('Kasie membuat Laporan Pemasaran PNBPsi')
    LogOut(driver)

@pytest.mark.webtestKalapas
def test_TC_GIATJA_036():
    KalapasGiatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login Kalapas')

@pytest.mark.webtestKalapas
def test_TC_GIATJA_037():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kalapas mengakses halaman Laporan Kegiatan Kerja dan Produksi')


@pytest.mark.webtestKalapas
def test_TC_GIATJA_038():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Sarana')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuaripemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Sarana')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Sarana')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Sarana')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Sarana')
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Sarana')
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julipemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Sarana')
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustuspemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Sarana')
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Sarana')
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktoberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Sarana')
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Sarana')
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desemberpemasaran-pnbp1").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Sarana')
    
    Log.info('1. Klik status pada bulan / tahun yang akan di verifikasi')

    # WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".circular")))

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "otorisasi")))
    time.sleep(2)   
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "otorisasi")))

    driver.find_element(By.XPATH, "//span[contains(.,'Otorisasi')]").click()
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submitButton > span")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "cancel")))
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, "statuVerifikasi")))
    driver.find_element(By.ID, "statuVerifikasi").click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'Sudah Otorisasi')]")))
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[contains(.,'Sudah Otorisasi')]").click()
    Log.info('Pilih status verifikasi"')

    driver.find_element(By.ID, "keterangan").send_keys(keteranganFaker)
    Log.info('input Keterangan ')

    driver.find_element(By.ID, "submitButton").click()

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(.,'Laporan Berhasil Diperbarui')]")))


    Log.info('Kalapas melakukan otorisasi pada Laporan Kegiatan Kerja dan Produksi yang telah di verifikasi oleh kasie')

def test_quit():
    quit(driver)






    
    