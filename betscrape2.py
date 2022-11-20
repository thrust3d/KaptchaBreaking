from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
web = 'https://www.psk.hr/oklade/tenis'
path = '/home/atom/Downloads/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(web)
time.sleep(3) #add implicit wait, if necessary
accept = driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div[1]/div[2]')
time.sleep(2)
accept.click()
driver. execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver. execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
main2 = driver.find_elements(By.CLASS_NAME, "event-link js-event-link")
l = []
print(main2)