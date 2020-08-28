# This file checks status of two circles. See https://www.bbc.co.uk/bitesize/guides/z9pssbk/revision/4 for details. 

import math

# Read data from the user.
first_circle_center_and_radius = input("Enter center coordinates and radius of first circle (example: x1 y1 r1) = ")
second_circle_center_and_radius = input("Enter center coordinates and radius of first circle (example: x2 y2 r2) = ")

# The values from the users are of type string.
# To perform mathematical operations, we need to convert them to float type
x1, y1, r1 = [float(coordinate)  for coordinate in first_circle_center_and_radius.split()]
x2, y2, r2 = [float(coordinate)  for coordinate in first_circle_center_and_radius.split()]

# Compute the distance between centers 
distance_max = r1 + r2 
distance_min = abs(r1 -r2)
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distance == distance_max or distance == distance_min: 
    print("The circles touch each other")
elif distance_min < distance < distance_max: 
    print("The circles interect at two points") 
elif distance == r1 or distance == r2: 
    print("The center of one circle lies on the other")
elif distance == 0: 
    print("Two circle are concentric")
else: 
    raise ValueError("Undetermined status")
