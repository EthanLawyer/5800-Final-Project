'''
Merge and process the two dataframes, and output processed data as a list.
Author: Yixiao Zhu
'''
from grab_data import *
from clean_data import *
from ParkInfo import *
import pandas as pd

COMMON_COLUMNS = ['ParkID', 'Name']
PARKID_INDEX = 0
NAME_INDEX = 1
COORDINATE_INDEX = 2
FACILITY_INDEX = 3
STARTING_INDEX = 0
ENDING_INDEX = -1

def output_processed_data(clean_park_df, clean_facilities_df):
    '''
    Function: merge and process the two dataframes, and output processed data as a list.
    Parameters:
        clean_park_df -- a dataframe, the clean dataframe of parks (3 columns: id, name, coordinates)
        clean_facilities_df -- a dataframe, the clean dataframe of facilities (3 columns: id, name, facility)
    Returns:
        processed_data -- a list of ParkInfo objects, the processed data
    Raises:
        KeyError -- if the input is not a pandas dataframe, or if required parameters are not inputted
        IndexError -- if the input is not a pandas dataframe, or if required parameters are not inputted
        TypeError -- if the input is not a pandas dataframe, or if required parameters are not inputted
        ValueError -- when inputted dataframe does not contain correct csv data
        MemoryError -- when the inputted data is too large to process
    '''
    processed_data = []

    try:
        merged_df = pd.merge(clean_park_df, clean_facilities_df, on = COMMON_COLUMNS, how = 'left').fillna("") # merge the two dataframes
        
        for i in range(len(merged_df)):

            park_id = str(merged_df.iloc[i, PARKID_INDEX])
            park_name = merged_df.iloc[i, NAME_INDEX]           
            park_facility = merged_df.iloc[i, FACILITY_INDEX]
            
            if len(processed_data) != 0 and park_name == processed_data[ENDING_INDEX][STARTING_INDEX]:
                processed_data[ENDING_INDEX][ENDING_INDEX].append(park_facility)
            else:
                park_coordinates = merged_df.iloc[i, COORDINATE_INDEX].split(', ')
                longitude = float(park_coordinates[STARTING_INDEX])
                latitude = float(park_coordinates[ENDING_INDEX])
                if park_facility == "":
                    park_facility = []
                    park = ParkInfo(park_id, park_name, longitude, latitude, park_facility)
                else:
                    park = ParkInfo(park_id, park_name, longitude, latitude, [park_facility])
                park_info_list = park.to_list()
                processed_data.append(park_info_list)

        return processed_data

    except KeyError as key_err:
        raise KeyError(f"Error. The inputted data is not correct Park data. Please check again. {key_err}")
    except IndexError as idx_err:
        raise IndexError(f"Error. The inputted data is not correct Park data. Please check again. {idx_err}")
    except ValueError as val_err:
        raise ValueError(f"Error. The inputted data is not correct Park data. Please check again. {val_err}")
    except MemoryError as mem_err:
        raise MemoryError(f"Error. The inputted data is not correct Park data. Please check again. {mem_err}")
    except Exception as err:
        raise Exception(f"Error. The inputted data is not correct Park data. Please check again. {err}")
    
