class Employee(object):
    """docstring for ."""
    empCount = 0;
    def __init__(self, name, salary):
        self.name = name;
        self.salary = salary;
        Employee.empCount +=1;
    def displayCount(self):
        print("Total Employees {0}".format(Employee.empCount));
    def displayEmployee(self):
        print("Name : {0}, Salary : {1}".format(self.name, self.salary));

emp1 = Employee('Mohan',10000);
emp1.displayCount();
emp1.displayEmployee();
emp2 = Employee('Atul',15000);
emp2.displayCount();
emp2.displayEmployee();
emp3 = Employee('Vivek',12000);
emp3.displayCount();
emp3.displayEmployee();
