'''
Cleans the raw pandas dataframe of csv file, and returns a cleaned pandas dataframe.
Author: Yixiao Zhu
'''
import pandas as pd
STARTING_INDEX = 0
ENDING_INDEX = -1

def clean_dataframe(raw_df, needed_indices):
    '''
    Function: cleans the raw dataframe and returns a cleaned dataframe.
    Parameters:
        raw_df -- a pandas dataframe of raw csv data
        needed_indices -- the indices of needed columns, in the form of a list of int
    Returns:
        cleaned_df -- a pandas dataframe of cleaned csv data
    Raises:
        TypeError -- if the input is not a pandas dataframe, or if required parameters are not inputted
        ValueError -- when inputted dataframe does not contain correct csv data
    '''
    if raw_df is None or needed_indices is None:
        raise TypeError("Error, function 'clean_dataframe' requires parameter 'raw_df' and 'needed_indices'.")
    
    if not isinstance(raw_df, pd.DataFrame):
        raise TypeError("Error. Please input a pandas dataframe.")

    if not isinstance(needed_indices, list) or not all(isinstance(index, int) for index in needed_indices):
        raise TypeError("Error. Please input a list of int.")

    try:
        cleaned_df = raw_df.iloc[:, needed_indices] # select the columns we need
        cleaned_df = cleaned_df.dropna() # drop any row with missing values
        cleaned_df = cleaned_df.reset_index(drop=True) # reset the index
        
        cleaned_df = cleaned_df.sort_values(by = cleaned_df.columns[STARTING_INDEX]) # sorting the parks in the numerical order of ParkID
        cleaned_df = cleaned_df.reset_index(drop = True) # reset the disordered indices
        
        return cleaned_df

    except IndexError as idx_err:
        raise IndexError(f"Error. The inputted data is not correct Park data. Please check again. {idx_err}")