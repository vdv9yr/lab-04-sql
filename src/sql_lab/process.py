import logging
import os

import mysql.connector
import pandas as pd



logging.basicConfig(level=logging.INFO)


def read_data(filename):
    """Read the CSV file into a pandas DataFrame."""
    logging.info("Reading data from %s", filename)

    data = pd.read_csv(filename)

    logging.info("Read %d rows from %s", len(data), filename)
    return data


def clean_data(data):
    """Remove rows with missing values and return the cleaned DataFrame."""
    logging.info("Cleaning data")

 
    cleaned_data = data.dropna()

    logging.info(
        "Removed %d rows with missing values",
        len(data) - len(cleaned_data),
    )

    return cleaned_data


def load_data(data, table):
    """Create the mock table if needed and upload the DataFrame to MySQL."""
    logging.info("Loading data into table %s", table)

  
    host = os.environ["DB_HOST"]
    database = os.environ["DB_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASSWORD"]

    connection = None
    cursor = None

    try:
 
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password,
        )

        cursor = connection.cursor()

        
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS mock (
            id BIGINT,
            `group` VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            gender VARCHAR(255),
            color VARCHAR(255)
        )
        """

        cursor.execute(create_table_sql)

        
        insert_sql = """
        INSERT INTO mock
        (id, `group`, last_name, email, gender, color)
        VALUES (%s, %s, %s, %s, %s, %s)
        """


        for _, row in data.iterrows():
            values = (
                row["id"],
                row["group"],
                row["last_name"],
                row["email"],
                row["gender"],
                row["color"],
            )

            cursor.execute(insert_sql, values)

        connection.commit()

        logging.info("Successfully uploaded %d rows", len(data))

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        raise

    finally:
    
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()


def main():
    """Read, clean, and load the mock data."""
    filename = "MOCK_DATA.csv"

    data = read_data(filename)
    cleaned_data = clean_data(data)


    load_data(cleaned_data, "mock")


if __name__ == "__main__":
    main()

    