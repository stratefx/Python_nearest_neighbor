# Distance.py

import csv
import datetime

# This class handles all distance calculations and package status updates as it parses through each trucks packages
class Distance:

    # Instantiates 2 lists to address and distance data from CSV files
    address_data_list = []
    distance_data_list = []

    # Parses address CSV file and loads it into an iterable list
    # Big-O(N)
    def load_address_data_list(self):
        self.address_data_list = []
        path = 'address_csv.csv'
        file = open(path)
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            self.address_data_list.append(row)

    # Parses distance CSV file and loads it into an iterable list
    # Big-O(N)
    def load_distance_data_list(self):
        self.distance_data_list = []
        path = 'distance_csv.csv'
        file = open(path)
        reader = csv.reader(file, delimiter=',')

        for row in reader:
            self.distance_data_list.append(row)

    # Returns distance data list
    def get_distance_list(self):
        return self.distance_data_list

    # Returns address data list
    def get_address_list(self):
        return self.address_data_list

    # Calculates time based on mileage
    # Big-O(1)
    def get_time(self, distance, truck_time):
        mins = (distance / 18) * 60
        time = truck_time
        tdelta = datetime.timedelta(minutes=mins)
        current_time = time + tdelta

        return current_time.time()

    # Gives us the row in address_list that matches our package address and returns the corresponding distance
    # in distance data list
    # Big-O(N)
    def get_address_row(self, starting_package_address, potential_package_address):
        potential_address_row = 0
        distance = 0.0
        for address_row in self.address_data_list:
            if(potential_package_address in address_row[0]):
                break
            potential_address_row += 1
        if(starting_package_address >= potential_address_row):
            distance = float(self.distance_data_list[starting_package_address][potential_address_row])

        return distance

    # Gives us the row in address_list that matches our package address
    # address_count is used to keep track of which row in address csv we're on
    # returns row of address file as address_count
    # Big_O(N)
    def get_row_for_address(self, starting_address):
        address_count = 0
        for address_row in self.address_data_list:
            if(starting_address in address_row[0]):
                break
            address_count += 1
        return address_count

    # Sets shortest_distance variables initial value to largest value in corresponding row
    def set_shortest_distance(self, row):
        print(max(self.distance_data_list[row]))

    # Handles any situation in which multiple packages loaded on the same truck are to be delivered to the
    # same address, making sure not to duplicate mileage for those packages
    # Big-O(N)
    def duplicate_addresses(self, starting_package_address, truck, my_hash_table, shortest_distance):
        for i in truck.cargo:
            if(starting_package_address == my_hash_table.search(i).address):
                p = my_hash_table.search(i)
                p.status = 'Delivered'
                p.delivery_time = self.get_time(shortest_distance, truck.time)
                truck.cargo.remove(i)

    # A variation of Nearest Neighbor algorithm
    # Takes as input a truck, a package and a hash table
    # Big-O(N^2)
    def next_package(self, truck, starting_package, my_hash_table):
        # Extracts packages address, finds which row of address list has that matching address,
        # initializes shortest_distance variable to farthest distance in corresponding data list row
        # and initializes variables for later use
        # Big-O(1)
        starting_package_address = starting_package.address
        starting_address_index = self.get_row_for_address(starting_package_address)
        shortest_distance = max(self.distance_data_list[starting_address_index])
        distance = 0.0
        selected_package_index = -1
        selected_package_id = -1
        package_index = -1

        # Iterates through each package id on truck where each package corresponding to a package id on the truck
        #   represents a potential next package to be passed recursively to sequence
        # For potential package to be chosen to be next, it must have to closest delivery  address to the
        #   current iterations starting package address, hence, why it is called "Nearest Neighbor"
        # Algorithm holds each distance in a variable called shortest distance as it iterates through all
        #   packages on the truck
        # Algorithm gets corresponding row in address list for each potential next package, and with that data can
        #   parse through the distance data list that corresponds to each pair of addresses, checking each and
        #   finding the shortest distance to the next package, making sure the chosen next package is on current truck
        # Big-O(N^2)
        for i in truck.cargo:
            potential_next_package_address = my_hash_table.search(i).address
            potential_next_package_index = self.get_row_for_address(potential_next_package_address)
            if (starting_address_index < potential_next_package_index):
                distance = self.distance_data_list[potential_next_package_index][starting_address_index]
                package_index = potential_next_package_index
                package_id = my_hash_table.search(i).id
            else:
                distance = self.distance_data_list[starting_address_index][potential_next_package_index]
                package_index = potential_next_package_index
                package_id = my_hash_table.search(i).id
            shortest_distance = float(shortest_distance)
            distance = float(distance)
            if (0.0 < distance < shortest_distance):
                    shortest_distance = distance
                    selected_package_index = package_index
                    selected_package_id = package_id

        # Updates package data for the package that was passed into sequence during current iteration
        # Big-O(1)
        p = my_hash_table.search(starting_package.id)
        p.status = 'Delivered'
        p.delivery_time = self.get_time(shortest_distance, truck.time)
        p.deliver_miles = shortest_distance
        truck.cargo.remove(starting_package.id)
        self.duplicate_addresses(starting_package_address, truck, my_hash_table, shortest_distance)

        # Calculates mileage from final package deliver of truck 2 back to the hub so drier can
        # switch to truck 3
        # Big-O(1)
        if((len(truck.cargo) == 1) and (truck.name == 'Truck 2')):
            truck.mileage = float(self.distance_data_list[selected_package_index][0])

        # Recursive call to next_package sequence until truck has delivered all loaded packages
        # Big_O(1)
        if(len(truck.cargo) and (selected_package_index != -1)):
            self.next_package(truck, my_hash_table.search(selected_package_id), my_hash_table)
