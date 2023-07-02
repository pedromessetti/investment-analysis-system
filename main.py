# main.py

from scrapers.fundamentus import generate_fundamentus_csv
from scrapers.invest_site import download_invest_site_xlsx, convert_xlsx_to_csv
from scrapers.status_invest import download_status_invest_csv
from utils import clean_logs_and_cache

generate_fundamentus_csv()
download_status_invest_csv()
download_invest_site_xlsx()

clean_logs_and_cache()
