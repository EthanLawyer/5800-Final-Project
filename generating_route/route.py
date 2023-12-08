from geopy.distance import geodesic
import requests


class Route():
    def __init__(self, data, parks_per_day):
        self.data = data
        self.size = len(data)
        self.visited = set()
        self.final_routes = []
        self.graph = []
        self.visited.add(0)
        self.parks_per_day = parks_per_day

    def add_self_location(self):
        response = requests.get('https://ipinfo.io')
        data = response.json()
        location = data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]
        self.data = [["my location", latitude, longitude, 1.0]] + self.data

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
        count = self.parks_per_day
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
            self.final_routes.append(day_route + ", total travel distance: " + str(day_distance) + "km")

    def display_results(self):
        self.add_self_location()
        if len(self.data) == 1:
            print("There is no park satisfying all of your preferences. Please choose less facilities.")
            return
        self.build_graph()
        self.compute_all_routes()
        print("Comprehensively considering your location and preferences, here are the recommended routes:")
        for item in self.final_routes:
            print(item)
