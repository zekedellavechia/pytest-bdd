# DOM é

from selenium.webdriver import Chrome

url = 'https:selenium.dunossauro.live/aula_04_a.html'

browser = Chrome()

browser.implicitly_wait(10)

browser.get(url)

ul = browser.find_element_by_tag_name('p')




browser.quit()