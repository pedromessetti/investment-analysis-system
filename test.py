import pandas as pandas
from scraper import Scraper

if not os.path.exists('csv'):
    os.mkdir('csv')

Scraper(fundamentus_url, 'fundamenus.csv').generate_csv()
Scraper(status_invest_url, 'status_invest.csv').download_csv()

df1 = pandas.read_csv('fundamentus.csv')
df2 = pandas.read_csv('status_invest.csv')

combined_csv = pandas.concat([df1, df2], ignore_index=True)