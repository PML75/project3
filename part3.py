import mysql.connector

class SampleDb:
    def __init__(self, connection):
        self.connection = connection

    def display_specific_record(self, connection, table_name, primary_key_column, record_id):
        cursor = connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM {table_name} WHERE {primary_key_column} = %s;", (record_id,))
            row = cursor.fetchone()

            if row:
                print("Specific Record: ", row)
            else:
                print("Record not found for provided attribute")
        except Exception as e:
            print("Error executing SQL query:", e)

    def display_all_records(self, table_name):
        cursor = self.connection.cursor()

        cursor.execute(f"SELECT * FROM {table_name};")

        rows = cursor.fetchall()
        if len(rows) > 0:
            print(f"\nAll records from '{table_name}':")
            for row in rows:
                print(row)
        else:
            print(f"No records found in '{table_name}'")

    def retrieve_artworks_sorted_by_style(self):
        try:
            connection = create_connection()
            cursor = connection.cursor()

            query = "SELECT * FROM ArtWork ORDER BY Type;"
            cursor.execute(query)
            rows = cursor.fetchall()

            if len(rows) > 0:
                print("Artwork report sorted by art style:")
                for row in rows:
                    print(row)
            else:
                print("No records found in 'ArtWork' table")

        except mysql.connector.Error as e:
            print(f"Error retrieving data: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

def create_connection():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Phuiscool1",
            database="artgallerydb"
        )
        return con
    except mysql.connector.Error as e:
        print(e)

