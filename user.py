from db import Database

class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.host = 'localhost'
        self.database = 'investment_analysis'
        self.connection = Database.connect_to_mysql(self.host, self.user, self.password)
        Database.create_database(self.connection, self.database)
        Database.connect_to_database(self.connection, self.database)
        self.connection.database = self.database
