# # ---Task 1---
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __eq__(self, other):
#         return self.radius == other.radius

#     def __gt__(self, other):
#         return self.radius > other.radius

#     def __lt__(self, other):
#         return self.radius < other.radius

#     def __le__(self, other):
#         return self.radius <= other.radius

#     def __ge__(self, other):
#         return self.radius >= other.radius

#     def __add__(self, value):
#         return Circle(self.radius + value)

#     def __sub__(self, value):
#         return Circle(self.radius - value)

#     def __iadd__(self, value):
#         self.radius += value
#         return self

#     def __isub__(self, value):
#         self.radius -= value
#         return self

#     def __str__(self):
#         return f"Circle with radius {self.radius}"

# circle1 = Circle(5)
# circle2 = Circle(7)

# print(circle1 == circle2) 
# print(circle1 > circle2)  
# print(circle1 < circle2)
# print(circle1 <= circle2)
# print(circle1 >= circle2)

# circle3 = circle1 + 2 
# circle4 = circle2 - 1  

# print(circle3)
# print(circle4)

# circle1 += 3  
# circle2 -= 1 

# print(circle1)
# print(circle2)

# ---Task 2---
# class Airplane:
#     def __init__(self, model, max_passengers, current_passengers):
#         self.model = model
#         self.max_passengers = max_passengers
#         self.current_passengers = current_passengers

#     def __eq__(self, other):
#         return self.model == other.model

#     def __add__(self, passengers):
#         new_passengers = self.current_passengers + passengers
#         if new_passengers <= self.max_passengers:
#             self.current_passengers = new_passengers
#         else:
#             print("Not enough space for additional passengers!")

#     def __iadd__(self, passengers):
#         self.__add__(passengers)
#         return self

#     def __sub__(self, passengers):
#         new_passengers = self.current_passengers - passengers
#         if new_passengers >= 0:
#             self.current_passengers = new_passengers
#         else:
#             print("Cannot remove more passengers than there are!")

#     def __isub__(self, passengers):
#         self.__sub__(passengers)
#         return self

#     def __gt__(self, other):
#         return self.max_passengers > other.max_passengers

#     def __lt__(self, other):
#         return self.max_passengers < other.max_passengers

#     def __le__(self, other):
#         return self.max_passengers <= other.max_passengers

#     def __ge__(self, other):
#         return self.max_passengers >= other.max_passengers

#     def __str__(self):
#         return f"{self.model} (Max Passengers: {self.max_passengers}, Current Passengers: {self.current_passengers})"

# plane1 = Airplane("Boeing 737", 150, 100)
# plane2 = Airplane("Airbus A320", 180, 120)

# print(plane1 == plane2)  
# print(plane1 > plane2) 

# plane1 += 20  
# plane2 -= 30 

# print(plane1)
# print(plane2)
