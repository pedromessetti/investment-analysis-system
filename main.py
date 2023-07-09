from scraper import Scraper 
from user import User
import var as v
import utils


if __name__ == '__main__':
    if input('Do you want to run the scraper? (y/n): ').lower() == 'y':
        print(f'\n{v.OKBLUE}Starting scraping ...{v.ENDC}\n')
        utils.handle_csv_dir()

        for source in v.sources:
            Scraper(source['url'], source['file_name']).run(source['type'])

    if input('\nDo you want to run the database? (y/n): ').lower() == 'y':
        utils.clear_terminal()
        print(f'\n{v.OKBLUE}Connecting to database ...{v.ENDC}')
        User()
    else:
        utils.exit_program()
