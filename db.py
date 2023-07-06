import mysql.connector
import utils as c

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def connect_to_mysql(host, user, password):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
            print("Connected to MySQL")
            return connection
        except mysql.connector.Error as error:
            print(f"{c.CROSSMARK}Failed: {error}{c.ENDC}")
            exit(1)

    def connect_to_database(connection, database):
        try:
            connection.database = database
            print(f"Connected to '{database}' database")
        except mysql.connector.Error as error:
            print(f"{c.CROSSMARK}Failed to connect to database '{database}': {error}{c.ENDC}")
            exit(1)

    def create_database(connection, database):
        cursor = connection.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{database}'")
        result = cursor.fetchone()

        if not result:
            try:
                cursor.execute(f"CREATE DATABASE {database}")
                print(f"{c.CHECKMARK}'{database}' Database created{c.ENDC}")
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to create database: {error}{c.ENDC}")
                exit(1)

        cursor.close()

    def create_table(connection, table):
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table}'")
        result = cursor.fetchone()

        if not result:
            try:
                cursor.execute(f"CREATE TABLE {table} (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), price VARCHAR(255), image VARCHAR(255), url VARCHAR(255))")
                print(f"Table '{table}' successfully created")
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to create table: {error}{c.ENDC}")
                exit(1)

        cursor.close()
