from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/explicit_wait2.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100")
     )
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    browser.execute_script("window.scrollBy(0, 500);")
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()
    time.sleep(30)
    browser.quit()
