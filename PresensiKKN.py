from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import pywintypes
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("Presensi KKN", "Sedang melakukan presensi KKN di Simaster", duration=30)

os.chdir("C:\\Users\ivans\\Desktop\\PythonScripts")

PATH = "C:\Program Files (x86)\chromedriver.exe"
Username = "" #Isikan id ugm
Password = "" #Isikan password

driver = webdriver.Chrome(PATH)

#Login Page
driver.get("https://simaster.ugm.ac.id")
time.sleep(2)
signin = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div/div[2]/div[1]/a[1]')
signin.click()
time.sleep(1)

#SSO Login Page
ugmid = driver.find_element_by_id('username')
ugmid.send_keys(Username)
password = driver.find_element_by_id('password')
password.send_keys(Password)
password.send_keys(Keys.RETURN)
time.sleep(1)

#Presensi Harian Modal
driver.get('https://simaster.ugm.ac.id/kkn/presensi/')
time.sleep(2)
presensi = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/a')
presensi.click()
time.sleep(2)
checklist = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/form/fieldset[2]/div/label')
checklist.click()
submit = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div/form/fieldset[3]/input[3]')
submit.click()
time.sleep(3)

#Signout
driver.get('https://simaster.ugm.ac.id/ugmfw/signin/signout_proses/')
time.sleep(1)

#Close Chrome
driver.quit()