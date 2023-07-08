import mysql.connector
import utils as c
import re

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
            print(f"\n{c.OKGREEN}MySQL Connection {c.OK}{c.ENDC}\n")
            return connection
        except mysql.connector.Error as error:
            print(f"{c.CROSSMARK}Failed: {error}{c.ENDC}")
            exit(1)


    def connect_to_database(connection, database):
        try:
            connection.database = database
            print(f"Database: {c.BOLD}{database}{c.ENDC}\n{c.OKGREEN}Connection {c.OK}{c.ENDC}\n")
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
                print(f"{c.CHECKMARK}Database '{database}' created{c.ENDC}")
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
                fonte VARCHAR(12),
                data DATE,
                ativo VARCHAR(6),
                cotacao FLOAT(10,2),
                p_l FLOAT(10,2),
                p_vp FLOAT(10,2),
                psr FLOAT(10,2),
                div_yield FLOAT(10,2),
                p_ativo FLOAT(10,2),
                p_cap_giro FLOAT(10,2),
                p_ebit FLOAT(10,2),
                p_ativo_circ FLOAT(10,2),
                ev_ebit FLOAT(10,2),
                ev_ebitda FLOAT(10,2),
                mrg_ebit FLOAT(10,2),
                mrg_liq FLOAT(10,2),
                liq_corr FLOAT(10,2),
                roic FLOAT(10,2),
                roe FLOAT(10,2),
                liq_2meses FLOAT(20,2),
                patrim_liq FLOAT(20,2),
                div_bruta_patrim FLOAT(10,2),
                cresc_rec_5anos FLOAT(10,2)
            )
        '''

        if not result:
            try:
                cursor.execute(query)
                print(f"{c.CHECKMARK}Table '{table}' created")
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to create table: {error}{c.ENDC}")
                exit(1)
        else:
            print(f"{c.WARNING}Table '{table}' already exists{c.ENDC}")

        cursor.close()


    def insert_data(connection, table, df):
        cursor = connection.cursor()

        # Get the column names from the table schema, excluding 'id'
        cursor.execute(f"DESCRIBE {table}")
        columns = [column[0] for column in cursor.fetchall() if column[0] != 'id']
        # Filter the DataFrame to include only matching columns
        df_filtered = df[columns]

        query = f'''
            INSERT INTO {table} (
                {', '.join(columns)}
            )
            VALUES (
                {', '.join(['%s' for _ in columns])}
            )
        '''

        try:
            for _, row in df_filtered.iterrows():
                converted_row = []
                for value in row:
                    try:
                        numeric_value = float(value)
                        converted_row.append((f'{numeric_value:.2f}'))
                    except ValueError:
                        converted_row.append(value)
                cursor.execute(query, tuple(converted_row))
            connection.commit()
            print(f"{c.CHECKMARK}Data from {df['fonte'][0]} inserted{c.ENDC}")
        except mysql.connector.Error as error:
            print(f"{c.CROSSMARK}Failed to insert data from {df['fonte'][0]}: {error}{c.ENDC}")

    def drop_table(connection, table):
        cursor = connection.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{table}'")
        result = cursor.fetchone()

        if result:
            try:
                cursor.execute(f"DROP TABLE {table}")
                print(f"{c.CHECKMARK}Table '{table}' deleted{c.ENDC}")
            except mysql.connector.Error as error:
                print(f"{c.CROSSMARK}Failed to drop table: {error}{c.ENDC}")
                exit(1)
        else:
            print(f"{c.WARNING}Table '{table}' does not exist{c.ENDC}")

        cursor.close()