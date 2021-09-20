from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
from Pass import username,password

PATH = 'C:\Program Files (x86)\chromedriver_win32\chromedriver' #Simpan chromedriver disini

driver = webdriver.Chrome(PATH)
driver.get('https://ilmu.upnjatim.ac.id/')

driver.find_element_by_class_name('login')\
    .click()
driver.find_element_by_link_text('Pengguna Lain (Non CAS)')\
    .click()
driver.find_element_by_name('username')\
    .send_keys(username)
driver.find_element_by_name('password')\
    .send_keys(password)
driver.find_element_by_id('loginbtn')\
    .click()