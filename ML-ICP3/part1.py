#Declaring employee class and creating default constructor, employee number function, and employee average salary function
class employee:
    averagesalary = 0
    numberofemployees = 0
    def __init_(self,name,family,salary,department):
        self.name = ""
        self.family = ""
        self.salary= 0
        self.department = ""
    def employeenum(self):
        self.__class__.numberofemployees += 1
    def average(self,salary,numberofemployees):
        self.__class__.averagesalary += self.salary/numberofemployees

#Creating fulltimeemployee class that inherits from employee class, setting number of full time employees to 0
class fulltimeemployee(employee):
    def __init__ (self, numberoffulltime):
        self.numberoffulltime = 0





