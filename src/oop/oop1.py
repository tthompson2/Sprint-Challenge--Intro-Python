# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
   
    print('pass')

class FlightVehicle(Vehicle):

    print('pass')

class Starship(FlightVehicle):
    print('pass')

class GroundVehicle(Vehicle):
    print('pass')

class Car(GroundVehicle):
    print('pass')

class Motorcycle(GroundVehicle):
    print('pass')

class Airplane(FlightVehicle):
    print('pass')

