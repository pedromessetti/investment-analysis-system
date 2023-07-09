from datetime import date
import var as v
import shutil
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def exit_program():
    shutil.rmtree('__pycache__')
    print(f"\n{v.ENDC}{v.GRAY}Quit program.{v.ENDC}")
    exit(0)


def handle_csv_dir():
    if not os.path.exists('csv'):
        os.mkdir('csv')
        print(f'{v.CHECKMARK}CSV directory created{v.ENDC}\n')
    else:
        for file in os.listdir('./csv'):
            if not file.endswith(f'_{date.today()}.csv'):
                os.remove(f'./csv/{file}')
                print(f'{v.CHECKMARK}Removed {file}{v.ENDC}')
