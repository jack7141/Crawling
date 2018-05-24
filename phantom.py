from selenium import webdriver
browser=webdriver.PhantomJS('C:\\Users\\황창호\\crawling\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')#설정주의해주고
browser.get("https://www.google.com/")
browser.implicitly_wait(3)

search=browser.find_element_by_css_selector('#lst-ib').send_keys("facebook")
# pw = browser.find_element_by_id('pw').send_keys('dlqms1004')
# button=browser.find_element_by_css_selector('input.btn_global[type=submit]')
# button.submit()
browser.save_screenshot("7.png")#png를 붙여야지 옳바르게 작동한다~
browser.quit()
