from source import *

Log = logging.getLogger(__name__)
log_format = '[%(asctime)s %(filename)s->%(funcName)s()]==>%(levelname)s: %(message)s'
fh = logging.FileHandler('./Log/log_07_LaporanSaranaPrasarana.txt', mode="w")
fh.setLevel(logging.INFO)
formatter = logging.Formatter(log_format)
fh.setFormatter(formatter)
Log.addHandler(fh)


@pytest.mark.webtestX
def test_TC_GIATJA_048():
    OpKemandirian(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login Operator')

@pytest.mark.webtestX
def test_TC_GIATJA_049():
    driver.implicitly_wait(60)
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Operator mengakses halaman Laporan Produk')

@pytest.mark.webtestX
def test_TC_GIATJA_050():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Kegiatan Kerja')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Kegiatan Kerja')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Kegiatan Kerja')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Kegiatan Kerja')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Kegiatan Kerja')
     
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Kegiatan Kerja')
     
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Kegiatan Kerja')
     
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustussarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Kegiatan Kerja')
     
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Kegiatan Kerja')
     
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktobersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Kegiatan Kerja')
     
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Kegiatan Kerja')
     
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Kegiatan Kerja')

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'OK')]")))
    driver.find_element(By.XPATH, "//button[contains(.,'OK')]").click()

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(.,'Membuat Laporan Berhasil !')]")))
     
    Log.info('membuat Laporan Sarana Dan Prasaran')

    LogOut(driver)







@pytest.mark.webtest
def test_TC_GIATJA_051():
    sleep(driver)   
    KasieGiatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Setup Os')

@pytest.mark.webtest
def test_TC_GIATJA_052():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kasie mengakses halaman Laporan Pemasaran PNBPsi')

@pytest.mark.webtest
def test_TC_GIATJA_053():
    sleep(driver)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Sarana')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Sarana')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Sarana')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Sarana')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Sarana')
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Sarana')
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Sarana')
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustussarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Sarana')
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Sarana')
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktobersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Sarana')
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Sarana')
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desembersarana3").click()
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
    Log.info('Kasie membuat Laporan Sarana Dan Prasarana')
     


    LogOut(driver)



@pytest.mark.webtest
def test_TC_GIATJA_054():
    KalapasGiatja(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Login Kalapas')

@pytest.mark.webtest
def test_TC_GIATJA_055():
    sleep(driver)
    MenuLaporan(driver)
    attach(data=driver.get_screenshot_as_png())
    Log.info('Kalapas mengakses halaman Laporan Kegiatan Kerja dan Produksi')


@pytest.mark.webtest
def test_TC_GIATJA_056():
    sleep(driver)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "Aprilsarana3")))
    if TanggalSetorFaker == "01":
        driver.find_element(By.ID, "Januarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Januari Sarana')
    elif TanggalSetorFaker == "02":
        driver.find_element(By.ID, "Febuarisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Febuari Sarana')
    elif TanggalSetorFaker == "03":
        driver.find_element(By.ID, "Maretsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Maret Sarana')
    elif TanggalSetorFaker == "04":
        driver.find_element(By.ID, "Aprilsarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('April Sarana')
    elif TanggalSetorFaker == "05":
        driver.find_element(By.ID, "Meisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Mei Sarana')
    elif TanggalSetorFaker == "06":
        driver.find_element(By.ID, "Junisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juni Sarana')
    elif TanggalSetorFaker == "07":
        driver.find_element(By.ID, "Julisarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Juli Sarana')
    elif TanggalSetorFaker == "08":
        driver.find_element(By.ID, "Agustussarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Agustus Sarana')
    elif TanggalSetorFaker == "09":
        driver.find_element(By.ID, "Septembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('September Sarana')
    elif TanggalSetorFaker == "10":
        driver.find_element(By.ID, "Oktobersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Oktober Sarana')
    elif TanggalSetorFaker == "11":
        driver.find_element(By.ID, "Novembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('November Sarana')
    elif TanggalSetorFaker == "12":
        driver.find_element(By.ID, "Desembersarana3").click()
        sleep(driver)
        attach(data=driver.get_screenshot_as_png())
        Log.info('Desember Sarana')
    
    Log.info('1. Klik status pada bulan / tahun yang akan di verifikasi')

    Log.info('1. Klik status pada bulan / tahun yang akan di verifikasi')
    WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".circular")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Belum Otorisasi')]")))
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))
    time.sleep(2)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))
    
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Otorisasi')]")))
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
    
    LogOut(driver)




    
    




    
    