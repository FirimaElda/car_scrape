from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
import re


def get_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver


# Returns a list of links from the result page.
def extract_results(url):
    driver = get_driver()
    driver.get(url)
    try:
        a = driver.find_elements_by_xpath("//*[contains(@href, 'fahrzeuge/details')]")
        linklist = [links.get_attribute('href') for links in a]
        return linklist
    finally:
        driver.quit()


def get_next_page_url(url):
    driver = get_driver()
    driver.get(url)
    try:
        nexturlelement = driver.find_element_by_xpath("//*[contains(text(), 'Weitere Angebote')]")
        return nexturlelement.get_attribute('data-href')
    except NoSuchElementException:
        print('No more cars in this search!')
        return None
    finally:
        driver.quit()


# Takes the URL of a car search and returns a list of prices for the offers on that search page.
def get_prices_from_results_url(url):
    driver = get_driver()
    driver.get(url)
    try:
        priceelements = driver.find_elements_by_xpath("//div[contains(@class, 'price-block')]")
        pricelist = [re.search(r'(\d*\.\d*) €', price.text) for price in priceelements]
        pricelistint = [int(re.sub(r'\.', '', pricere.group(1))) for pricere in pricelist if pricere is not None]
        print(len(pricelist))
        print(pricelist)
        print(pricelistint)
        return priceelements
    except NoSuchElementException:
        print('No price elements found!')
        return None
    finally:
        driver.quit()


# Gets a URL to a car page and returns the price of it.
def get_price_from_offer_url(url):
    driver = get_driver()
    driver.get(url)
    try:
        priceelement = driver.find_element_by_xpath("//span[@class = 'h3 rbt-prime-price']")
        print(priceelement.text)
        return priceelement.text
    except NoSuchElementException:
        print('No price element found!')
        return None
    finally:
        driver.quit()
