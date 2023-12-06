from part3 import SampleDb, create_connection


def display_menu():
    print("Options:")
    print("1. Display Specific Record")
    print("2. Display All Records")
    print("3. Display Sorted by Style")
    print("4. Quit")
    choice = int(input("Enter your choice (1-4): "))
    return choice


def main():
    try:
        connection = create_connection()
        sample_db = SampleDb(connection)

        while True:
            choice = display_menu()

            if choice == 1:
                tables = ['Artist', 'ArtWork', 'Customer', 'ArtShows']
                print("Available tables:")
                for idx, table in enumerate(tables, start=1):
                    print(f"{idx}. {table}")

                table_choice = int(input("Enter the number corresponding to the table: "))
                selected_table = tables[table_choice - 1]

                primary_key_columns = {
                    'Artist': 'ArtistID',
                    'ArtWork': 'ArtWorkID',
                    'Customer': 'CustomerID',
                    'ArtShows': 'ArtShowID'
                }

                record_id = int(input(f"Enter the ID for the record in '{selected_table}': "))

                sample_db.display_specific_record(connection, selected_table, primary_key_columns[selected_table],
                                                  record_id)

            elif choice == 2:
                for table in ['Artist', 'ArtWork', 'Customer', 'ArtShows']:
                    sample_db.display_all_records(table)

            elif choice == 3:
                sample_db.retrieve_artworks_sorted_by_style()

            elif choice == 4:
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please enter a valid option.")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
