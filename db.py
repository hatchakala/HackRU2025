from pymongo import MongoClient # type: ignore
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://athardhik06:loungeAvail123@cluster0.h1jez.mongodb.net/"
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['lounge_data']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   

def get_database():
    """Connect to MongoDB and return the database instance."""
    CONNECTION_STRING = "mongodb+srv://athardhik06:loungeAvail123@cluster0.h1jez.mongodb.net/"
    client = MongoClient(CONNECTION_STRING)
    return client['user_lounge_info']

def insert_lounge_data(lounge_id, number_of_people, decibel_value=None):
    """Insert or update lounge data in MongoDB."""
    dbname = get_database()
    collection = dbname["lounge_data"]

    # Insert a new document or update if loungeID already exists
    collection.update_one(
        {"_id": lounge_id},
        {"$set": {"numberOfPeople": number_of_people, "decibelValue": decibel_value}},
        upsert=True  # Creates a new document if it doesn't exist
    )
    
    print(f"Data inserted/updated: LoungeID={lounge_id}, People={number_of_people}, Decibel={decibel_value}")
