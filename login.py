from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
url = "https://test-qa.inlaze.com/auth/sign-in"
driver.get(url)
driver.implicitly_wait(60)

#formulario Login
email = driver.find_element(By.ID, "email")
email.send_keys("brayanmora@gmail.com")
clave = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[2]/app-password/div/input")
clave.send_keys("Prueba1320*")
login = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button")
login.click()
usuario = driver.find_element(By.XPATH, "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/div/label/div/img")
usuario.click()
time.sleep(3)
logout = driver.find_element(By.XPATH, "/html/body/app-root/app-panel-root/app-navbar/div/div[2]/div/ul/li[3]/a")
logout.click()
time.sleep(3)

driver.quit()