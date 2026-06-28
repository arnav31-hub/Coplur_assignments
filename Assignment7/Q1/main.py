#Q1. Create a text file and add topics covered in today's session(each topic in a new line):

file = open('Class_7_topics.txt', 'w')
file.write("Topics Covered in Today's class:" \
"\n 1) How to Create/edit a File using python python" \
"\n 2) What is CSV file" \
"\n 3) How to create/edit a csv file using python" \
"\n 4) Use of OS.path Module to check if a file exists")

print("Class_7_topics.txt Created")

file = open("Class_7_topics.txt", "r")

for each in file:
    print(each, end="")