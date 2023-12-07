'''
The class of ParkInfo is used to store information about a park in Greater Vancouver Area, including its ID, name, geographic coordinates and facilities.
Author: Yixiao Zhu
'''

class ParkInfo:
    '''
        Class: ParkInfo
        It contains information about a park in Greater Vancouver Area, including its ID, name, geographic coordinates and facilities.
    '''
    def __init__(self, parkid, name, longitude, latitude, facilities):
        '''
        Constructor -- create a new instance of Park
        Parameters:
            parkid -- an int, the park's ID
            name -- a str, the park's name
            longitude -- a float, the park's longitude
            latitude -- a float, the park's latitude
            facilities -- a list of str, the park's facilities        
        Raises:
            TypeError -- when user input less or more than 5 arguments
            TypeError -- when any of the input is not the right type
            NameError -- when input is not defined
        '''
        if len([parkid, name, longitude, latitude, facilities]) != PARAMS_NUM:
            raise TypeError("Class Park requires 5 argument: parkid, name, longitude, latitude, facilities.")

        elif isinstance(parkid, int) == False:
            raise TypeError("Wrong input: parkid should be an int.")

        elif isinstance(name, str) == False:
            raise TypeError("Wrong input: name should be a str.")

        elif isinstance(longitude, float) == False:
            raise TypeError("Wrong input: longitude should be a float.")

        elif isinstance(latitude, bool) == False:
            raise TypeError("Wrong input: latitude should be a float.")

        elif isinstance(facilities, list) == False:
            raise TypeError("Wrong input: facilities should be a list.")

        else:
            try:
                self.parkid = parkid
                self.name = name
                self.longitude = longitude
                self.latitude = latitude
                self.facilities = facilities
            except NameError:
                raise NameError("NameError occured. The input is not defined.")

    def to_list(self):
        '''
        Function: convert the ParkInfo object to a list
        Parameters:
            None
        Returns:
            a list of the park's information
        Raises:
            None
        '''
        return [self.parkid, self.name, self.longitude, self.latitude, self.facilities]
