import math
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def printInfo(self):
        print(f"Position: {self.x}, {self.y};")

class Circle(Point):
    def __init__(self, x=0.0, y=0.0, r=0.0):
        super().__init__(x,y)
        self.r = r
    def area(self):
        area = math.pi * self.r * self.r
        return area
    def printInfo(self):
        print(f"Position: {self.x}, {self.y}; Radius: {self.r}; Area: {self.area()};")
    
ft = Circle(20,20, 10)
# print(ft.area())
ft.printInfo()


# class Name:
#     def __init__(self, tt, fN, lN):
#         self.tt = tt
#         self.fN = fN
#         self.lN = lN
#     def setName(self, t, f, l):
#         self.tt = t
#         self.fN = f
#         self.lN = l
#     def getFullName(self):
#         name = "{}. {} {}".format(self.tt, self.fN, self.lN)
#         return name

# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#     def setDate(self, d, m, y):
#         self.day = d
#         self.month = m
#         self.year = y
#     def getDate(self):
#         date = "{}/{}/{}".format(self.day, self.month, self.year)
#         return date
#     def getDateBC(self):
#         date = "{}/{}/{}".format(self.day, self.month, (self.year + 543))
#         return date
    
# class Address:
#     def __init__(self, houNO, street, district, city, country, postcode):
#         self.houno = houNO
#         self.street = street
#         self.district = district
#         self.city = city
#         self.country = country
#         self.postcd = postcode
#     def setAddress(self, houseNo, street, district, city, country, postcode):
#         self.houno = houseNo
#         self.street = street
#         self.district = district
#         self.city = city
#         self.country = country
#         self.postcd = postcode
#     def getAddress(self):
#         self.address = "{} {} {} {} {} {}".format(self.houno, self.street, self.district, self.city, self.country, self.postcd)
#         return self.address

# class Department:
#     def __init__(self, desc, mng, listEm= []):
#         self.description = desc
#         self.manager = mng
#         self.employeeList = listEm
#     def addEmployee(self, e):
#         self.employeeList.append(e)
#         e.Department = Department(self.description, self.manager, self.employeeList)
#     def deleteEmployee(self, e):
#         self.employeeList.remove(e)
#         e.Department = None
#     def setManager(self, e):
#         if e in self.employeeList:
#             self.manager = e
#     def printInfo(self):
#         print(f"Description: {self.description}")
#         print(f"Manager: {self.manager}")
#         print(f"Employee-List: {self.employeeList}")

# class Person:
#     def __init__(self, name, birthday, address):
#         super().__init__()
#         self.name = name
#         self.birthday = birthday
#         self.address = address
#     def printInfo(self):
#         print(f"Name: {self.name.getFullName()}")
#         print(f"Birthday: {self.birthday.getDate()}")
#         print(f"Address: {self.address.getAddress()}")

# class Employee(Person):
#     def __init__(self, name, birthday, address):
#         super().__init__(name, birthday, address)
#     def printInfo(self):
#         print(f"Name: {self.name}")
#         print(f"Birthday: {self.birthday}")
#         print(f"Address: {self.address}")
        

# class Temp(Employee):
#     def __init__(self, name, birthday, address, wage):
#         super().__init__(name, birthday, address)
#         self.wage = wage
#     def printInfo(self):
#         super().printInfo()
#         print(self.wage)

# class PermEmployee(Employee):
#     def __init__(self, name, birthday, address, salary):
#         super().__init__(name, birthday, address)
#         self.salary = salary
#     def printInfo(self):
#         super().printInfo()
#         print(self.salary)

# name = Name("Mr.", "John", "Doe")
# birthdate = Date(1, 1, 1990)
# adress = Address(123, "Sukhumvit", "Klongtoey", "Bangkok", "Thailand", 10110)
# startDate = Date(1, 1, 2020)
# person = Person(name, birthdate, adress)
# person.printInfo()



# department = Department("IT", None, [])
# employee = PermEmployee(name, birthdate, adress, startDate, department, 100000)
# employee.printInfo()

# department.add_employee(employee)
# department.printInfo()