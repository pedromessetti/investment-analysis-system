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
        Database.create_database(self.connection, self.database)
        Database.create_table(self.connection, self.table)
        self.connection.database = self.database
