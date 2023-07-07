import shutil
import csv
import requests
import utils as c
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url, file_name):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        self.file_name = file_name
        self.response = requests.get(self.url, headers=self.headers)


    def generate_csv(self):
        if self.response.status_code == 200:
            soup = BeautifulSoup(self.response.content, 'html.parser')
            
            with open(self.file_name, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for tr in soup.find_all('tr'):
                    data = []
                    for th in tr.find_all('th'):
                        data.append(th.text.strip().upper())
                    if data:
                        writer.writerow(data)
                        continue
                    data = [td.text.strip().replace('%', '').replace('.', '').replace(',', '.').replace('NA', '0') for td in tr.find_all('td')]
                    try:
                        writer.writerow([float(val) if val else None for val in data])
                    except ValueError:
                        writer.writerow(data)

            if self.file_name == 'invest_site.csv':
                with open(self.file_name, 'r') as csv_file:
                    reader = csv.reader(csv_file)
                    rows = list(reader)[6:]
                
                with open(self.file_name, 'w', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerows(rows)
            
            shutil.move(self.file_name, 'csv/' + self.file_name)
            print(f'{c.CHECKMARK}{self.file_name}{c.ENDC}')
        else:
            print(f'{c.CROSSMARK}Error: Response Status Code {c.BOLD}{self.response.status_code}{ENDC}')


    def download_csv(self):
        if self.response.status_code == 200:
            with open(self.file_name, 'wb') as csv_file:
                csv_file.write(self.response.content)

            with open(self.file_name, 'r') as csv_file:
                reader = csv.reader(csv_file, delimiter=';')
                modified_rows = []
                for row in reader:
                    modified_rows.append([cell.replace('.', '').replace(',', '.') if cell else '0' for cell in row])

            with open(self.file_name, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(modified_rows)

            shutil.move(self.file_name, 'csv/' + self.file_name)
            print(f'{c.CHECKMARK}{self.file_name}{c.ENDC}')
        else:
            print(f'{c.CROSSMARK}Error: Response Status Code {c.BOLD}{self.response.status_code}{c.ENDC}')
