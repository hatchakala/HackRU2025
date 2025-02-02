from db import get_database  # Import the database connection logic

def insert_lounge_data(floor, number_of_people, decibel_value=None):
    """Insert or update lounge data for a specific floor in MongoDB."""
    dbname = get_database()
    
    # Calculate the lounge IDs for the specific floor (11, 21, ..., 111 for floor 1, etc.)
    lounge_ids = [floor * 10 + i for i in range(1, 12)]  # 11, 21, ..., 111 for floor 1
    
    collection = dbname[f"floor_{floor}_lounge_data"]  # Use collection specific to the floor

    # Loop through the calculated lounge IDs and insert data
    for lounge_id in lounge_ids:
        collection.update_one(
            {"_id": lounge_id},
            {"$set": {"numberOfPeople": number_of_people, "decibelValue": decibel_value}},
            upsert=True  # Creates a new document if it doesn't exist
        )
        print(f"Floor {floor} - Data inserted/updated: LoungeID={lounge_id}, People={number_of_people}, Decibel={decibel_value}")




def get_lounge_data_for_floor(floor):
    """Fetch all lounge data for a specific floor from MongoDB."""
    dbname = get_database()
    collection = dbname[f"floor_{floor}_lounge_data"]  # Use collection specific to the floor
    
    lounges = list(collection.find({}, {"_id": 1}))  # Fetch all lounges and include _id (lounge_id)
    return lounges


def get_lounge_data_for_all_floors():
    """Fetch all lounge data across all floors."""
    dbname = get_database()
    all_floors_data = {}
    
    for floor in range(1, 5):  # For floors 1 to 4
        collection = dbname[f"floor_{floor}_lounge_data"]
        lounges = list(collection.find({}, {"_id": 0}))  # Fetch all lounges without the _id field
        all_floors_data[floor] = lounges
    
    return all_floors_data


# Example usage:
if __name__ == "__main__":
    # Insert data for each lounge on floor 1, floor 2, floor 3, and floor 4
    for floor in range(1, 5):
        for lounge_id in range(floor*10 + 1, floor*10 + 12):  # Example lounge ids 11, 21, ..., 111 for floor 1
            insert_lounge_data(floor, lounge_id, 5, 50)  # Insert data for each lounge, here 5 people and 50 decibel value
    
    # Get data for floor 1
    floor_1_data = get_lounge_data_for_floor(1)
    print("Floor 1 Data:", floor_1_data)

    # Get all lounge data for all floors
    all_floors_data = get_lounge_data_for_all_floors()
    print("All Floors Data:", all_floors_data)