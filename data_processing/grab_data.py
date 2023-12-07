'''
Grabs the csv data from the url and returns it as a string
Author: Yixiao Zhu
'''

import requests
KEY_WORD = "http"

def grab_data(url):
    '''
    Function: to retrieve the csv file from inputted url, and return it as a uncleaned string
    Parameters:
        url -- a string
    Returns:
        text -- a string of the uncleaned csv data
    Raises:
        TypeError -- if the input is not a str, or if required parameters are not inputted
        ValueError -- if the inputted str is not a url
        HTTPError -- when HTTPError occurs
        ConnectionError -- when connection failed
        Timeout -- when connection timeouts
        TooManyRedirects -- when failed to connnect after too many redirects
        RequestException -- when other error occurs
    '''    
    if url is None:
        raise TypeError("Error, function 'grab_data' requires parameter 'url'.")

    if not isinstance(url, str):
        raise TypeError("Error. The input should be a link.")

    if KEY_WORD not in url:
        raise ValueError("Error. Please input a url.")

    else:
        try:
            response = requests.get(url)

            if response.status_code == 200:               
                text = response.text
                return text
            else:
                response.raise_for_status()

        except requests.exceptions.HTTPError as http_error:
            raise requests.exceptions.HTTPError(f"HTTPError.{http_error}")
        except requests.exceptions.ConnectionError as conn_error:
            raise requests.exceptions.ConnectionError(f"ConnectionError. {conn_error}")
        except requests.exceptions.Timeout as timeout_error:
            raise requests.exceptions.Timeout(f"Timeout Error. {timeout_error}")
        except requests.exceptions.TooManyRedirects as red_error:
            raise requests.exceptions.TooManyRedirects(f"Error. TooManyRedirects. {red_error}")
        except requests.exceptions.RequestException as req_error:
            raise requests.exceptions.RequestException(f"Error occured.{req_error}")


