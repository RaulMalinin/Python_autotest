from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/alert_accept.html")
 
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = float(browser.find_element(By.ID, "input_value").text)
    
    a = math.log(abs(12*math.sin(x)))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(a)

    submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit.click()

    #str(math.In(abs(12*sin(168))))

finally:
    time.sleep(30)
    browser.quit()
