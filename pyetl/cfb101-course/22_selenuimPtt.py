from selenium.webdriver import Chrome

url = 'https://www.ptt.cc/bbs/index.html'
driver = Chrome('./chromedriver')

driver.get(url)

driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()

cookies = driver.get_cookies()
print(cookies)

driver.close()