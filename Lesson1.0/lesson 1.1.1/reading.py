
#Reading content from a text file
with open('Lesson1.0/invoice.txt','r')as file:
    content = file.read()
    print(content)

#Reading lines in a file
with open('Lesson1.0/invoice.txt','r')as file:
    for line in file:
        print(line.strip())

#Parsing the number of lines in text file
with open('/home/decoder/Desktop/Courses/Document-parsing/Lesson1.0/lesson 1.1.1/invoice.txt','r')as file:
    lines = file.readlines()
    for line in lines:
        print(line,end="**\n")
