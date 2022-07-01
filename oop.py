# class Line:
#
#     def __init__(self, coord1=(0, 0), coord2=(0, 0)):
#         self.coord1 = coord1
#         self.coord2 = coord2
#
#     def distance(self):
#         return ((self.coord2[1] - self.coord1[1])**2 + (self.coord2[0] - self.coord1[0])**2)**0.5
#
#     def slope(self):
#         return (self.coord2[1] - self.coord1[1]) / (self.coord2[0] - self.coord1[0])
#
#
# coordin1 = (3, 2)
# coordin2 = (8, 10)
#
# my_line = Line(coordin1, coordin2)
#
# print(my_line.distance())
# print(my_line.slope())
#
#
# class Cylinder:
#
#     def __init__(self, height=1, radius=1):
#         self.radius = radius
#         self.height = height
#
#     def volume(self):
#         return 3.14 * self.radius**2 * self.height
#
#     def surface(self):
#         return 2 * 3.14 * self.radius * (self.height + self.radius)

# my_cyl = Cylinder(2, 3)
# print(my_cyl.volume())
# print(my_cyl.surface())




# class Fraction():
#     numerator = 5
#     denominator = 10
#
#     def print(self):
#         print(self.numerator)
#         # print('\u0332'.join(f'{self.numerator} '))
#         print(self.denominator)
#
#
#     def get_reversed(self):
#         print('Revers')
#         self.print()
#         rev_fr = Fraction()
#         rev_fr.numerator = self.denominator
#         rev_fr.denominator = self.numerator
#         rev_fr.print()
#
#     def reduce(self):
#         a = self.numerator
#         b = self.denominator
#         while a != b:
#             if a > b:
#                 a -= b
#             else:
#                 b -= a
#
#         if a != 1:
#             print('The fraction')
#             self.numerator //= a
#             self.denominator //= a
#             self.print()
#         else:
#             print('Cant be reduced')
#
# f1 = Fraction()
# f1.print()
# f1.get_reversed()
# f1.reduce()






