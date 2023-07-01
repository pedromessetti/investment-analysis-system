# scrapers/status_invest.py

import common


def download_status_invest_csv():

    # Appropriated URL of Status Invest to scrape
    url = 'https://statusinvest.com.br/acoes/busca-avancada'

    driver , wait = common.setup_firefox_driver()

    driver.get(url)
    get_url = driver.current_url
    wait.until(common.EC.url_to_be(url))

    if get_url == url:
        button = wait.until(common.EC.visibility_of_element_located((common.By.CLASS_NAME, 'btn-main.fs-3')))
    button.click()

    # Wait for the page to load
    button = wait.until(common.EC.visibility_of_element_located((common.By.CLASS_NAME, 'btn-download.btn.btn-main-green.btn-small.waves-effect.waves-light')))
    button.click()

    # Wait for the file to be downloaded
    while True:
        files = common.os.listdir(common.os.path.expanduser('~/Downloads/'))
        csv_files = [f for f in files if f.endswith('.csv') and f.startswith('statusinvest')]
        if len(csv_files) > 0:
            break
        time.sleep(1)

    downloads_folder = common.os.path.expanduser('~/Downloads/')
    # Find the name of the downloaded CSV file in the Downloads folder
    file_name = next(filename for filename in common.os.listdir(downloads_folder) if filename.endswith('.csv') and filename.startswith('statusinvest'))

    # Move the file from Downloads folder to the current folder
    common.shutil.move(common.os.path.join(downloads_folder, file_name), 'csv/status_invest.csv')
    print('status_invest.csv successfully downloaded!')

    driver.quit()
