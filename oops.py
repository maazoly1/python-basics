class Employee:
    a = 1
    def __init__(self, base_salary = 1):
        self.base_salary = base_salary
    
    # show default value of variable a means class value
    @classmethod
    def show(self):
        print(f"The value of a is {self.a}")

    # Property Decorator, now there is no self.name
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    # Setter Decorator
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    # operator overloading
    def __add__(self, salary):
        return self.base_salary + salary.base_salary

# obj = Employee()
# obj.a = 45
# obj.show()

# obj.name = "Maaz Mohammad"
# print(obj.name)

# a = Employee(10)
# b = Employee(20)
# print(a + b)

#create a class 2-d vector to create 3-d vector class

class twoDVector: 
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"{self.i}i x {self.j}j")
        

class threeDVector(twoDVector): 
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"{self.i}i x {self.j}j x {self.k}k")
        
# a = twoDVector(1,2)
# a.show()
# b = threeDVector(1,2,3)
# b.show()

# create an Employee class in which salary gets increment

class Employee:
    old_salary = 18000
    increment = 0

    @property
    def increment_after_salary(self):
        return self.increment
    
    @increment_after_salary.setter
    # finding percentage of increment from new salary and old salary
    def increment_after_salary(self, salary):
        self.increment = (salary/self.old_salary - 1)*100
    
# emp = Employee()
# emp.increment_after_salary = 25000
# print(emp.increment)

class ComplexN:
    def __init__(self, real_num):
        self.num = real_num

    def __add__(self, real_num):
        return ComplexN(self.num + real_num.num)

    def __mul__(self, real_num):
        return ComplexN(self.num * real_num.num)
    
    def __repr__(self):
        return str(self.num)
    
# num1 = ComplexN(1)
# num2 = ComplexN(2)

# print(num1 * num2)

# finding length of a list in class vector using operator overloading

class Vector:

    def __init__(self, l):
        self.list = l

    def __len__(self):
        return len(self.list)
    
v = Vector([1,2,3,4])

print(len(v))