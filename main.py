# main.py

from scrapers.fundamentus import generate_fundamentus_csv
from scrapers.invest_site import download_xlsx, convert_to_csv
from scrapers.status_invest import download_status_invest_csv
from utils import clean_logs_and_cache
import multiprocessing


if __name__ == '__main__':
    # Create a process for downloading the CSV file
    p = multiprocessing.Process(target=download_status_invest_csv)
    p.start()

    # Download the Excel file in the parent process
    download_xlsx()

    # Wait for the child process to finish
    p.join()

    # Convert the Excel file to CSV
    convert_to_csv()

    # Clean logs and cache
    clean_logs_and_cache()
