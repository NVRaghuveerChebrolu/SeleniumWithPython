#calsses are user defined blueprint ot datatype
#calculator : sum, mul, add, constant
#methods, class variables, instance variables , constructor...etc

#self keyword is mandatory when calling variables names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

#self is global and universal to call any variable

class Calculator:
    num=100  #class variables
    #default constructor : __init__ is the constructor

    def __init__(self,a,b):
        self.firstNumber=a #instance variables
        self.secondNumber=b
        print("I am constructor in parent class and i am called automatically when the object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(3,5)  #syntax to create objects in python
obj.getData()
print(obj.summation())

obj1= Calculator(4,8)  #syntax to create objects in python
obj1.getData()
print(obj1.summation())

