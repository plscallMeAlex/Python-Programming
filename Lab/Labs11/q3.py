

class Name:
    def __init__(self, tt, fN, lN):
        self.tt = tt
        self.fN = fN
        self.lN = lN

    def getFullName(self):
        name = "{}. {} {}".format(self.tt, self.fN, self.lN)
        return name

class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def getDate(self):
        date = "{}/{}/{}".format(self.day, self.month, self.year)
        return date

    def getDateBC(self):
        date = "{}/{}/{}".format(self.day, self.month, (self.year + 543))
        return date
    
class Address:
    def __init__(self, houNO, street, district, city, country, postcode):
        self.houno = houNO
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcd = postcode

    def getAddress(self):
        address = "{} {} {} {} {} {}".format(self.houno, self.street, self.district, self.city, self.country, self.postcd)
        return address

class Department:
    def __init__(self, desc, mng, listEm=[]):
        self.description = desc
        self.manager = mng
        self.employeeList = listEm

    def addEmployee(self, e):
        self.employeeList.append(e)
        e.Department = self

    def deleteEmployee(self, e):
        self.employeeList.remove(e)
        e.Department = None

    def setManager(self, e):
        if isinstance(e, PermEmployee) and e in self.employeeList:
            self.manager = e

    def printInfo(self):
        print(f"Description: {self.description}")
        print(f"Manager: {self.manager.name.getFullName() if self.manager else 'None'}")
        print(f"Employee-List: {[emp.name.getFullName() for emp in self.employeeList]}")

class Person:
    def __init__(self, name, birthday, address):
        self.name = name
        self.birthday = birthday
        self.address = address

    def printInfo(self):
        print(f"Name: {self.name.getFullName()}")
        print(f"Birthday: {self.birthday.getDate()}")
        print(f"Address: {self.address.getAddress()}")

class Employee(Person):
    def __init__(self, name, birthday, address, startDate, department):
        super().__init__(name, birthday, address)
        self.startDate = startDate
        self.Department = department

    def printInfo(self):
        super().printInfo()
        print(f"Start Date: {self.startDate.getDate()}")
        print(f"Department: {self.Department.description}")

class Temp(Employee):
    def __init__(self, name, birthday, address, wage):
        super().__init__(name, birthday, address)
        self.wage = wage
    def printInfo(self):
        super().printInfo()
        print(self.wage)

class PermEmployee(Employee):
    def __init__(self, name, birthday, address, salary):
        super().__init__(name, birthday, address)
        self.salary = salary
    def printInfo(self):
        super().printInfo()
        print(self.salary)


# Example usage
name = Name("Mr.", "John", "Doe")
birthdate = Date(1, 1, 1990)
address = Address(123, "Sukhumvit", "Klongtoey", "Bangkok", "Thailand", 10110)
startDate = Date(1, 1, 2020)
department = Department("IT", None, [])
person = Person(name, birthdate, address)
person.printInfo()

employee = Employee(name, birthdate, address, startDate, department)
department.addEmployee(employee)
employee.printInfo()

