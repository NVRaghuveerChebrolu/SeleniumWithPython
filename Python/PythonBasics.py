print("hello")
# here are the comments i have defined

# In Python, we no need to specify any return type or explicitly mention any return type
# no need any semicolon at the end
# In Pycharm code indentation is very seriously considered .i.e how you defined the code.etc space alignment

a = 4
print(a)

Str="hello world"
print(Str)

a,b,c,d=3,5,6.4,"Great"
print(a,b,c,d)
# In python string concatenation is not allowed with integer and string but we can with same different data types)
#print ("value is "+b)
print(a+b)
#below is the way of using format method to concatinate different data types
print("{} {}".format("Value of a+b is",a+b))

#to know what type of data a variable is holding
print(type(b))
print(type(c))
print(type(d))

age =25
height =5.9
favorite_color ="blue"

print("{} {} {}".format("age",age,type(age)))
print("{} {} {}".format("height",height,type(height)))
print("{} {} {}".format("favorite_color",favorite_color,type(favorite_color)))

#data type list -> with square bracket : It allows multiple values and can be different data types
values = [1,4,"raghu",6,9]
#List is a data Type that allows multiple values and can be different data types.

print(values[3]) #6 is the output
print(values[2]) #raghu is the output
print(values[-1]) # 9 is output because in python -1 will give reference to the last element
print(values[1:3])# print n to n-1 index
values.insert(3,"chebrolu") # add value to the list on 3rd index
print(values)
values.append("End") #[1, 4, 'raghu', 'chebrolu', 6, 9, 'End']
print(values)
values[2]="veer" #[1, 4, 'veer', 'chebrolu', 6, 9, 'End']
print(values)
del values[0] #deletes the oth index
print (values) #[4, 'veer', 'chebrolu', 6, 9, 'End']

#data type Tuple -> #List and tuple does the samething but the only difference is that Tuple is immutable.
# you cannot change the existing behavior. You cannot modify it.
#Tuple is indicated with () and list is indicated with []
values = (1,4,"raghu",6.4)
print(values[2])
#values[2]="raghu"  #TypeError: 'tuple' object does not support item assignment

#Data type : Dictionary (similar to hashmap in java): store key and value pairs
#key should not be in inn ""
# string is indicated with " " and integer is not indicated with nay quotes.
dic={1:"first name", "last name":4, "abc":"hello world"}
print(dic["abc"])
print(dic[1])

# how to create dictionary at run time. Adding new values to dictionary is important
dictHello={}
dictHello["firstName"]="Raghuveer"
dictHello["lastName"]="Chebrolu"
dictHello["city"]="Hyderabad"
print(dictHello["firstName"])

#if block and loops in python
greeting ="good Morning"
if greeting =="Morning":
    print("condition matches")
    print("part of if block")
else:
    print("condition not matches")
    print("part of else block")
print("if else condition code is completed")

#for loop
obj =[2,3,5,8,10]
for i in obj:
    print(i*2)

# print sum of first five natural numbers 1+2+3+4+5=15
#for loop
# for(int i=1;i<=5;i+)   #in java
sum=0
for j in range(1,6):     #range(i,j) -> i = j-1
    sum=sum+j
print("{} {}".format("sum of 1 to 5 is ",sum))

print("******************")
#3rd argument : print the 3rd index
for k in range(1,10,3):
    print(k)

print("*****skipping first index*****")
#3rd argument : print the 3rd index
for m in range(10):
    print(m)

#while loop
print("****while loop****")
it = 10
while it>1:
    if it==9:
        it =it-1
        continue
    if it ==3:
        break
    print(it)
    it =it-1
print("while loop execution is done")
