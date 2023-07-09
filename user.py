from cleaner import Cleaner
from db import Database
import mysql.connector
import pandas as pd
import var as v
import getpass
import utils
import os


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
                print(f"{v.OKGREEN}MySQL Connection {v.OK}{v.ENDC}\n")
                return user, password, connection
            except mysql.connector.Error as error:
                utils.clear_terminal()
                print(f"{v.CROSSMARK}Failed: {error}{v.ENDC}")
                if input("\nRetry? (y/n) ").lower() != "y":
                    utils.exit_program()
                else:
                    utils.clear_terminal()


    def check_database(self):
        self.cursor.execute(f"SHOW DATABASES LIKE '{self.database}'")
        result = self.cursor.fetchone()

        if not result:
            try:
                self.cursor.execute(f"CREATE DATABASE {self.database}")
                print(f"{v.CHECKMARK}Database '{self.database}' created{v.ENDC}")
                if input(f"{v.PRESSENT}"):
                    pass
            except mysql.connector.Error as error:
                print(f"{v.CROSSMARK}Failed to create database: {error}{v.ENDC}")
                utils.exit_program()
        else:
            try:
                self.connection.database = self.database
                print(f"Database: {v.BOLD}{self.database}{v.ENDC}\n{v.OKGREEN}Connection {v.OK}{v.ENDC}")
                if input(f"{v.PRESSENT}"):
                    pass
            except mysql.connector.Error as error:
                print(f"{v.CROSSMARK}Failed to connect to database '{self.database}': {error}{v.ENDC}")
                utils.exit_program()


    def get_option(self):
        while True:
            utils.clear_terminal()
            print(f"{v.MENU}")
            option = input(f"Your option: {v.BOLD}")
            if option == '0':
                self.connection.close()
                utils.exit_program()
            elif option == '1':
                utils.clear_terminal()
                print(f"{v.OKBLUE}Create table ...\n{v.ENDC}")
                Database.create_table(self.connection)
            elif option == '2':
                utils.clear_terminal()
                print(f"{v.OKBLUE}Insert into ...\n{v.ENDC}")
                table = input(f"{v.ENDC}Table name: {v.BOLD}")
                self.cursor.execute(f"SHOW TABLES LIKE '{table}'")
                result = self.cursor.fetchone()
                if result:
                    for source in v.sources:
                        try:
                            df = pd.read_csv(f'./csv/{source["file_name"]}')
                            df['fonte'] = source['name']
                            df['data'] = source['file_name'].split('_')[1].split('.')[0]
                            df = Cleaner(df).clean()
                            Database.insert_data(self.connection, table, df)
                            input(f"{v.PRESSENT}")
                        except pd.errors.ParserError as er:
                            print(f"{v.CROSSMARK}Failed: {er}{v.ENDC}")
                else:
                    print(f"{v.CROSSMARK}Table '{table}' not found{v.ENDC}")
                    if input(f"{v.PRESSENT}"):
                        pass
            elif option == '3':
                utils.clear_terminal()
                print(f"{v.OKBLUE}Remove table ...\n{v.ENDC}")
                Database.drop_table(self.connection)
            elif option == '4':
                utils.clear_terminal()
                Database.show_tables(self.connection)
            elif option == '5':
                utils.clear_terminal()
                print(f"{v.OKBLUE}View table ...\n{v.ENDC}")
                Database.view_table(self.connection)
            elif option == '6':
                utils.clear_terminal()
                print(f"{v.OKBLUE}Show columns from ...\n{v.ENDC}")
                Database.describe_table(self.connection)
            elif option == '7':
                utils.clear_terminal()
                print(f"{v.OKBLUE}Select from table ...\n{v.ENDC}")
                Database.select_from_table(self.connection)
