# scrapers/fundamentus.py

import csv
import shutil
import requests
from bs4 import BeautifulSoup

def generate_fundamentus_csv():

    # Appropriated URL of Fundamentus to scrape
    url = 'https://www.fundamentus.com.br/resultado.php'

    # Headers used when making the request
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    # Make the request to the website and get the content
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parsing of the HTML using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Open the CSV file for writing using a context manager
        with open('fundamentus.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Loop through each table row in the HTML content
            for tr in soup.find_all('tr'):
                data = []

                # If the table row contains table headers, append the text of each header to the data list
                for th in tr.find_all('th'):
                    data.append(th.text)

                # If the data list is not empty, write the data list to the CSV file and continue to the next table row
                if data:
                    csv_writer.writerow(data)
                    continue

                # If the table row contains table data, extract the data from each table cell and clean it
                data = [td.text.strip().replace('%', '').replace('.', '').replace(',', '.') for td in tr.find_all('td')]

                # Write the cleaned data to the CSV file
                try:
                    csv_writer.writerow([float(val) if val else None for val in data])
                except ValueError:
                    csv_writer.writerow(data)

        # Move the file to the csv directory
        shutil.move('fundamentus.csv', 'csv/fundamentus.csv')
        print('fundamentus.csv successfully generated!')
    else:
        print(f'Cannot acess Status Invest\nResponse Status Code: {response.status_code}')