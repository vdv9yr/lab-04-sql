import logging
import os

import mysql.connector


# Configure logging.
logging.basicConfig(level=logging.INFO)


def get_connection():
    """Create and return a connection to the MySQL database."""
    logging.info("Connecting to database")

    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )


def get_data_by_group(value):
    """Return all rows from mock where the group column equals value."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        
        query = """
        SELECT id, `group`, last_name, email, gender, color
        FROM mock
        WHERE `group` = %s
        """

        cursor.execute(query, (value,))

        results = cursor.fetchall()

        logging.info(
            "Found %d rows where group = %s",
            len(results),
            value,
        )

        return results

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        raise

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()


def plot_counts(groupby):
    """Count rows in mock grouped by the specified column."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        allowed_columns = {
            "id",
            "group",
            "last_name",
            "email",
            "gender",
            "color",
        }

        if groupby not in allowed_columns:
            raise ValueError(f"Invalid column name: {groupby}")

        query = f"""
        SELECT `{groupby}`, COUNT(*) AS count
        FROM mock
        GROUP BY `{groupby}`
        ORDER BY count DESC
        """

        cursor.execute(query)

        results = cursor.fetchall()

        logging.info(
            "Calculated counts grouped by %s",
            groupby,
        )

        return results

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        raise

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()


def main():
    """Demonstrate the database query functions."""
    
    fluffy_rows = get_data_by_group("Fluffy")

    print("Rows where group = Fluffy:")
    for row in fluffy_rows:
        print(row)


    gender_counts = plot_counts("gender")

    print("\nCounts by gender:")
    for value, count in gender_counts:
        print(f"{value}: {count}")


if __name__ == "__main__":
    main()