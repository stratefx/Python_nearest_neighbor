# Package.py
import csv

# This class serves to create package objects with attributes that aid in conforming to delivery constraints(assumptions)
# Big-O(N)
class Package:

    # Constructor
    # Big-O(1)
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, status='At the hub'):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self. weight = weight
        self.notes = notes
        self.status = status
        self.delivery_time = 0 # use as a dateTime
        self.deliver_miles = 0 # to add all package miles to get total mile instead of using truck
        self.truck = ''

    # ToString
    # Big-O(1)
    def __str__(self):
        return 'ID: %s, Address: %s, City: %s, Zip: %s, Deadline: %s, Weight: %s,' \
               ' Status: %s, Delivery Time: %s' % \
               (self.id, self.address, self.city, self.zip, self.deadline, self.weight,
                self.status, self.delivery_time)

    # Loads the package data from the CSV and uses constructor to instantiate package object
    #   and places them in the hash table each with a unique key
    def load_package_data(my_hash_table):
        path = 'package_csv.csv'
        file = open(path, newline='')
        reader = csv.reader(file, delimiter=',')
        next(reader)

        # Loops through each line of the CSV file after it's been read in by the reader and passes data
        #   to package constructor
        # Big-O(N)
        for package in reader:
            # id, address, city, state, zip, deadline, weight, notes
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            weight = float(package[6])
            notes = package[7]

            p = Package(id, address, city, state, zip, deadline, weight, notes)
            my_hash_table.insert(p.id, p)
