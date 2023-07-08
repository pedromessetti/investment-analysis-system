import mysql.connector
import os
from db import Database
import utils as c
import pandas as pd
from utils import Cleaner
import getpass


class User:
    def __init__(self):
        self.user,self.password, self.connection = User.get_user()
        self.cursor = self.connection.cursor()

        self.database = 'investment_analysis'
        User.check_database(self)
        self.connection.database = self.database

        User.get_option(self)


    def get_user():
        while True:
            user = input(f"\nEnter user: ")
            password = getpass.getpass(f"Enter password: ")
            print()
            host = 'localhost'
            try:
                connection = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password
                )
                print(f"{c.OKGREEN}MySQL Connection {c.OK}{c.ENDC}\n")
                return user, password, connection
            except mysql.connector.Error as error:
                c.clear_terminal()
                print(f"{c.CROSSMARK}Failed: {error}{c.ENDC}")
                if input("\nRetry? (y/n) ").lower() != "y":
                    c.exit_program()
                else:
                    c.clear_terminal()


    def check_database(self):
        self.cursor.execute(f"SHOW DATABASES LIKE '{self.database}'")
        result = self.cursor.fetchone()

        if not result:
            try:
                self.cursor.execute(f"CREATE DATABASE {self.database}")
                print(f"{c.CHECKMARK}Database '{self.database}' created{c.ENDC}")
                if input(f"{c.ENDC}Press ENTER to continue..."):
                    pass
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to create database: {error}{c.ENDC}")
                c.exit_program()
        else:
            try:
                self.connection.database = self.database
                print(f"Database: {c.BOLD}{self.database}{c.ENDC}\n{c.OKGREEN}Connection {c.OK}{c.ENDC}\n")
                if input(f"{c.ENDC}Press ENTER to continue..."):
                    pass
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to connect to database '{self.database}': {error}{c.ENDC}")
                c.exit_program()


    def get_option(self):
        while True:
            c.clear_terminal()
            print(f"{c.MENU}")
            option = input(f"Your option: {c.BOLD}")
            if option == '0':
                self.connection.close()
                c.exit_program()
            if option == '1':
                c.clear_terminal()
                print(f"{c.OKBLUE}Create table ...\n{c.ENDC}")
                Database.create_table(self.connection)
            elif option == '2':
                c.clear_terminal()
                print(f"{c.OKBLUE}Insert into table ...\n{c.ENDC}")
                table = input(f"{c.ENDC}Table name: {c.BOLD}")
                self.cursor.execute(f"SHOW TABLES LIKE '{table}'")
                result = self.cursor.fetchone()
                if result:
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
                            Database.insert_data(self.connection, table, df)
                            input(f"{c.ENDC}Press ENTER to continue...")
                        except pd.errors.ParserError as er:
                            print(f"{c.CROSSMARK}Failed: {er}{c.ENDC}")
                else:
                    print(f"{c.CROSSMARK}Table '{table}' not found{c.ENDC}")
                    if input(f"{c.ENDC}Press ENTER to continue..."):
                        pass
            elif option == '3':
                c.clear_terminal()
                print(f"{c.OKBLUE}Remove table ...\n{c.ENDC}")
                Database.drop_table(self.connection)
            elif option == '4':
                c.clear_terminal()
                print(f"{c.OKBLUE}Show table ...\n{c.ENDC}")
                Database.show_tables(self.connection)
