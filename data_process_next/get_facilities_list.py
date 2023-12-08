def get_sorted_unique_facilities(processed_data):
    '''
    Function: Get sorted and unique park facility names from processed_data list.
    Parameters:
        processed_data -- a list of ParkInfo objects, the processed data
    Returns:
        sorted_facilities -- a sorted list of unique park facility names
    '''
    facilities = []
    for park_info in processed_data:
        facilities.extend(park_info[3])
    sorted_facilities_list = sorted(set(facilities))
    return sorted_facilities_list

def get_parks_by_facilities(processed_data):
    '''
    Function: Get parks that have selected facilities from processed_data list.
    Parameters:
        processed_data -- a list of ParkInfo objects, the processed data
    Returns:
        selected_parks -- a list of parks that have selected facilities
    '''
    sorted_facilities_list = get_sorted_unique_facilities(processed_data)

    print("Please select facilities：")
    for index, facility in enumerate(sorted_facilities_list):
        print(f"{index + 1}. {facility}")

    selected_facilities_indices = input("Please enter facility numbers, separate multiple facilities with commas(','):：")
    selected_facilities_indices = [int(i) for i in selected_facilities_indices.split(',')]

    selected_parks = []
    for park_info in processed_data:
        park_facilities = park_info[3]
        if any(index - 1 < len(sorted_facilities_list) and sorted_facilities_list[index - 1] in park_facilities for index in selected_facilities_indices):
            selected_parks.append(park_info)

    return selected_parks
