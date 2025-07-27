#In python , function is a group of related statements that perform a specific task

#Function definition or declaration
def GreetMe(name):
    print("Good Morning! "+name)

#function call
GreetMe("Raghu")

#Function definition or declaration
def AddIntegers(a,b):
    return a+b

print(AddIntegers(3,5))

def CalculateAverage(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average

# Input values
a = 10
b = 20
c = 30

# Call the function and store the result
result = CalculateAverage(a, b, c)

# Print the expected output
print(f"The average of {a}, {b}, and {c} is {result}")