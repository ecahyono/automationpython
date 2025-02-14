import platform, sys, json
from os import environ, path
from selenium import webdriver
from pytest import mark
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

from dotenv import load_dotenv
load_dotenv()

def initDriver():
    if platform.system() == 'Darwin':
        driver = webdriver.Chrome(environ.get("CHROMEDRIVERMAC"))
    elif platform.system() == 'Windows':
        swin = Service(environ.get("CHROMEDRIVERWIN"))
        driver = webdriver.Chrome(service=swin)

    driver.get(environ.get("HOSTDO"))
    #driver.get(environ.get("HOST"))
    driver.maximize_window()
    driver.implicitly_wait(60)
    return driver

def loadDataPath():
    if platform.system() == 'Darwin':
        file = open(environ.get("MACJSONDATA"), 'r')
    elif platform.system() == 'Windows':
        file = open(environ.get("WINJSONDATA"), 'r')

    data = json.load(file)
    return data

def buttonTambah(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createButton"]')))
    driver.find_element(By.XPATH, '//*[@id="createButton"]').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="submitButton"]')))
    print('.')

def buttonSubmit(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'submitButton')))
    driver.find_element(By.ID, 'submitButton').click()
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(.,\'Berhasil Ditambahkan\')]')))
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchButton"]')))
    print('.')

def selectKategoriPegawai(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "pegawai").click()
    print('.')

def selectKategoriTamuDinas(driver):
    driver.implicitly_wait(60)
    WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inputKategori"]')))
    driver.find_element(By.XPATH, '//*[@id="inputKategori"]').click()
    driver.find_element(By.ID, "tamuDinas").click()
    print('.')

def sleep(driver):
    driver.implicitly_wait(60)
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    #time.sleep(5)
    print("-")
    print(WARNING + "===============================================================================    PRESS ENTER FOR NEXT STEP    ===============================================================================")
    time.sleep(2)
    #input("")
    print('wait . . . . . . . . . . . . . . . . . . . . . ')
    

def waituntill(driver):
    driver.implicitly_wait(60)
def quit(driver):
    time.sleep(5)
    print('.')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▓▒▒▓▒▒▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')
    print('▒▓▒▒▒▒▒▒▒▒▓▒')
    print('▒▒▓▓▓▓▓▓▓▓▒▒')
    print('▒▒▒▒▒▒▒▒▒▒▒▒')

    driver.close()
    driver.quit()

def hold(driver):
    WARNING = '\033[93m'
    print(WARNING +"================================================================= Press Enter to continue")
    input("")