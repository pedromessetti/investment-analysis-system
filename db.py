import mysql.connector
import utils as c
from datetime import date

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
                fonte VARCHAR(13),
                data DATE,
                ativo VARCHAR(6),
                cotacao DECIMAL(10,2),
                p_l DECIMAL(10,2),
                p_vp DECIMAL(10,2),
                psr DECIMAL(10,2),
                div_yield DECIMAL(10,2),
                p_ativo DECIMAL(10,2),
                p_cap_giro DECIMAL(10,2),
                p_ebit DECIMAL(10,2),
                p_ativo_circ DECIMAL(10,2),
                ev_ebit DECIMAL(10,2),
                ev_ebitda DECIMAL(10,2),
                mrg_ebit DECIMAL(10,2),
                mrg_liq DECIMAL(10,2),
                liq_corr DECIMAL(10,2),
                roic DECIMAL(10,2),
                roe DECIMAL(10,2),
                liq_2meses DECIMAL(10,2),
                patrim_liq DECIMAL(10,2),
                div_bruta_patrim DECIMAL(10,2),
                cresc_rec_5anos DECIMAL(10,2)
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


    def insert_data(self, table, csv_file):
        connection = self.connect_to_mysql()
        cursor = connection.cursor()

        with open(csv_file, 'r') as file:
            csv_data = csv.DictReader(file)

            for row in csv_data:
                data = date.today()

                query = f'''
                    INSERT INTO {table} (
                        fonte, data, ativo, cotacao, p_l, p_vp, psr, div_yield, p_ativo,
                        p_cap_giro, p_ebit, p_ativo_circ, ev_ebit, ev_ebitda, mrg_ebit,
                        mrg_liq, liq_corr, roic, roe, liq_2meses, patrim_liq,
                        div_bruta_patrim, cresc_rec_5anos
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    )
                '''

                values = (
                    csv_file.split('.')[0],
                    data,
                    row['Papel'] if 'Papel' in row else row['TICKER'],
                    row['Cotação'] if 'Cotação' in row else row['PRECO'],
                    row['P/L'],
                    row['P/VP'],
                    row['PSR'],
                    row['Div.Yield'] / 100 if 'Div.Yield' in row else row['DY'] / 100,
                    row['P/Ativo'] if 'P/Ativo' in row else row['P/ATIVOS'],
                    row['P/Cap.Giro'] if 'P/Cap.Giro' in row else row['P/CAP. GIRO'],
                    row['P/EBIT'] if 'P/EBIT' in row else row['P/EBIT'],
                    row['P/Ativ Circ.Liq'] if 'P/Ativ Circ.Liq' in row else row['P. AT CIR. LIQ.'],
                    row['EV/EBIT'] if 'EV/EBIT' in row else row['EV/EBIT'],
                    row['EV/EBITDA'] if 'EV/EBITDA' in row else row['EV/EBITDA'],
                    row['Mrg Ebit'] / 100 if 'Mrg Ebit' in row else row['MARG. LIQUIDA'] / 100,
                    row['Mrg. Líq.'] / 100 if 'Mrg. Líq.' in row else row['Margem Líquida'] / 100,
                    row['Liq. Corr.'],
                    row['ROIC'] / 100 if 'ROIC' in row else row['ROInvC'] / 100,
                    row['ROE'],
                    row['Liq.2meses'],
                    row['Patrim. Líq'],
                    row['Dív.Brut/ Patrim.'] if 'Dív.Brut/ Patrim.' in row else row['DIV. LIQ. / PATRI.'],
                    row['Cresc. Rec.5a'] / 100 if 'Cresc. Rec.5a' in row else row['CAGR RECEITAS 5 ANOS'] / 100
                )

                try:
                    cursor.execute(query, values)
                except mysql.connector.Error as error:
                    print(f"Failed to insert data: {error}")

        connection.commit()
        cursor.close()
        connection.close()
