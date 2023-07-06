import mysql.connector


def create_database(host, user, password, database):
    print(f"Connecting to MySQL server at '{host}'")
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )
    except mysql.connector.Error as error:
        print(f"Failed to connect to MySQL: {error}")
        exit(1)
    
    cursor = connection.cursor()
    
    cursor.execute(f"SHOW DATABASES LIKE '{database}'")
    result = cursor.fetchone()

    if result:
        print(f"Database '{database}' already exists")
    else:
        try:
            cursor.execute(f"CREATE DATABASE {database}")
            print(f"Database '{database}' sucessfully created")
        except mysql.connector.Error as error:
            print(f"Failed to create database: {error}")
            exit(1)
    
    cursor.close()
    connection.close()
