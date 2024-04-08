class Point():
    # This function is the construction, called it everytime when the class is called
    # self is an instances of the class
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2,2)

print(p)
print(p.x)
print(p.y)

# class Flight():
#     # The init function will declare everything needed for constructor variables 
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     def add_passenger(self, name):
#         if len(self.passengers) < int(self.capacity):
#             self.passengers.append(name)
#         else:
#             print("The flight is full, consider remove some passengers")

# flight = Flight(3)

# flight.add_passenger("Meng Kiat")
# flight.add_passenger("Hui Ru")
# flight.add_passenger("Yu Heng")
# flight.add_passenger("Yu Wei")

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if  not self.open_seats():
            return False
        
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight = Flight(3)
people = ["Meng Kiat", "Hui Ru", "Cassey", "Yu Heng", "Yu Wei"]

for person in people:
    # It will return true or false from the function
    success = flight.add_passenger(person)

    if success:
        print(f"Successfully adding {person} into seat")
    else:
        print("The seat is full, consider remove some person")


