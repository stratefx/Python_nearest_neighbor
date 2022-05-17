# Michael Bliss | Student ID #001136448

from Distance import Distance
import Hash
import Truck
import Package
import datetime
import csv

# Determines capacity of hash table
# Big-O(N)
path = 'package_csv.csv'
file = open(path, newline='')
reader = csv.reader(file, delimiter=',')
next(reader)
initial_capacity = 0
for line in reader:
    initial_capacity += 1

# Creates hash instance
my_hash_table = Hash.HashTable(initial_capacity)
Package.Package.load_package_data(my_hash_table)

# Prints all package data as it stands post delivery to screen
# Big-O(N)
def get_all_package_data():
    for i in range(len(my_hash_table.hash_table) + 1):
        print('{}'.format(my_hash_table.search(i + 1)))

# Creates 3 Truck objects
truck1 = Truck.Trucks()
truck1.name = 'Truck 1'
truck1.time = datetime.datetime(2021, 1, 1, 9, 5, 0)
truck2 = Truck.Trucks()
truck2.name = 'Truck 2'
truck2.time = datetime.datetime(2021, 1, 1, 8, 0, 0)
truck3 = Truck.Trucks()
truck3.name = 'Truck 3'
truck3.time = datetime.datetime(2021, 1, 1, 10, 6, 0)

# Load truck1
# Big-O(N)
for p in range(1, 41):
    package = my_hash_table.search(p)
    if(package.id == 1 or
            package.id == 4 or
            package.id == 5 or
            package.id == 7 or
            package.id == 8 or
            package.id == 10 or
            package.id == 6 or
            package.id == 25 or
            package.id == 28 or
            package.id == 29 or
            package.id == 30 or
            package.id == 32 or
            package.id == 34 or
            package.id == 37 or
            package.id == 40):
        truck1.cargo.append(package.id)
        package.truck = truck1.name

# Load truck2
# Big-O(N)
for p in range(1, 41):
    package = my_hash_table.search(p)
    if (package.id == 2 or
            package.id == 3 or
            package.id == 13 or
            package.id == 14 or
            package.id == 15 or
            package.id == 16 or
            package.id == 19 or
            package.id == 20 or
            package.id == 11 or
            package.id == 12 or
            package.id == 18 or
            package.id == 21 or
            package.id == 22 or
            package.id == 23 or
            package.id == 36 or
            package.id == 38):
        truck2.cargo.append(package.id)
        package.truck = truck2.name

# Load truck 3
# BigO_(N)
for p in range(1, 41):
    package = my_hash_table.search(p)
    if (package.id == 9 or
            package.id == 17 or
            package.id == 24 or
            package.id == 26 or
            package.id == 27 or
            package.id == 31 or
            package.id == 33 or
            package.id == 35 or
            package.id == 39):
        truck3.cargo.append(package.id)
        package.truck = truck3.name

# Loads CSV files for distance and addresses into 2 separate lists
distance_object = Distance()
distance_object.load_distance_data_list()
distance_object.load_address_data_list()


# Calls next_package sequence once for each truck, generating delivery data
distance_object.next_package(truck1, my_hash_table.search(25), my_hash_table)
distance_object.next_package(truck2, my_hash_table.search(2), my_hash_table)
distance_object.next_package(truck3, my_hash_table.search(9), my_hash_table)

# Calculates total miles, prints total miles and all package data to screen before
# prompting user for input selection
# Big-O(N)
miles = 0
for i in range(1, 41):
    miles = my_hash_table.search(i).deliver_miles + miles
print('\nTOTAL MILEAGE : ', miles + truck1.mileage, '\n')
get_all_package_data()

# Takes a time from user and calculates all package statuses at that time
# Big-O(N)
def user_input_time_status(time, my_hash_table):
    for i in range(1, 41):
        p = my_hash_table.search(i)

        if((p.truck == truck1.name) and (truck1.time.time() < time.time() < p.delivery_time)):
            my_hash_table.search(i).status = 'En Route on Truck 1'
        elif ((p.truck == truck1.name) and (time.time() < truck1.time.time())):
                my_hash_table.search(i).status = 'At the hub'
        elif ((p.truck == truck2.name) and (truck2.time.time() < time.time() < p.delivery_time)):
                my_hash_table.search(i).status = 'En Route on Truck 2'
        elif((p.truck == truck2.name) and (time.time() < truck2.time.time())):
            my_hash_table.search(i).status = 'At the hub'
        elif ((p.truck == truck3.name) and (truck3.time.time() < time.time() < p.delivery_time)):
            my_hash_table.search(i).status = 'En Route on Truck 3'
        elif ((p.truck == truck3.name) and (time.time() < truck3.time.time())):
            my_hash_table.search(i).status = 'At the hub'

    # Will print all package data to the screen as they stand at the time input by user
    get_all_package_data()
    # Resets package statuses to delivered so user can input another time
    for i in range(1, 41):
        my_hash_table.search(i).status = 'Delivered'

# Main method, entry point for user
if __name__ == '__main__':

    # Presents user with interface for selections to interact with program and display selected data
    # Big-O(1)
    end_program = True
    while (end_program):
        # prints option for user to  choose from
        print('\nChoose from the following by entering the number:')
        print('1: Print one specific package by ID')
        print('2: Search by time')
        print('3: Terminate program')

        # Takes input from user for selection
        selection = input("\nChose your selection wisely (1, 2, or 3): ")

        # Select individual package by ID
        if selection == '1':
            package_id = int(input("Enter the package ID (1 - 40):"))
            print('\nYour selection:')
            print(Hash.HashTable.search(my_hash_table, package_id))
        # Display all package data at a user given time
        elif selection == '2':
            time_input = input('Enter a time in the format Hour:Minutes - ')
            time = datetime.datetime.strptime(time_input, '%H:%M')
            user_input_time_status(time, my_hash_table)
        # Terminates program
        elif selection == '3':
            print('Goodbye for now, but not forever...')
            end_program = False
        # Handles invalid user input
        elif selection == '4':
            path = 'package_csv.csv'
            file = open(path, newline='')
            reader = csv.reader(file, delimiter=',')
            next(reader)
            initial_capacity = 0
            for line in reader:
                initial_capacity += 1
            print(initial_capacity)
        else:
            print('Something went wrong! Please make another selection (1, 2, or 3).')
