'''
This is the main program that retrieve and process the data, and optimize route for the user's travel plan.
Author: Yixiao Zhu, Xin Sun
'''
from data_process_next.get_facilities_list import get_sorted_unique_facilities
from data_process_next.get_park_utility_list import get_selected_park_indices, get_park_utility_list
from data_processing.grab_data import grab_data
from data_processing.clean_data import clean_dataframe
from data_processing.output_processed_data import output_processed_data
import pandas as pd
from view.user_interface import display_facility_menu, get_selected_facilities, display_max_parks_per_day_menu

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
        processed_data = output_processed_data(cleaned_parks, cleaned_facilities)
        
        # [TEMPORARY] output the list of parks info into a txt file for testing
        # with open("testing_output.txt", "w") as f:
        #     for park in list_of_parks_info:
        #         f.write(str(park) + "\n")
        sorted_facilities_list = get_sorted_unique_facilities(processed_data)
        parks_per_day = display_max_parks_per_day_menu();
        display_facility_menu(sorted_facilities_list)
        selected_facilities = get_selected_facilities()
        index_data = get_selected_park_indices(sorted_facilities_list, selected_facilities, processed_data)
        park_utility_list = get_park_utility_list(processed_data)

        filtered_parks = [park_utility_list[index] for index in index_data]

        print(parks_per_day)
        print(filtered_parks)
        # parks_with_selected_facilities = get_parks_by_facilities(processed_data, selected_facilities)
        #
        # display_selected_parks(parks_with_selected_facilities)


    except Exception as e:
        print(e)

main()