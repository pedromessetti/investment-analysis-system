import os
from db import Database
import utils as c
import pandas as pd
from utils import Cleaner

class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.host = 'localhost'
        self.database = 'investment_analysis'
        self.connection = Database.connect_to_mysql(self.host, self.user, self.password)
        Database.connect_to_database(self.connection, self.database)
        self.table = input(f"Table name: {c.BOLD}")
        Database.create_database(self.connection, self.database)
        Database.create_table(self.connection, self.table)
        self.connection.database = self.database
        for file in os.listdir('./csv'):
            try:
                df = pd.read_csv(f'./csv/{file}')
                df['fonte'] = file.split('_')[0]
                df['data'] = file.split('_')[1].split('.')[0]
                if file.split('_')[0] == 'Fundamentus':
                    df = Cleaner(df).fundamentus()
                    df = Cleaner(df).div()
                elif file.split('_')[0] == 'StatusInvest':
                    df = Cleaner(df).status_invest()
                    df = Cleaner(df).div()
                elif file.split('_')[0] == 'InvestSite':
                    df = Cleaner(df).invest_site()
                    df = Cleaner(df).div()
                Database.insert_data(self.connection, self.table, df)
            except pd.errors.ParserError as er:
                print(f"{c.CROSSMARK}Failed: {er}{c.ENDC}")

        if input(f'\nDo you want to delete some table? (y/n): ').lower() == 'y':
            Database.drop_table(self.connection, input(f"{c.BOLD}Table name: {c.ENDC}"))
        self.connection.close()
        print(f"{c.OKGREEN}Connection closed{c.ENDC}")
