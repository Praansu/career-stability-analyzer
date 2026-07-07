import pandas as pd
import os

# This script is responsible for getting our "ingredients" (the data) 
# from the internet so we have something real to work with.

def fetch_valid_data():
    """
    Downloads real-world data about college majors from the web.
    """
    # This is a public URL from FiveThirtyEight that contains data on 170+ college majors
    url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/all-ages.csv"
    
    # We'll store everything in a folder called 'data'
    data_dir = "data"
    file_path = os.path.join(data_dir, "college_majors_data.csv")
    
    # If the 'data' folder doesn't exist yet, we'll create it here
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"--- Just created a '{data_dir}' folder to keep things organized ---")

    print(f"--- Fetching fresh data from the web (this might take a second)... ---")
    
    try:
        # Pandas can read files directly from a URL! Pretty cool, right?
        df = pd.read_csv(url)
        
        # We save it to your computer so the project works even if you're offline later
        df.to_csv(file_path, index=False)
        print(f"--- Success! Data saved to: {file_path} ---")
        return file_path
        
    except Exception as e:
        # In case the internet is down or the link changes
        print(f"--- Oops! Something went wrong while downloading: {e} ---")
        return None

if __name__ == "__main__":
    fetch_valid_data()
