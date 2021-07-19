import csv

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options


def get_driver():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    return driver


def is_there_next_page(searchurl):
    driver = get_driver()
    driver.get(searchurl)
    try:
        nexturlelement = driver.find_element_by_xpath("//span[contains(@class, 'btn btn--orange btn--s "
                                                      "next-resultitems-page')]")
        nexturlelement.get_attribute('data-href')
    except NoSuchElementException:
        print('No more cars in this search!')
        return False
    finally:
        driver.quit()
        return True


def get_next_search_url(searchurl):
    driver = get_driver()
    driver.get(searchurl)
    try:
        nexturlelement = driver.find_element_by_xpath("//span[contains(@class, 'btn btn--orange btn--s "
                                                      "next-resultitems-page')]")
        return nexturlelement.get_attribute('data-href')
    except NoSuchElementException:
        print('No more cars in this search!')
    finally:
        driver.quit()


# Returns a list of offers and writes the offer URLs to a csv file.
def get_offers_from_results_url(url):
    driver = get_driver()
    driver.get(url)
    try:
        offerelements = driver.find_elements_by_xpath("//a[contains(@class, 'link--muted no--text--decoration "
                                                      "result-item')]")
        with open('offerurls.csv', 'a', encoding='UTF8', newline='') as f:
            for offer in offerelements:
                url = offer.get_attribute('href')
                writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([url])
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
