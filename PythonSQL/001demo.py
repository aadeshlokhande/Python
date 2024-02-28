import pymysql

def connect_to_database():
    # Replace these values with your actual database credentials
    host = 'your_database_host'
    user = 'your_database_username'
    password = 'your_database_password'
    database_name = 'your_database_name'

    # Establish the connection
    connection = pymysql.connect(host=host, user=user, password=password, db=database_name)
    return connection

def fetch_data(connection):
    # Create a cursor object
    cursor = connection.cursor()

    # Example: SELECT query
    sql_query = "SELECT * FROM your_table_name;"
    cursor.execute(sql_query)

    # Fetch the results (assuming you want to fetch all rows)
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor
    cursor.close()

if __name__ == "__main__":
    # Connect to the database
    db_connection = connect_to_database()

    # Fetch and print data
    fetch_data(db_connection)

    # Commit and close the connection
    db_connection.commit()
    db_connection.close()
