# file = open('text.txt')
# file.close()

# read the file and store all elements int the list and reverse the list and write back to text file
#second argument r indicate reading the file and w indicates writing to file
with open('text.txt','r') as reader: #no need to write file .close when you use this line
    content=reader.readlines() # file contents will be avaiable
    reversed(content) # it is going to reverse the contents
    with open("text.txt",'w') as writer:
        for line in reversed(content):
            writer.write(line)