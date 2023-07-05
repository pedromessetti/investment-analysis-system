<h1 align="center">
    Investiment Analysis System
</h1>

## Index
- [Index](#index)
- [Description](#description)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)
- [Learnings](#learnings)
- [Contributing](#contributing)
- [Author](#author)

## Description

<p>
The project is a Python application that scrapes stock data from various financial websites and generates CSV files for analysis. It collects data from the following sources:

- [Fundamentus](https://www.fundamentus.com.br/resultado.php): Scrapes fundamental stock data from Fundamentus and generates a `fundamentus.csv` file.
- [Status Invest](https://statusinvest.com.br/): Downloads a CSV file from Status Invest containing advanced search results and saves it as `status_invest.csv`.
- [Invest Site](https://www.investsite.com.br/): Downloads an XLSX file from Invest Site containing stock selection data and convert it to `invest_site.csv`.    
</p>

## Configuration

Before running the application, ensure that you have the following prerequisites installed:

- Python 3.10
- BeautifulSoup
- Requests
- Shutil

You can install the dependencies by running the following command:

    pip3 install bs4 requests shutil

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