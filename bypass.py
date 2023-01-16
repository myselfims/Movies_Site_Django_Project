from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



def direct_download(url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument("USER AGENT")
    driver = webdriver.Chrome(executable_path= ChromeDriverManager().install())
    d_link = ''
    while d_link == '':
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content,'html.parser')
            anchors = soup.find_all('a')
            link = ''
            for a in anchors:
                if str(a.getText()) == '✅ Fast Server (G-Drive)':
                    link = a.get('href')
                    break


            driver.get(link)
            driver.get_screenshot_as_file("screenshot.png")

            btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="landing"]/span/a')))

            btn.click()

            btn2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/article/span[2]")))

            btn2.click()
            sleep(10)

            btn3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/article/span[1]")))

            btn3.click()

            sleep(10)

            btn4 = driver.find_element(By.ID,'two_steps_btn')
            l = btn4.get_attribute('href')

            driver.get(l)

            btn5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/button")))

            btn5.click()

            sleep(10)

            input = driver.find_element(By.XPATH,'//*[@id="wi"]/div/input')
            d_link = str(input.get_attribute('value'))
        except:
            print('Trying again!')
    
    return str(input.get_attribute('value'))


link = direct_download('https://href.li/?https://blog.officialboypalak.in/?id=MjR5N2pBSUx3SGR5UXhIbG4yeVZaQmZjMXl3R1MxUm8vL3I0VzFGM3N1L3BjMGxubjZyeERCRWlkNWpvRVFDL0tIUjVhMGl3Si82REp5SGg0UThhb1QycDYzRnBuWnlRTVByWENJWkw3V28vQXQ2NVhGcW9uRGJyWnJSNzhieEh1Q1BVQzgzUmRYUEFrU2M4K25mWUxhN1hIUEcrK1I1TTlpcWtQc3FVWTQ2T2NsQ0x1TWdtSDFHaE1sUDhueDlHZUZSeW1LN2pMYkhROFA4T0tmLzVtOFQzeTkycVJLZHlCeUdFUDRUN3QvcTR2QkVKeHI5ekliNE1vQlZRdXladg==')

print(link)