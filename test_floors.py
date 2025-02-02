from floors import insert_lounge_data, get_lounge_data_for_floor, get_lounge_data_for_all_floors

def test_insert_lounge_data():
    """Test inserting lounge data for all lounges on a floor."""
    # Insert data for floor 1
    print("Inserting data for floor 1...")
    insert_lounge_data(1, 5, 50)  # This will insert data for lounges 11, 21, ..., 111
    
    # Insert data for floor 2
    print("Inserting data for floor 2...")
    insert_lounge_data(2, 3, 60)  # This will insert data for lounges 12, 22, ..., 112
    
    # Insert data for floor 3
    print("Inserting data for floor 3...")
    insert_lounge_data(3, 7, 45)  # This will insert data for lounges 13, 23, ..., 113
    
    # Insert data for floor 4
    print("Inserting data for floor 4...")
    insert_lounge_data(4, 4, 55)  # This will insert data for lounges 14, 24, ..., 114

def test_get_lounge_data():
    """Test fetching lounge data for a specific floor and all floors."""
    # Fetch data for floor 1
    floor_1_data = get_lounge_data_for_floor(1)
    print("Floor 1 Data:", floor_1_data)

    # Fetch data for floor 2
    floor_2_data = get_lounge_data_for_floor(2)
    print("Floor 2 Data:", floor_2_data)

    # Fetch data for all floors
    all_floors_data = get_lounge_data_for_all_floors()
    print("All Floors Data:", all_floors_data)


if __name__ == "__main__":
    # Test inserting lounge data
    test_insert_lounge_data()

    # Test fetching lounge data
    test_get_lounge_data()
