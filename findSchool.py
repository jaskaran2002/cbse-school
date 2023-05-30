from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options



def findSchool(query):
    PATH = "./geckodriver"
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(executable_path=PATH, options=options)
    url = "https://cbseit.in/cbse/cbse_maps/chckmap"
    driver.get(url)

    try:
        searchField = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID, 'txtsch')))
    except:
        print("not found searchfield")
        driver.quit()
        return 'none'

    searchField = driver.find_element(By.ID, 'txtsch')
    searchField.send_keys(query)

    submitField = driver.find_element(By.ID, 'btnfind')
    submitField.send_keys(Keys.ENTER)

    try:
        answer = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID, 'rdbsource')))
    except:
        driver.quit()
        return 'none'

    answer = driver.find_element(By.ID, 'rdbsource')
    temp = answer.text
    driver.quit()
    return temp


