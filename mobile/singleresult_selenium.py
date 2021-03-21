from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def extract_results(url):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    a = driver.find_element_by_xpath("//*[contains(@href, 'fahrzeuge/details')]")
    print(a.get_attribute('href'))
