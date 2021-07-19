import argparse
import os
import re

import pandas

import mobile.singleresult as sr
import mobile.singleresult_selenium as srs


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
    print('Getting offer URLs...')
    # remove old results before starting anew...
    os.remove('offerurls.csv')
    currurl = args.result_URL
    pagenr = 0
    while currurl is not None:
        pagenr += 1
        print('Crawling page ' + str(pagenr))
        srs.get_offers_from_results_url(currurl)
        currurl = srs.get_next_search_url(currurl)
    print('Processing offers...')
    df = pandas.read_csv('offerurls.csv', header=None)
    print(df)
