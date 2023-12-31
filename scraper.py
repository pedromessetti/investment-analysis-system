from bs4 import BeautifulSoup
from datetime import date
import var as v
import requests
import shutil
import csv


class Scraper:
    def __init__(self, url, file_name):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        self.file_name = file_name
        try:
            self.response = requests.get(self.url, headers=self.headers)
        except requests.exceptions.ConnectionError as error:
            print(f'{v.CROSSMARK}{self.file_name}\nError: {v.ENDC}{error}')

    
    def run(self, type):
        if type == 'download':
            self.download_csv()
        if type == 'generate':
            self.generate_csv()


    def generate_csv(self):
        try:
            if self.response.status_code == 200:
                soup = BeautifulSoup(self.response.content, 'html.parser')

                with open(self.file_name, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    for tr in soup.find_all('tr'):
                        data = []
                        for th in tr.find_all('th'):
                            data.append(th.text.strip().lower().replace('.',' ').replace(' ', '_').replace('/', '_').replace('preço', 'p'))
                        if data:
                            writer.writerow(data)
                            continue
                        data = [td.text.strip().replace('%', '').replace('.', '').replace(',', '.').replace('NA', '0') for td in tr.find_all('td')]
                        try:
                            writer.writerow([float(val) if val else None for val in data])
                        except ValueError:
                            writer.writerow(data)

                if self.file_name == f'InvestSite_{date.today()}.csv':
                    with open(self.file_name, 'r') as csv_file:
                        reader = csv.reader(csv_file)
                        rows = list(reader)[6:]

                    with open(self.file_name, 'w', newline='') as csv_file:
                        writer = csv.writer(csv_file)
                        writer.writerows(rows)

                shutil.move(self.file_name, 'csv/' + self.file_name)
                print(f'{v.CHECKMARK}{self.file_name}{v.ENDC}')
            else:
                print(f'{v.CROSSMARK}{self.file_name}\nError: Response Status Code {v.BOLD}{self.response.status_code}{v.ENDC}')
        except Exception as error:
            print(f'{v.CROSSMARK}{self.file_name}\nError: {v.ENDC}{error}')
            if input("Press Enter to continue..."):
                pass


    def download_csv(self):
        try:
            if self.response.status_code == 200:
                with open(self.file_name, 'wb') as csv_file:
                    csv_file.write(self.response.content)

                with open(self.file_name, 'r') as csv_file:
                    reader = csv.reader(csv_file, delimiter=';')
                    modified_rows = []
                    for i, row in enumerate(reader):
                        if i == 0:
                            modified_rows.append([cell.strip().lower().replace('.', '').replace(' ', '_').replace('/', '_') for cell in row])
                        else:
                            modified_rows.append([cell.replace('.', '').replace(',', '.') if cell else '0' for cell in row])

                with open(self.file_name, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(modified_rows)

                shutil.move(self.file_name, 'csv/' + self.file_name)
                print(f'{v.CHECKMARK}{self.file_name}{v.ENDC}')
            else:
                print(f'{v.CROSSMARK}{self.file_name}\nError: Response Status Code {v.BOLD}{self.response.status_code}{v.ENDC}')
        except Exception as error:
            print(f'{v.CROSSMARK}{self.file_name}\nError: {v.ENDC}{error}')
