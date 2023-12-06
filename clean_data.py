'''
Cleans the raw data from the csv file and returns a cleaned pandas dataframe.
Author: Yixiao Zhu
'''

import grab_data
import pandas as pd

STARTING_INDEX = 0
ENDING_INDEX = -1
KEY_WORD = "http"
LETTERS_TO_REMOVE = "\ufeff"

def create_dataframe(text):
    '''
    Function: cleans the raw data from the csv file and returns a cleaned pandas dataframe.
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

        splitted_data = text.split("\r\n") # note: all lines in the csv end with \r\n

        if len(splitted_data) == 1:
            raise ValueError("Error. The inputted text does not contain correct csv data.") # if the string in data does not contain the delimiter we assigned, it returns a list of one element

        column_titles = splitted_data[STARTING_INDEX].split(";") # getting a list of all the column titles

        if len(column_titles) == 1:
            raise ValueError("Error. The inputted text does not contain correct csv data.") # if the string of column titles does not contain the delimiter we assigned, it returns a list of one element
        
        rows = []

        for row in splitted_data[STARTING_INDEX+1 : ENDING_INDEX]: # splitting each row by ";" 
            row_splitted = row.split(";")

            if len(row_splitted) == 1:
                raise ValueError("Error. The inputted text does not contain correct csv data.") # if the string in data does not contain the delimiter we assigned, it returns a list of one element

            else:
                if row_splitted != [""]: # delete any blank row
                    rows.append(row_splitted)

        raw_df = pandas.DataFrame(rows, columns = column_titles) # create a raw pandas dataframe for further cleaning

        return raw_df

    else:
        raise TypeError("Error. Please input a str.")