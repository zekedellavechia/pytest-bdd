from selenium.webdriver import Firefox
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Firefox()

browser.get(url)

browser.implicitly_wait(10)

a = browser.find_element_by_tag_name('a')

for click in range(10):
    p = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'P value: {p[-1].text} click value: {click}')

    print(f'Same value: {p[-1].text == str(click)}')




browser.quit()

