file=open('text.txt')
#Read all the contents of file
#print(file.read())
#Read n number of characters by passing parameter
print("********")
print(file.read(3))
#read one single line at a time readLine()
# print(file.readline())
#file.close()
#print line by line using readLine method

# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

