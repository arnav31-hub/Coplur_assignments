#1)Write a python program that takes in a student name, class. It should also take in five subject marks of the students and find the total mark and percentage. Display a result in such a way that their name, class,  and percentage are printed:

#Taking name and class from user
name = input("Enter student's name: ")
Class = input("Enter student's class: ")

#Taking subjects marks from user
hindi = int(input("Enter marks in subject Hindi: "))
science = int(input("Enter marks in subject Science: "))
math = int(input("Enter marks in subject Math: "))
sst = int(input("Enter marks in subject SST: "))
computer = int(input("Enter marks in subject Computer: "))

#Calculating total marks and percentage
total_marks = hindi + science + math + sst + computer
percentage = float((total_marks/500)*100)

#Printing result of given student and marks
print("Name of student:",name)
print("Class of student:",Class)
print("Percentage:",percentage) 