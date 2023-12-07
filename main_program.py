'''
This is the main program that retrieve and process the data, and optimize route for the user's travel plan.
Author: Yixiao Zhu, 
'''
from data_processing.grab_data import grab_data
from data_processing.clean_data import clean_dataframe
from data_processing.output_processed_data import output_processed_data
import pandas as pd
PARKS_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
FACILITIES_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks-facilities/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
PARKS_NEEDED_INDICES = [0, 1, -1]
FACILITIES_NEEDED_INDICES = [0, 1, 2]

def main():
    try:
        # grab the csv data from the url
        parks_raw_df = grab_data(PARKS_URL)
        facilities_raw_df = grab_data(FACILITIES_URL)
        
        # clean the data
        cleaned_parks = clean_dataframe(parks_raw_df, PARKS_NEEDED_INDICES)
        cleaned_facilities = clean_dataframe(facilities_raw_df, FACILITIES_NEEDED_INDICES)

        # merge the two sets of data, eliminate duplicates and output the processed data as list
        list_of_parks_info = output_processed_data(cleaned_parks, cleaned_facilities)
        
        # [TEMPORARY] output the list of parks info into a txt file for testing
        with open("testing_output.txt", "w") as f:
            for park in list_of_parks_info:
                f.write(str(park) + "\n")
    
    except Exception as e:
        print(e)

main()