from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


class FaunaClick:
    print("request repeat time:")
    RepeatTime = input()
    if not RepeatTime.isdigit():
        Print("please input integer number only")
    IntRepeatTime = int(RepeatTime)
    driver = webdriver.Chrome('./chromedriver.exe')
    driver.get("https://faunaraara.com")
    print(driver.title)
    WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.XPATH, "//img[@class='logo']")))
    for count in range(0, IntRepeatTime):
        ClickTarget = driver.find_element(By.XPATH, "//img[@class='logo']")
        ClickTarget.click()
        time.sleep(2)
    driver.execute_script("alert('completed');")
    print("comlete repeated",str(IntRepeatTime),"times")