<h1 align="center">
    Investiment Analysis System
</h1>

<p>
The Investment Analysis System is a Python application that collects stock data from various financial websites and generates CSV files for analysis. It uses web scraping techniques to gather data from the following sources:

- [Fundamentus](https://www.fundamentus.com.br/resultado.php): Scrapes fundamental stock data from Fundamentus and generates a `fundamentus.csv` file.
- [Status Invest](https://statusinvest.com.br/): Downloads a CSV file from Status Invest containing advanced search results and saves it as `status_invest.csv`.
- [Invest Site](https://www.investsite.com.br/): Downloads an XLSX file from Invest Site containing stock selection data and convert it to `invest_site.csv`.    
</p>

## Index
- [Index](#index)
- [Description](#description)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [License](#license)
- [Learnings](#learnings)
- [Contributing](#contributing)
- [Author](#author)

## Description

<p>
The Investment Analysis System is a Python application that helps investors gather and analyze stock data from different sources. By scraping data from Fundamentus, Status Invest, and Invest Site, it provides investors with valuable insights for making informed investment decisions.

The system consists of two main components: main.py and scraper.py. The main.py script acts as the entry point and orchestrates the scraping process for each website. It creates instances of the Scraper class defined in scraper.py and calls the appropriate methods to generate or download the CSV files.

The Scraper class encapsulates the functionality for scraping and processing the data. It uses the BeautifulSoup library to parse HTML content and extract relevant information. The generate_csv method generates CSV files by iterating over the HTML structure and writing the data to the files. The download_csv method downloads CSV or XLSX files from the websites and performs necessary modifications before saving them.
</p>


## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- Python 3.10
- BeautifulSoup
- Requests
- Shutil

You can install the dependencies by running the following command:

    pip3 install bs4 requests shutils

## Usage

To use the script, follow these steps:

1. Clone the repository:

        git clone https://github.com/pedromessetti/investment-analysis-system.git

2. `cd` to the project directory

3. `mkdir csv` to create the folder for storing the csv files

4. Run the main script:

        python3.10 main.py

This will execute the scraping functions and store the necessary CSV files in the `csv` directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Learnings

The project was developed using Python 3.10 and various libraries. Here are some learnings that I have with the following tools:

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): A library for parsing HTML and XML.
- [Requests](https://docs.python-requests.org/): A library for making HTTP requests.

## Contributing

If you encounter any issues or have suggestions for improvement, please open an issue.

## Author
| [<img src="https://avatars.githubusercontent.com/u/105685220?v=4" width=115><br><sub>Pedro Vinicius Messetti</sub>](https://github.com/pedromessetti) |
|:---------------------------------------------------------------------------------------------------------------------------------------------------: |