def display_facility_menu(sorted_facilities_list):
    print("Please select facilities:")
    for index, facility in enumerate(sorted_facilities_list):
        print(f"{index + 1}. {facility}")


def get_selected_facilities(sorted_facilities_list):
    length = len(sorted_facilities_list)
    while True:
        selected_facilities_indices = input(
            "Please enter facility numbers, separate multiple facilities with commas(','): ")
        facility_indices = selected_facilities_indices.split(',')
        try:
            selected_indices = [int(index) for index in facility_indices]

            if all(index > 0 and index <= length for index in selected_indices):
                return selected_indices
            else:
                print(f"Invalid input. Please enter positive integers between 1 and {length} separated by commas.")
        except ValueError:
            print("Invalid input. Please enter valid integers separated by commas.")


def get_selected_park_indices(sorted_facilities_list, selected_facilities_indices, processed_data):
    selected_park_indices = []

    for index, park_info in enumerate(processed_data):
        park_facilities = park_info[3]
        selected_facilities = [sorted_facilities_list[index - 1] for index in selected_facilities_indices]

        if all(facility in park_facilities for facility in selected_facilities):
            selected_park_indices.append(index)

    return selected_park_indices

def display_max_parks_per_day_menu():
    while True:
        try:
            max_parks = int(input("Please enter the maximum number of parks you can visit in a day: "))
            if max_parks > 0:
                return max_parks
            else:
                print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")