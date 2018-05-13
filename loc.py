from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome('/Program Files/chromedriver')
driver.get('https://www.google.com')

search=driver.find_element_by_css_selector('#lst-ib').send_keys("facebook")
driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').send_keys(Keys.ENTER)#.click()
time.sleep(2)