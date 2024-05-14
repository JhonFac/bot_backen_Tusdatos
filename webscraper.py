# Importamos las bibliotecas necesarias
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def crear_ventana(main):
    # Opciones del navegador
    options = Options()
    if main: options.add_argument("--start-maximized")  # Maximizar la ventana del navegador
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # Configuración del WebDriver para Chrome
    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver


def ciclo_buscar(driver, id, pestana):


    search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "texto"))  # Busca el campo por su 'id'
    )
    search.send_keys(id)
    search.send_keys(Keys.RETURN)

    no_fund = True
    ciclos = False
    time_await = 10

    for i in range(1,100):
        if ciclos: break

        try:

            xpath_to_wait_for = "/html/body/app-root/div"
            # Espera hasta que el elemento esté presente
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_to_wait_for))
            )
            # Espera hasta que el elemento desaparezca
            WebDriverWait(driver, 30).until(
                EC.invisibility_of_element_located((By.XPATH, xpath_to_wait_for))
            )
        except:
            ciclos = False
            no_fund = True
            search.clear()
            break

        for i in range(1,10):
            try: 
                fecha = f'//*[@id="causas"]/mat-expansion-panel[{i}]/mat-expansion-panel-header/span[1]/div/span[1]'
                fecha = WebDriverWait(driver, time_await).until(
                    EC.presence_of_element_located((By.XPATH, fecha))
                )

                tipo = f'//*[@id="causas"]/mat-expansion-panel[{i}]/mat-expansion-panel-header/span[1]/div/span[2]'
                no_causa = f'//*[@id="causas"]/mat-expansion-panel[{i}]/mat-expansion-panel-header/span[1]/div/span[3]'
                contenido = f'//*[@id="causas"]/mat-expansion-panel[{i}]/div/div/div/article/p'
                contenido = driver.find_element(By.XPATH, contenido)

                # print("HTML del elemento:", contenido.get_attribute("innerHTML"))

                tipo = driver.find_element(By.XPATH, tipo)
                no_causa = driver.find_element(By.XPATH, no_causa)
                
                print(fecha.text)
                print(tipo.text)
                print(no_causa.text)
                print('............')
                print(contenido.text)

                if pestana: abrir_otra_pestana(driver, no_causa.text)

                print('------------')                 
                time_await = 2

            except:
                if ciclos: True
                print("Hay mas casos")
                break                 

        time_await = 10
        boton_xpath = '/html/body/app-root/app-expel-listado-coincidencias/expel-sidenav/mat-sidenav-container/mat-sidenav-content/section/section[2]/mat-paginator/div/div/div[2]/button[2]'
        boton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, boton_xpath))
        )
        # print("HTML del elemento: ", boton.get_attribute("innerHTML"))
        try:
            valor_disabled = boton.get_attribute("disabled")
            if valor_disabled == "true":
                break
        except:
                print("Hay mas paginas")
                raise

        time.sleep(1)

        js_selector = 'body > app-root > app-expel-listado-coincidencias > expel-sidenav > mat-sidenav-container > mat-sidenav-content > section > section.paginacion > mat-paginator > div > div > div.mat-mdc-paginator-range-actions > button.mat-mdc-tooltip-trigger.mat-mdc-paginator-navigation-next.mdc-icon-button.mat-mdc-icon-button.mat-unthemed.mat-mdc-button-base'
        driver.execute_script('document.querySelector("' + js_selector + '").click();')


    if no_fund:
        js_selector = 'body > app-root > app-expel-listado-coincidencias > expel-sidenav > mat-sidenav-container > mat-sidenav > div > mat-nav-list > div > button:nth-child(2)'
        driver.execute_script('document.querySelector("' + js_selector + '").click();')






def abrir_otra_pestana(driver, id):

    try:
        driver = crear_ventana(False)
        driver.get("https://procesosjudiciales.funcionjudicial.gob.ec/busqueda")
        WebDriverWait(driver, 10) 
        ciclo_buscar(driver, id, False)
    except:
        # Cerrar el controlador para evitar fugas de memoria
        driver.quit()




def main():
    driver = crear_ventana(True)
    driver.switch_to.window(driver.window_handles[0])

    try:
        # Abrimos YouTube
        driver.get("https://procesosjudiciales.funcionjudicial.gob.ec/busqueda")
        WebDriverWait(driver, 10) 
        lista = ['0968599020001','0992339411001','1791251237001','0968599020001']
        for t in lista:
            ciclo_buscar(driver, t, True)


        print('------------ todas las fechas ')



        time.sleep(5)
    finally:
        # Cerramos el controlador para evitar fugas de memoria
        driver.quit()


main()