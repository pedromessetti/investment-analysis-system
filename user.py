from db import Database
import utils as c

class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.host = 'localhost'
        self.database = 'investment_analysis'
        self.connection = Database.connect_to_mysql(self.host, self.user, self.password)
        Database.connect_to_database(self.connection, self.database)
        self.table = input(f"Table name: {c.BOLD}")
        self.db = Database(self.host, self.user, self.password, self.database)
        self.db.create_table(self.table)
        self.db.insert_data(self.table, 'fundamentus.csv')
        self.db.insert_data(self.table, 'status_invest.csv')
        self.db.insert_data(self.table, 'invest_site.csv')

        print("Data inserted successfully.")