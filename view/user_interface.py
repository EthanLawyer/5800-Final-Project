def display_facility_menu(sorted_facilities_list):
    print("Please select facilities:")
    for index, facility in enumerate(sorted_facilities_list):
        print(f"{index + 1}. {facility}")


def get_selected_facilities():
    selected_facilities_indices = input(
        "Please enter facility numbers, separate multiple facilities with commas(','): ")
    return [int(i) for i in selected_facilities_indices.split(',')]


def get_selected_park_indices(sorted_facilities_list, selected_facilities_indices, processed_data):
    selected_park_indices = []

    for index, park_info in enumerate(processed_data):
        park_facilities = park_info[3]
        selected_facilities = [sorted_facilities_list[index - 1] for index in selected_facilities_indices]

        if all(facility in park_facilities for facility in selected_facilities):
            selected_park_indices.append(index)

    return selected_park_indices

def display_max_parks_per_day_menu():
    '''
    Function: Get the maximum number of parks a user can visit in a day.
    Returns:
        max_parks -- an integer representing the maximum number of parks per day
    '''
    try:
        max_parks = int(input("Please enter the maximum number of parks you can visit in a day: "))
        return max_parks
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return display_max_parks_per_day_menu()