'''
Cleans the raw data from the csv file and returns a cleaned pandas dataframe.
Author: Yixiao Zhu
'''

import grab_data
import pandas as pd

STARTING_INDEX = 0
ENDING_INDEX = -1
LETTERS_TO_REMOVE = "\ufeff"
LINE_BREAK = "\r\n"
LINE_SEPARATOR = ";"

def create_dataframe(text):
    '''
    Function: cleans the raw data from the csv file and returns a raw pandas dataframe.
    Parameters:
        text -- a string of the uncleaned csv data
    Returns:
        raw_df -- a pandas dataframe of raw csv data
    Raises:
        TypeError -- if the input is not a str, or if required parameters are not inputted
        ValueError -- when inputted str does not contain correct csv data
    '''
    if text is None:
        raise TypeError("Error, function 'create_dataframe' requires parameter 'text'.")

    if isinstance(text, str):

        splitted_data = text.split(LINE_BREAK) # note: all lines in the csv end with \r\n

        if len(splitted_data) == 1:
            raise ValueError("Error. The inputted text does not contain correct csv data.") # if the string in data does not contain the delimiter we assigned, it returns a list of one element

        column_titles = splitted_data[STARTING_INDEX].split(LINE_SEPARATOR) # getting a list of all the column titles

        if len(column_titles) == 1:
            raise ValueError("Error. The inputted text does not contain correct csv data.") # if the string of column titles does not contain the delimiter we assigned, it returns a list of one element
        
        rows = []

        for row in splitted_data[STARTING_INDEX+1 : ENDING_INDEX]: # splitting each row by ";" 
 
            if LETTERS_TO_REMOVE in row:
                row = row.replace(LETTERS_TO_REMOVE, "")
            
            row_splitted = row.split(LINE_SEPARATOR)

            if len(row_splitted) == 1:
                raise ValueError("Error. The inputted text does not contain correct csv data.") # if the string in data does not contain the delimiter we assigned, it returns a list of one element

            else:
                if row_splitted != [""]: # delete any blank row
                    rows.append(row_splitted)

        raw_df = pd.DataFrame(rows, columns = column_titles) # create a raw pandas dataframe for further cleaning

        return raw_df

    else:
        raise TypeError("Error. Please input a str.")


def clean_dataframe(raw_df, indices):
    '''
    Function: cleans the raw dataframe and returns a cleaned dataframe.
    Parameters:
        raw_df -- a pandas dataframe of raw csv data
        indices -- the indices of needed columns, in the form of a list of int
    Returns:
        cleaned_df -- a pandas dataframe of cleaned csv data
    Raises:
        TypeError -- if the input is not a pandas dataframe, or if required parameters are not inputted
        ValueError -- when inputted dataframe does not contain correct csv data
    '''
    if raw_df is None or indices is None:
        raise TypeError("Error, function 'clean_dataframe' requires parameter 'raw_df' and 'indices'.")
    
    if not isinstance(raw_df, pd.DataFrame):
        raise TypeError("Error. Please input a pandas dataframe.")

    if not isinstance(indices, list) or not all(isinstance(index, int) for index in indices):
        raise TypeError("Error. Please input a list of int.")

    try:
        cleaned_df = raw_df.iloc[:, indices] # select the columns we need
        cleaned_df = cleaned_df.dropna() # drop any row with missing values
        cleaned_df = cleaned_df.reset_index(drop=True) # reset the index
        
        for i in range(len(cleaned_df)): # convert all the ParkID from str to int
            item = cleaned_df.iloc[i, STARTING_INDEX]
            if item.isnumeric():
                cleaned_df.iloc[i, STARTING_INDEX] = int(item)
            else:
                raise ValueError("Wrong input data.")
        
        cleaned_df = cleaned_df.sort_values(by = cleaned_df.columns[STARTING_INDEX]) # sorting the parks in the numerical order of ParkID
        cleaned_df = cleaned_df.reset_index(drop = True) # reset the disordered indices
        
        return cleaned_df

    except IndexError as idx_err:
        raise IndexError(f"Error. The inputted data is not correct Park data. Please check again. {idx_err}")