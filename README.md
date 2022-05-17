# Python_nearest_neighbor
A variation of the nearest neighbor problem, solving a real world problem with the use of data structures and algorithms.

Applies the algorithms and data structures studied to solve a real programming problem. Implements an algorithm to route delivery trucks that allow 
all delivery constraints to be met while traveling under 140 miles total distance.

A fictitious parcel service needs to determine an efficient route and delivery distribution for their Daily Local Deliveries (DLD) because packages 
are not currently being consistently delivered by their promised deadline. The DLD route has three trucks, two drivers, and an average 
of 40 packages to deliver each day. Each package has specific criteria and delivery requirements.

This software solution determines an algorithm in code and presents a solution where all 40 packages (sourced from a supplied Microsoft Excel file) will be delivered on time while meeting each package’s requirements and keeping the combined total distance traveled under 140 miles for both trucks. The specific delivery locations are shown on a map supplied by the educational institution and distances to each location are given in the attached distance table.

A recursive algorithm is implimented at runtime to find the nearest neighbor. A console UI with 3 options to choose from is then presented to the
user. They can check the status of an individual package by searching a hash table with it's package id, the status of all package at any
time of the user's choosing (demonstrating where each truck and package at any given time durring the delivery simulation), or terminate
the program.
