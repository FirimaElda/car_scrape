import argparse
import mobile.singleresult as sr
import mobile.singleresult_selenium as srs
import re


def get_next_result_page_url(resulturl):
    nextpageattr = re.search(r'pageNumber=(\d*)', resulturl)
    print(nextpageattr)
    if nextpageattr is None:
        nextpageattr = 1
        resulturl += '&pageNumber=1'
    else:
        nextpageattr = nextpageattr.group(1)
    nextpagenr = int(nextpageattr) + 1
    print(nextpagenr)
    nextpageurl = re.sub(r'pageNumber=(\d*)', 'pageNumber=' + str(nextpagenr), resulturl)
    print(nextpageurl)


if __name__ == '__main__':
    # setup the arguments...
    parser = argparse.ArgumentParser()
    parser.add_argument('result_URL', help='The URL of the results of the cars to be scraped.')
    args = parser.parse_args()
    carres = sr.extract_results(args.result_URL)
    print('-----------------------------------------------------')
    print('Cars on first page: ' + str(len(carres)))
    print('-----------------------------------------------------')
    print('Getting prices of cars...')
    srs.get_prices_from_results_url(args.result_URL)
    if False:
        print('Building list of cars...')
        currurl = args.result_URL
        iternr = 0
        carurllist = []
        while currurl is not None:
            iternr += 1
            print('Getting cars of page ' + str(iternr) + '...')
            currcars = srs.extract_results(currurl)
            print('Number of cars on page: ' + str(len(currcars)))
            carurllist.extend(currcars)
            currurl = srs.get_next_page_url(currurl)
        print('Done building list. Got ' + str(len(carurllist)) + ' car URLs.')
        print('Working through scraped cars...')
        pricelist = [srs.get_price_from_offer_url(carurl) for carurl in carurllist]
        print(pricelist)
