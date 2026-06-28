import tkinter as tk
from tkinter import messagebox
import csv
import os

def write_file():
    filename = fName.get()
    mode = entermode.get()
    if mode == "a" and not os.path.exists(filename):
        messagebox.showerror("Error", "File does not exist")
        return
    with open(filename, mode, newline="") as file:
        writer = csv.writer(file)

        if mode == "w":
            writer.writerow(["Name", "Mobile", "Email"])
        else:
            name = name_1.get()
            email = mail_1.get()
            mobile = numb_1.get()
            writer.writerow([name, email , mobile])

root = tk.Tk()
root.title("CSV GUI")
root.geometry("700x700")

label1 = tk.Label(root, text = "Enter File Name", font =('Ariel', 15))
label1.pack(pady="20")
fName = tk.Entry(root)
fName.pack()

label4 = tk.Label(root, text = "Choose mode, write: 'w', append: 'a'", font =('Ariel', 15))
label4.pack(pady="20")
entermode = tk.Entry(root)
entermode.pack()

label5 = tk.Label(root, text = 'To add data change mode to "a"', font =('Ariel', 15))
label5.pack(pady="20")

label2 = tk.Label(root, text = "Enter Name", font =('Ariel', 15))
label2.pack(pady="20")
name_1 = tk.Entry(root)
name_1.pack()

label3 = tk.Label(root, text = "Enter address", font =('Ariel', 15))
label3.pack(pady="20")
mail_1 = tk.Entry(root)
mail_1.pack()

label3 = tk.Label(root, text = "Enter number", font =('Ariel', 15))
label3.pack(pady="20")
numb_1 = tk.Entry(root)
numb_1.pack()

tk.Button(root, text="Submit", command=write_file, bg="blue").pack(pady="10")


root.mainloop()