import argparse
import mobile.singleresult as sr
import mobile.singleresult_selenium as srs


if __name__ == '__main__':
    # setup the arguments...
    parser = argparse.ArgumentParser()
    parser.add_argument('result_URL', help='The URL of the results of the cars to be scraped.')
    #parser.add_argument('--alpha', action='store_true')
    #parser.add_argument('--plot', action='store_true')
    #parser.add_argument('--stock', help='The symbol of the stock to get. Only necessary if alpha-switch is on.')
    args = parser.parse_args()
    carres = sr.extract_results(args.result_URL)
    print('-----------------------------------------------------')
    for car in carres:
        print(car.prettify())
        print('-----------------------------------------------------')

    print(len(carres))
    srs.extract_results(args.result_URL)
