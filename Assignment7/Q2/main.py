# Create a csv file for address book. 
# Create a program with structure having following options:
# 1. Add contact details(Name, Mobile, Email)
# 2. View Contacts
# 3. Exit
# your program should take input from user for name, mobile, email then create a list from this data and then append to the csv file:

import csv
import os

def create(filename):
    head =[
        ['Name', 'Mobile', 'Email']
    ]

    file = open(filename, 'w', newline="")

    writer = csv.writer(file)

    for row in head:
        writer.writerow(row)

def addDetails(filename):
        if os.path.exists(filename):
            info =[]
            ent = input("Enter name, mobile, email seperated by comma: ").split(",")
            info.append(ent)

            with open(filename, 'a', newline="") as file:

                writer = csv.writer(file) 

                for row in info:
                    writer.writerow(ent)
            ent = 0
        else:
            print("File does not exist")

def view(filename):
    if os.path.exists(filename):

        with open(filename , 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)
    else:
        print("File does not exist")

should_run = True
while True:
    if should_run:
        fn = str(input('Enter File Name: '))
        should_run = False
    c = int(input("Choose Option:" \
        "\n 1) Create File " \
        "\n 2) Enter Details" \
        "\n 3) View File" \
        "\n 4) Exit: "))

    if c == 1:
        create(fn)
    elif c == 2:
        addDetails(fn)
    elif c == 3:
        view(fn)
    elif c == 4:
        break
    else:
        print("invalid input")