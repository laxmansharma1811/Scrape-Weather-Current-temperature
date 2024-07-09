from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.accuweather.com/en/np/kathmandu/241809/weather-forecast/241809")

time.sleep(5)

try:
    temp_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "temp"))
    )
    current_temp = temp_element.text
    print(f'Current Temperature: {current_temp}')
except Exception as e:
    print(f'Error: {e}')
finally:
    driver.quit()