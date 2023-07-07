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
                print(f"{c.CHECKMARK}Database: '{database}' created{c.ENDC}")
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to create database: {error}{c.ENDC}")
                exit(1)

        cursor.close()


    def create_table(connection, table):
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table}'")
        result = cursor.fetchone()
        query = f'''
            CREATE TABLE {table} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fonte CHAR(37),
                data DATE,
                ativo VARCHAR(6),
                cotacao FLOAT,
                p_l FLOAT,
                p_vp FLOAT,
                psr FLOAT,
                div_yield FLOAT,
                p_ativo FLOAT,
                p_cap_giro FLOAT,
                p_ebit FLOAT,
                p_ativo_circ FLOAT,
                ev_ebit FLOAT,
                ev_ebitda FLOAT,
                mrg_ebit FLOAT,
                mrg_liq FLOAT,
                liq_corr FLOAT,
                roic FLOAT,
                roe FLOAT,
                liq_2meses FLOAT,
                patrim_liq FLOAT,
                div_bruta_patrim FLOAT,
                cresc_rec_5anos FLOAT
            )
        '''

        if not result:
            try:
                cursor.execute(query)
                print(f"{c.CHECKMARK}Table: '{table}' created")
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to create table: {error}{c.ENDC}")
                exit(1)

        cursor.close()
