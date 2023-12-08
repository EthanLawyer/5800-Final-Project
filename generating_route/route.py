from geopy.distance import geodesic
import random
import requests

MAX_PARKS_PER_DAY = 3

# Sample data for parks in Metro Vancouver
parks_data = [
    ["Stanley Park", 49.3043, -123.1443],
    ["Queen Elizabeth Park", 49.2419, -123.1124],
    ["Grouse Mountain", 49.3801, -123.0815],
    ["Lynn Canyon Park", 49.3438, -123.0179],
    ["Pacific Spirit Regional Park", 49.2505, -123.2101],
    ["Burnaby Mountain Park", 49.2776, -122.9126],
    ["Lighthouse Park", 49.3316, -123.2636],
    ["Capilano River Regional Park", 49.3529, -123.1149],
    ["Deer Lake Park", 49.2380, -122.9899],
    ["VanDusen Botanical Garden", 49.2397, -123.1298]
]

# Add a random number between 0.7 and 1.0 to each park
for park in parks_data:
    random_number = round(random.uniform(0.7, 1.0), 2)
    park.append(random_number)


def get_location():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    return latitude, longitude


latitude, longitude = get_location()
parks_data = [["my location", latitude, longitude, 1.0]] + parks_data
# print(parks_data)


class Route():
    def __init__(self, data):
        self.data = data
        self.size = len(data)
        self.visited = set()
        self.final_routes = []
        self.graph = []
        self.visited.add(0)

    def coords(self, id):
        return self.data[id][1], self.data[id][2]

    def distance(self, a, b):
        return round(geodesic(a, b).kilometers, 2)

    def build_graph(self):
        for i in range(self.size):
            cur_row = []
            for j in range(self.size):
                if i == j:
                    cur_row.append(0)
                else:
                    start = self.coords(i)
                    dest = self.coords(j)
                    cost = round(self.distance(start, dest) * self.data[j][3] * self.data[i][3], 4)
                    cur_row.append(cost)
            self.graph.append(cur_row)

    def prim(self):
        count = MAX_PARKS_PER_DAY
        cur = 0
        day_route = "my location"
        day_distance = 0
        while count > 0 and self.size != len(self.visited):
            next_cost = -1
            next_dest = -1
            for i, cost in enumerate(self.graph[cur]):
                if (next_cost < 0 or cost < next_cost) and (i not in self.visited):
                    next_cost = cost
                    next_dest = i
            day_distance += self.distance(self.coords(cur), self.coords(next_dest))
            day_route += " -> " + self.data[next_dest][0]
            count -= 1
            cur = next_dest
            self.visited.add(cur)
        return day_route, round(day_distance, 2)

    def compute_all_routes(self):
        while self.size != len(self.visited):
            day_route, day_distance = self.prim()
            self.final_routes.append((day_route, str(day_distance) + "km"))

    def display_results(self):
        self.build_graph()
        self.compute_all_routes()
        for item in self.final_routes:
            print(item)


def main():
    route = Route(parks_data)
    route.display_results()


if __name__ == "__main__":
    main()

