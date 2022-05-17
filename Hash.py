# Hash.py
import csv

# This class functions to create a hash table with a unique hash code and allow a user to
#   search, update or remove items
# Big-O(N)
class HashTable():
    # Assigns all buckets with an empty list called hash_table
    # Big-O(N)
    def __init__(self, initial_capacity):
        # Constructor puts an empty list in each bucket. A list of lists.
        self.hash_table = []
        for i in range(initial_capacity):
            # appends an empty list (inner bucket list) to each element of hash_table
            self.hash_table.append([])

    # This function is in case hash() is not allowed
    # Big-O(N)
    def my_hash_function(self, key):
        prime = 31
        hashed_number = 0
        for i in range(len(self.table)):
            hashed_number = prime * hashed_number + key

        return hashed_number

    # Inserts new item into the hash hash_table or updates existing one
    # Big-O(N)
    def insert(self, key, package):
        # Get unique number to determine which bucket (hash_bucket) in hash_table to put new item
        # If hash() is not allowed, use this     ==>     hash_bucket = my_hash_function(key)
        hash_bucket = hash(key) % len(self.hash_table)   # this is which bucket to use
        bucket_list = self.hash_table[hash_bucket]       # this is the list of buckets available

        # If key is found and exists already, update it
        for key_val in bucket_list:
            # print(key_value)
            if key_val[0] == key:
                key_val[1] = package
                return True

        # If key does not already exist, append to end of bucket_list inside hash_table element
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    # Locates an item using hash key and returns it
    # Big-O(N)
    def search(self, key):
        # get unique number (which bucket) in hash_table where this key would be.
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]
        # print(bucket_list)

        # search list (bucket_list) inside list (hash_table)
        for key_val in bucket_list:
            # print(key_value)
            # key_val[0] = ID , key_val[1] = value
            if key_val[0] == key:
                #print(key_val[1])
                return key_val[1]
        return None

    # Removes an item with matching key from the hash_table.
    # Big-O(N)
    def remove(self, key):
        # get unique number (which bucket) in hash_table where this key would be.
        bucket = hash(key) % len(self.hash_table)
        bucket_list = self.hash_table[bucket]

        # remove the item from bucket_list inside hash_table
        for key_val in bucket_list:
            # print (key_value)
            if key_val[0] == key:
                bucket_list.remove([key_val[0], key_val[1]])