from src import *
from fakeoption import *
from Register_Pendampingan import SimpanRegister
from indikator import *

# init driver by os
@mark.fixture_pembimbingan
def testconfigandlogin():
	Log.info('Konfigurasi agar berjalan di setiap sistem operasi (mac dan Windos)')
	global driver, pathData
	driver = initDriver()
	pathData = loadDataPath()
	Log.info('Memasukan User name dan Password di halaman Login')
	bapasbdg(driver) #Operator BPS

@mark.fixture_pembimbingan
def testpembimbingan():
  Log.info('Menambah Data Register Pendampingan')
  driver.get('http://kumbang.torche.id:32400/bapas/pendaftaran/register-pembimbingan')
  WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.ID, 'buttonCari')))
  turu(driver)

@mark.fixture_pembimbingan
def testdatapembimbingan():
  A = wb['Register Pembimbingan']
  pembimbingan = 2
  while pembimbingan <= len(A['A']):
    UPTObimbingan               = A['A'+str(pembimbingan)].value
    NoregNamabimbingan          = A['B'+str(pembimbingan)].value
    jenisKlienPembimbingan      = A['C'+str(pembimbingan)].value
    DasarPembimbingan           = fake.random_element(elements=('Putusan Pengadilan', 'Penetapan Pengadilan','SK Menkumham','SK Kabapas'))
    TglAwalBimbingan            = tanggal_sebelumnya.strftime('%d/%m/%Y')
    TglAkhirBimbignan           = tgl_sebulan_berikutnya.strftime('%d/%m/%Y')
    CariPetugasPembimbingan     = A['H'+str(pembimbingan)].value
    driver.find_element(By.ID, 'createButton').click()
    try:
      Log.info('Memilih UPT')
      time.sleep(3)
      elem = driver.find_element(By. ID, "upt")
      elem.click()
      elem.send_keys(UPTObimbingan)
      WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'upt0')))
      klikupt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//li[contains(.,'"+UPTObimbingan+"')]")))
      klikupt.click()

      Log.info('Memilih WBP')
      elem1 = driver.find_element(By. ID, "nama")
      elem1.click()
      elem1.send_keys(NoregNamabimbingan)
      awal = time.time()
      # driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='"+NoregNamabimbingan+"']/parent::*").click()
      wbpnya = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "nama0")))
      akhir = time.time()
      lamatunggu = awal - akhir
      Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(lamatunggu)))
      wbpnya.click()

      Log.info('Melakukan pencarian data WBP, menunggu loading detail WBP')
      time.sleep(2)
      driver.find_element(By.ID, 'findButton').click()
      kop = time.time()
      WebDriverWait(driver, 35).until(EC.visibility_of_element_located((By.XPATH, "//td[@class='el-descriptions__cell el-descriptions__content is-bordered-content' and text()='"+NoregNamabimbingan+"']")))
      kip = time.time()
      tungguload = kop - kip
      Log.info("Waktu yang dibutuhkan: {:.2f} detik".format(abs(tungguload)))

      Log.info('memelihi Jenis Klien')
      jereg = driver.find_element(By.ID, 'dropdownJenisRegistrasi')
      jereg.click()
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "jenisRegistrasi0")))
      jereg.send_keys(jenisKlienPembimbingan)
      driver.find_element(By.XPATH, "//li[contains(.,'"+jenisKlienPembimbingan+"')]").click()

      Log.info('memelihi Dasar Pembimbingan')
      daspembim = driver.find_element(By.ID, 'dropdownDasarPembimbingan')
      daspembim.click()
      daspembim.send_keys(DasarPembimbingan)
      daspembim.send_keys(Keys.DOWN)
      daspembim.send_keys(Keys.ENTER)

      Log.info('Tgl awal Bimbingan')
      tglaawal = driver.find_element(By. ID, "tglAwalBimbingan")
      tglaawal.click()
      tglaawal.send_keys(TglAwalBimbingan)
      tglaawal.send_keys(Keys.ENTER)

      Log.info('Tgl Akir nimbingan')
      tglakhir = driver.find_element(By. ID, "tglAkhirBimbingan")
      tglakhir.click()
      tglakhir.send_keys(TglAkhirBimbignan)
      tglakhir.send_keys(Keys.ENTER)

      Log.info('memelihi Petugas Pembimbingan')
      pk = driver.find_element(By.ID, 'searchPetugasPenerima')
      pk.click()
      turu(driver)
      pk.send_keys(CariPetugasPembimbingan)
      turu(driver)
      pknama = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "searchPetugasPenerima0")))
      pknama.click()

      Log.info('Upload SuratDasarPembimbingan')
      driver.find_element(By.ID, 'pilihFoto0').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'FILEPDF'))
      pyautogui.press('enter')

      driver.find_element(By.ID, 'tambah_foto').click()
      namafotonya = driver.find_element(By.ID, 'namaFoto5')
      namafotonya.click()
      namafotonya.send_keys(Keys.DOWN)
      namafotonya.send_keys(Keys.ENTER)


      driver.find_element(By.ID, 'dropdownSurat').click()
      WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.ID, 'surat0')))
      driver.find_element(By.ID, 'dropdownSurat').send_keys(AsalsuratPembimbingan)
      driver.find_element(By.XPATH, "//li[contains(.,'"+ AsalsuratPembimbingan+"')]").click()
      Log.info('input Nomer surat')
      driver.find_element(By.ID, "noSurat0").send_keys("NO",Nosurat1Pembimbingan)
      Log.info('pilih tanggal surat')
      tglsuratpernth = driver.find_element(By.ID, "TglSurat0")
      tglsuratpernth.send_keys(tglsuratPembimbingan)
      tglsuratpernth.send_keys(Keys.ENTER)
      Log.info('input Perihal surat')
      driver.find_element(By.ID, 'keterangann0').send_keys("KeteranganNO",Nosurat1Pembimbingan)

      Log.info('Upload SuratPengantarPenyerahan')
      driver.find_element(By.ID, 'pilihFoto1').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'FILEPDF'))
      pyautogui.press('enter')

      Log.info('Upload SuratPengantarPenyerahan')
      driver.find_element(By.ID, 'pilihFoto2').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'FILEPDF'))
      pyautogui.press('enter')

      Log.info('Upload SuratPengantarPenyerahan')
      driver.find_element(By.ID, 'pilihFoto3').click()
      time.sleep(3)
      pyautogui.write(environ.get(r'FILEPDF'))
      pyautogui.press('enter')


      Log.info('deskripsi SuratPengantarPenyerahan')
      driver.find_element(By.ID, "noSurat1").send_keys("NO",Nosurat1Pembimbingan)
      ltg1 = driver.find_element(By.ID, "TglSurat1")
      ltg1.send_keys(tglsuratPembimbingan)
      ltg1.send_keys(Keys.ENTER)
      driver.find_element(By.ID, 'keterangann1').send_keys("KeteranganNO",Nosurat1Pembimbingan)

      driver.find_element(By.ID, "noSurat2").send_keys("NO",Nosurat1Pembimbingan)
      ltg2 = driver.find_element(By.ID, "TglSurat2")
      ltg2.send_keys(tglsuratPembimbingan)
      ltg2.send_keys(Keys.ENTER)
      driver.find_element(By.ID, 'keterangann2').send_keys("KeteranganNO",Nosurat1Pembimbingan)

      driver.find_element(By.ID, "noSurat3").send_keys("NO",Nosurat1Pembimbingan)
      ltg3 = driver.find_element(By.ID, "TglSurat3")
      ltg3.send_keys(tglsuratPembimbingan)
      ltg3.send_keys(Keys.ENTER)
      driver.find_element(By.ID, 'keterangann3').send_keys("KeteranganNO",Nosurat1Pembimbingan)

      SimpanRegister(driver)
    except NoSuchElementException:
      driver.close()
      driver.quit()
      Log.info('Tidak ada elemen tersedia')  
    pembimbingan = pembimbingan + 1
  print ('Beres registerlitmas')
    


