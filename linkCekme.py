from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()

page_num = 1

driver.get("https://filmmax.org/film-arsivi/sayfa/148/")


while True:
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'movie-title')))
        links = driver.find_elements(By.CSS_SELECTOR, "a.movie-title")

        for i in range(len(links)):
            if i < len(links) and links[i].get_attribute("href").startswith("https://filmmax.org/"):
                if links[i].is_displayed() and links[i].is_enabled():
                    with open("linkler.txt", "a", encoding="utf-8") as file:
                        file.write(links[i].get_attribute("href") + "\n")
                else:
                    print(f"")

        page_num = page_num + 1
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[1]/div[3]/a[6]')))
        next_page = driver.find_element(By.XPATH, '//html/body/div/div[2]/div[1]/div[3]/a[6]')
        
       
        next_page.click()

    except NoSuchElementException:
        break

driver.quit()