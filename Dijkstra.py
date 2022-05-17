# Dikstra.py
import Truck
import main


class Vertex:
    # Constructor for a new Vertx object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, address):
        self.address = address
        self.distance = float('inf')
        self.previous_address = None

class Graph:
    def __init__(self):
        self.adjacency_dictionary = {} # vertex dictionary {key:value}
        self.distances_dictionary = {} # edge dictionary {key:value}

    def add_vertex(self, new_address):
        self.adjacency_dictionary[new_address] = [] # {vertex_1: [], vertex_2: [], ...}

    def add_directed_edge(self, from_address, to_address, distance = 1.0):
        self.distances_dictionary[(from_address, to_address)] = distance
            # {(vertex_1,vertex_2): 484, (vertex_1,vertex_3): 626, (vertex_2,vertex_6): 1306, ...}
        self.adjacency_dictionary[from_address].append(to_address)
            # {vertex_1: [vertex_2, vertex_3], vertex_2: [vertex_6], ...}

    def add_undirected_edge(self, address_a, address_b, distance = 1.0):
        self.add_directed_edge(address_a, address_b, distance)
        self.add_directed_edge(address_b, address_a, distance)


def dijkstra_shortest_path(g, start_address, truck1, truck2):
    # Create queue of unvisited addresses and fill it with all addresses
    unvisited_address_queue = []
    for current_address in g.adjacency_dictionary:
        unvisited_address_queue.append(current_address)

    # Start_address has a distance of 0 from itself
    start_address.distance = 0


    # One address is removed with each iteration until all are removed (visited)
    while len(unvisited_address_queue) > 0:

        # Visit address with minimum distance from start_vertex
        smallest_index = 0
        #miles = 0
        for i in range(1, len(unvisited_address_queue)):
            #print(unvisited_address_queue[i].address, unvisited_address_queue[i].distance, unvisited_address_queue[i].previous_address)
            if unvisited_address_queue[i].distance < unvisited_address_queue[smallest_index].distance:
                smallest_index = i
                #miles = unvisited_address_queue[i].distance + miles
                #print('smallest index is: ', smallest_index)

        current_address = unvisited_address_queue.pop(smallest_index)
        #miles = current_address.distance + miles
        #print(miles)
        #print("From Start Vertex to current_address.address: " + current_address.address + " distance: " + str(current_address.distance))

        # Check potential path lengths from the current address to all adjacent addresses
        for adj_address in g.adjacency_dictionary[current_address]: # values from adjacency_dictionary
            distance = g.distances_dictionary[(current_address, adj_address)] # values from distances_dictionary
            alternative_path_distance = current_address.distance + distance

            # If shorter path from start_address to adj_address is found, update adj_address's distance and previous address
            if alternative_path_distance < adj_address.distance:
                adj_address.distance = alternative_path_distance
                adj_address.previous_address = current_address

                # This line updates mileage
                truck1.mileage = adj_address.distance + truck1.mileage

                # This line prints the current mileage and time
                print(truck1.mileage, ' ', main.get_time(truck1, truck2))

'''
    At some point during this function I need to check truck cargo to see if
    package addresses match current address and deliver that package if so
    
    Is it possible to only pass a single truck object and force the algorithm to 
    only visit 16 addresses per call to match the cargo capacity of the truck??
    Then run it again for the second truck object? If so, the first truck will need
    to return to the hub to get the remaining packages for the final run. 
    
    Will need to accept a user selected time as an argument and check it each iteration,
    then when the time is reached, end and display the package status at that time
'''


# Not sure how or if I can use this for anything yet
def get_shortest_path(start_address, end_address):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_address = end_address
    while current_address is not start_address:
        path = " -> " + str(current_address.address) + path
        current_address = current_address.previous_address
    path = start_address.address + path
    return path

# Not sure how or if I can use this for anything yet
def get_shortest_path_city(start_address, end_address, my_hash_table):
    # Start from end_vertex and build the path backwards.
    path = ""
    current_address = end_address
    while current_address is not start_address:
        #package = my_hash_table.search(int(current_address.address))
        package = my_hash_table.search(current_address.address)
        path = " -> " + package.address + path
        current_address = current_address.previous_address
    path = "Salt Lake City " + path
    return path
