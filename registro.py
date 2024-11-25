from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "https://test-qa.inlaze.com/auth/sign-in"
driver.get(url)
driver.implicitly_wait(60)

boton_sign_up = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/span/a")
time.sleep(3)
boton_sign_up.click()
time.sleep(5)

#Formulario de registro
nombre = driver.find_element(By.ID, "full-name")
nombre.send_keys("Usuario Prueba")
email = driver.find_element(By.ID, "email")
email.send_keys("brayanmora1320@gmail.com")
contrasena = driver.find_element(By.CSS_SELECTOR, ".input.input-bordered.join-item.w-full")
contrasena.send_keys("Prueba2024*")
confirm_contrasena = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[4]/app-password/div/input")
confirm_contrasena.send_keys("Prueba2024*")
guardar = driver.find_element(By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/button")
guardar.click()
time.sleep(5)

driver.quit()



