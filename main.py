from part3 import SampleDb, create_connection

# Function to display the menu options
def display_menu():
    print("Options:")
    print("1. Display Specific Record")
    print("2. Display All Records")
    print("3. Display Sorted by Style")
    print("4. Quit")
    choice = int(input("Enter your choice (1-4): "))
    return choice

# Main function to execute the program
def main():
    try:
        # Establish a database connection
        connection = create_connection()
        # Create an instance of the SampleDb class
        sample_db = SampleDb(connection)

        # Loop to display the menu and perform actions based on user choice
        while True:
            choice = display_menu()

            if choice == 1:
                # Provide options to select from available tables
                tables = ['Artist', 'ArtWork', 'Customer', 'ArtShows']
                print("Available tables:")
                for idx, table in enumerate(tables, start=1):
                    print(f"{idx}. {table}")

                # Prompt user to select a table
                table_choice = int(input("Enter the number corresponding to the table: "))
                selected_table = tables[table_choice - 1]  # Adjusting for 0-based index

                # Define the primary key column for each table (modify this according to your table structure)
                primary_key_columns = {
                    'Artist': 'ArtistID',
                    'ArtWork': 'ArtWorkID',
                    'Customer': 'CustomerID',
                    'ArtShows': 'ArtShowID'
                }

                # Get user input for record ID
                record_id = int(input(f"Enter the ID for the record in '{selected_table}': "))

                # Display specific record based on user inputs
                sample_db.display_specific_record(connection, selected_table, primary_key_columns[selected_table],
                                                  record_id)

            elif choice == 2:
                # Display all records for each table
                for table in ['Artist', 'ArtWork', 'Customer', 'ArtShows']:
                    sample_db.display_all_records(table)

            elif choice == 3:
                # Retrieve and display artworks sorted by style
                sample_db.retrieve_artworks_sorted_by_style()

            elif choice == 4:
                print("Exiting program...")
                break  # Exit the loop and end the program

            else:
                print("Invalid choice. Please enter a valid option.")

    except Exception as e:
        print(e)

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
