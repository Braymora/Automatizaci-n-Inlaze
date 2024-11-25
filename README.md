### Instrucciones para ejecutar los scripts de automatización

- Instalar Python, puede ser descargado desde [python.org](https://www.python.org/downloads/)
- En Visual Studio Code abrir una terminal para instalar selenium

bash
pip install selenium


- Descargar el WebDriver del navegador, en este caso Chrome, extrae el archivo descargado y colocar el ejecutable de `chromedriver.exe` en una carpeta de tu preferencia (por ejemplo, `C:\chromedriver`).
- Escribir el código de automatización, en este caso se hizo en el editor Visual Studio Code.
- Guardar el archivo con extensión .py, en este caso registro.py
    
    registro.py
  
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
    
    
- Login.py
    
    
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
    ```
    
- Abrir una terminal y navegar hasta la carpeta donde se guardo el script.
- En este caso
    
    bash
    cd C:\Users\braya\OneDrive\Escritorio\Automatización Inlaze
    
    
- Ejecutar los scripts utilizando python.
    
    bash
    python automation_script.py
    
    
- Ver el resultado.
