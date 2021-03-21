import requests
from bs4 import BeautifulSoup
import argparse
import re


def extract_results(resulturl):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    }
    page = requests.get(resulturl, headers=headers)
    regex = re.compile('.*/fahrzeuge/details.*')

    soup = BeautifulSoup(page.content, 'html.parser')
    cars = soup.find_all('a', {'href': regex})
    return cars


if __name__ == '__main__':
    # den in raw_html gespeicherten HTML-Quelltext parsen
    html = BeautifulSoup(raw_html, 'html.parser')

    # den Inhalt des Tags mit Klasse 'car-title' extrahieren
    car_title = html.find(class_='g-row').text.strip()

    # falls es sich bei diesem Auto um einen Volkswagen Käfer handelt
    if car_title == 'Volkswagen Käfer':
        # vom Titel des Autos zum umschließenden <li>-Tag aufsteigen
        html.find_parent('li')

        # den Preis des Autos ermitteln
        car_price = html.find(class_='sales-price').text.strip()

        # den Preis des Autos ausgeben
        print(car_price)
