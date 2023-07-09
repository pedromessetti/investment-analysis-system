import mysql.connector
import prettytable
import tkinter as tk
import var as v


class Database:

    def create_table(connection):
        cursor = connection.cursor()
        table = input(f"{v.ENDC}Table name: {v.BOLD}")
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
                print(f"{v.CHECKMARK}Table '{table}' created")
                if input(f"{v.PRESSENT}"):
                    pass
            except mysql.connector.Error as error:
                print(f"{v.CROSSMARK}Failed to create table: {error}{v.ENDC}")
                if input(f"{v.PRESSENT}"):
                    pass
        else:
            print(f"{v.WARNING}Table '{table}' already exists{v.ENDC}")
            if input(f"{v.PRESSENT}"):
                pass
        cursor.close()


    def insert_data(connection, table, df):
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table}")
        columns = [column[0] for column in cursor.fetchall() if column[0] != 'id']
        df_filtered = df[columns]
        query = f'''
            INSERT INTO {table} (
                {', '.join(columns)}
            )
            VALUES (
                {', '.join(['%s' for _ in columns])}
            )
        '''
        if input(f"Insert data from {df['fonte'][0]}? (y/n): ").lower() == 'y':
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
                print(f"\n{v.CHECKMARK}Data from {df['fonte'][0]} inserted{v.ENDC}")
            except mysql.connector.Error as error:
                print(f"{v.CROSSMARK}Failed to insert data from {df['fonte'][0]}: {error}{v.ENDC}")
        cursor.close()


    def drop_table(connection):
        cursor = connection.cursor()
        table = input(f"{v.ENDC}Table name: {v.BOLD}")
        cursor.execute(f"SHOW TABLES LIKE '{table}'")
        result = cursor.fetchone()

        if result:
            try:
                cursor.execute(f"DROP TABLE {table}")
                print(f"{v.CHECKMARK}Table '{table}' deleted{v.ENDC}")
                if input(f"{v.PRESSENT}"):
                    pass
            except mysql.connector.Error as error:
                print(f"{v.CROSSMARK}Failed to drop table: {error}{v.ENDC}")
                if input(f"{v.PRESSENT}"):
                    pass
        else:
            print(f"{v.WARNING}Table '{table}' does not exist{v.ENDC}")
            if input(f"{v.PRESSENT}"):
                pass
        cursor.close()

    
    def show_tables(connection):
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()
        print(f"{v.ENDC}Tables:\n")
        for table in result:
            print(f"{v.STAR}{v.WHITE}{table[0]}{v.ENDC}")
        if input(f"{v.PRESSENT}"):
            pass
        cursor.close()


    def view_table(connection):
        cursor = connection.cursor()
        table_name = input(f"{v.ENDC}Table name: {v.BOLD}")
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor.fetchone()

        if result:
            cursor.execute(f"SELECT * FROM {table_name}")
            table = table_name
            result = cursor.fetchall()
            table = prettytable.PrettyTable()
            table.field_names = [i[0] for i in cursor.description]
            for row in result:
                table.add_row(row)

            # Create a new window
            window = tk.Tk()
            window.title(f"Table {table_name}")
            window.geometry("800x600")

            # Create a text widget with the table
            text = tk.Text(window, wrap=tk.NONE)
            text.insert(tk.END, str(table))
            text.config(state=tk.DISABLED)
            text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            # Create a scrollbar for the text widget
            scrollbar = tk.Scrollbar(window, command=text.yview)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            # Configure the text widget to use the scrollbar
            text.config(yscrollcommand=scrollbar.set)

            window.mainloop()
        else:
            print(f"{v.WARNING}Table '{table_name}' does not exist{v.ENDC}")
            if input(f"{v.PRESSENT}"):
                pass
        cursor.close()


    def describe_table(connection):
        cursor = connection.cursor()
        table = input(f"{v.ENDC}Table name: {v.BOLD}")
        cursor.execute(f"SHOW TABLES LIKE '{table}'")
        result = cursor.fetchone()

        if result:
            cursor.execute(f"DESCRIBE {table}")
            result = cursor.fetchall()
            print(f"\n|{'-'*22}|\n| {'Field':<20} |\n|{'-'*22}|")
            for row in result:
                print(f"| {row[0]:<20} |")
            print(f"|{'-'*22}|\n")
            if input(f"{v.PRESSENT}"):
                pass
        else:
            print(f"{str(v.WARNING)}Table '{table}' does not exist{str(v.ENDC)}")
            if input(f"{v.PRESSENT}"):
                pass
        cursor.close()


    def select_from_table(connection):
        cursor = connection.cursor()
        table = input(f"{v.ENDC}Table name: {v.BOLD}")
        fields = input(f"{v.ENDC}Field(s): {v.BOLD}")
        cursor.execute(f"SHOW TABLES LIKE '{table}'")
        result = cursor.fetchone()

        if result:
            try:
                cursor.execute(f"SELECT {fields} FROM {table}")
                result = cursor.fetchall()
                table = prettytable.PrettyTable()
                table.field_names = [i[0] for i in cursor.description]
                for row in result:
                    table.add_row(row)
                print(table)
            except mysql.connector.Error as error:
                print(f"{v.CROSSMARK}Failed to select from table: {error}{v.ENDC}")
            if input(f"{v.PRESSENT}"):
                pass
        else:
            print(f"{str(v.WARNING)}Table '{table}' does not exist{str(v.ENDC)}")
            if input(f"{v.PRESSENT}"):
                pass
        cursor.close()
