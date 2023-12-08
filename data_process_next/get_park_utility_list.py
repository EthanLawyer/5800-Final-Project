def get_selected_park_indices(sorted_facilities_list, selected_facilities_indices, processed_data):
    '''
    Function: Get indices of parks that have all selected facilities.
    Parameters:
        sorted_facilities_list -- a sorted list of unique park facility names
        selected_facilities_indices -- a list of indices representing selected facilities
        processed_data -- a list of ParkInfo objects, the processed data
    Returns:
        selected_park_indices -- a list of indices of parks that have all selected facilities
    '''
    selected_park_indices = []

    for index, park_info in enumerate(processed_data):
        park_facilities = park_info[3]
        selected_facilities = [sorted_facilities_list[index - 1] for index in selected_facilities_indices]

        if all(facility in park_facilities for facility in selected_facilities):
            selected_park_indices.append(index)

    return selected_park_indices


def get_park_utility_list(processed_data):
    '''
    Function: Transform park data to include a utility value based on facility count.
    Parameters:
        processed_data -- a list of ParkInfo objects, the processed data
    Returns:
        transformed_data -- a list of park data with transformed utility values
    '''
    transformed_data = []
    max_count_at_index_3 = max(len(park_info[3]) for park_info in processed_data)

    for park_info in processed_data:
        count_at_index_3 = len(park_info[3])
        transformed_value = 1 - 0.3 * (count_at_index_3 / max_count_at_index_3)
        new_park_info = [park_info[0], park_info[1], park_info[2], transformed_value]
        transformed_data.append(new_park_info)

    return transformed_data

