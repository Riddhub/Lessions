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


# class Point:
#     "New class"
#     color = 'red'
#     circle = 2
#
#  a.__dict__
# Point.__doc__
#
# Point.type_pt = 'disc'
# setattr(Point, 'type_pt', 'square')
#
# Point.color
# getattr(Point, 'a', False)
#
# hasattr(Point, 'prob')
#
# del Point.prop
# delattr(Point, 'type_pt')


# class Point:
#     "New class"
#     color = 'red'
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# pt = Point()
# pt2 = Point()
# pt.set_coords(1, 2)
# pt2.set_coords(10, 20)
# print(pt.__dict__)
# print(pt2.__dict__)
#
# print(pt.get_coords())
# f = getattr(pt, 'get_coords')
# print(f())

######################## INITIALIZATION AND FINALIZATION ##################

# class Point:
#     'New class'
#     color = 'red'
#     circle = 2
#
#     def __init__(self, x=0, y=0):
#         print('call __init__')
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Deleting instance: ' + str(self))
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# pt = Point(1, 2)
# print(pt.__dict__)


###########################  MAGIC METHOD #####################

# class Point:
#     'New class'
#     color = 'red'
#     circle = 2
#
#     def __new__(cls, *args, **kwargs):
#         print('call __new__ for ' + str(cls))
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print('call __init__ for ')
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# print(pt)


#######################  SINGLETON (SIMPLE) ###############################

# class Database:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#
#     def __del__(self):
#         Database.__instance = None
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f'connecting witt DB: {self.user}, {self.psw}, {self.port}')
#
#     def close(self):
#         print('close connect with DB')
#
#     def read(self):
#         return 'data from DB'
#
#     def write(self, data):
#         print(f'write in DB {data}')
#
# db = Database('root', '1234', 80)
# db2 = Database('root2', '124', 40)
# print(id(db), id(db2))
# print(db.__dict__)


######################### DECARATION:  Methods ######################

# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD
#
#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#
#         print(self.norm2(self.x, self.y))
#
#     @staticmethod
#     def norm2(x, y):
#         return x*x + y*y
#
#     def get_coord(self):
#         return self.x, self.y
#
#
# v = Vector(1, 20)
# gc = Vector.get_coord(v)
# print(gc)
# print(Vector.validate(5))
# print(Vector.norm2(5, 6))


