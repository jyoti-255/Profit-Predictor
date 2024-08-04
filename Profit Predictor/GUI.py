from tkinter import *
from tkinter.messagebox import *
from pickle import *
import os
import sys

def resource_path2(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()
root.title("Profit Predictor")
root.geometry("700x600+50+50")
f = ("Century", 35, "bold")

# Load the model
with open("company.pkl", "rb") as f1:
    model = load(f1)

def find():
    try:
        rnd = float(ent_rnd.get())
        adm = float(ent_adm.get())  
        mar = float(ent_mar.get())  
    except ValueError:
        showerror("Issue", "R&D spend, Administration, and Marketing Spend should be in numbers only")
        ent_rnd.delete(0, END)
        ent_adm.delete(0, END)
        ent_mar.delete(0, END)
        ent_rnd.focus()
        return
    profit = model.predict([[rnd, adm, mar]])
    msg = "Profit: " + str(round(profit[0], 2))
    showinfo("Profit", msg)
    ent_rnd.delete(0, END)
    ent_adm.delete(0, END)
    ent_mar.delete(0, END)
    ent_rnd.focus()

lab_title = Label(root, text="Profit Predictor", font=f)
lab_rnd = Label(root, text="Enter R&D spend", font=f)
ent_rnd = Entry(root, font=f)
lab_adm = Label(root, text="Enter Administration spend", font=f)
ent_adm = Entry(root, font=f)
lab_mar = Label(root, text="Enter Marketing spend", font=f)
ent_mar = Entry(root, font=f)

btn_find = Button(root, text="Find Profit", font=f, command=find)

lab_title.pack(pady=20)
lab_rnd.pack(pady=5)
ent_rnd.pack(pady=5)
lab_adm.pack(pady=5)
ent_adm.pack(pady=5)
lab_mar.pack(pady=5)
ent_mar.pack(pady=5)
btn_find.pack(pady=20)

root.mainloop()
