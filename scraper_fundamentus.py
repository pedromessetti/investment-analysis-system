from bs4 import BeautifulSoup
import requests
import csv


def scrape_fundamentus():
    URL = 'https://www.fundamentus.com.br/resultado.php'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    fundamentus_csv_writer = csv.writer(open('fundamentus.csv', 'w'))

    for tr in soup.find_all('tr'):
        data = []

        for th in tr.find_all('th'):
            data.append(th.text)

        if data:
            fundamentus_csv_writer.writerow(data)
            continue

        for td in tr.find_all('td'):
            val = td.text.strip()
            if '%' in val:
                val = val.replace('%', '')
            if '.' in val:
                val = val.replace('.', '')
            val = val.replace(',', '.')
            data.append(val)

        if data:
            fundamentus_csv_writer.writerow(data)


def generate_stocks_names():
    URL = 'https://www.fundamentus.com.br/detalhes.php'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'}
    site = requests.get(URL, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')

    fundamentus_csv_writer = csv.writer(open('fundamentus_stocks_names.csv', 'w'))

    for tr in soup.find_all('tr'):
        data = []

        for th in tr.find_all('th'):
            data.append(th.text)

        if data:
            fundamentus_csv_writer.writerow(data)
            continue

        for td in tr.find_all('td'):
            val = td.text.strip()
            if '%' in val:
                val = val.replace('%', '')
            if '.' in val:
                val = val.replace('.', '')
            val = val.replace(',', '.')
            data.append(val)

        if data:
            fundamentus_csv_writer.writerow(data)
