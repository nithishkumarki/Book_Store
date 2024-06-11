import sqlite3
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the main window
root = Tk()
root.title("BOOK STORE")
root.geometry("1080x720")

# Load the background image
bg_image = Image.open("bg.jpg")
bg_image = bg_image.resize((1080, 720), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Treeview for displaying data
my_tree = ttk.Treeview(root)
storeName = "BOOK STORE"

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

def insert(id, name, price, quantity):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")

    cursor.execute("INSERT INTO inventory VALUES (?, ?, ?, ?)", (id, name, price, quantity))
    conn.commit()
    conn.close()

def delete(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")

    cursor.execute("DELETE FROM inventory WHERE itemId = ?", (data,))
    conn.commit()
    conn.close()

def update(id, name, price, quantity, idName):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")

    cursor.execute("UPDATE inventory SET itemId = ?, itemName = ?, itemPrice = ?, itemQuantity = ? WHERE itemId = ?", (id, name, price, quantity, idName))
    conn.commit()
    conn.close()

def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def insert_data():
    itemId = str(entryId.get())
    itemName = str(entryName.get())
    itemPrice = str(entryPrice.get())
    itemQuantity = str(entryQuantity.get())
    if itemId == "" or itemName == " ":
        print("Error Inserting Id")
    if itemName == "" or itemName == " ":
        print("Error Inserting Name")
    if itemPrice == "" or itemPrice == " ":
        print("Error Inserting Price")
    if itemQuantity == "" or itemQuantity == " ":
        print("Error Inserting Quantity")
    else:
        insert(str(itemId), str(itemName), str(itemPrice), str(itemQuantity))

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#f8f9fa')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def delete_data():
    selected_items = my_tree.selection()
    if not selected_items:
        print("No item selected to delete")
        return
    selected_item = selected_items[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#f8f9fa')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def update_data():
    selected_items = my_tree.selection()
    if not selected_items:
        print("No item selected to update")
        return
    selected_item = selected_items[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryId.get(), entryName.get(), entryPrice.get(), entryQuantity.get(), update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#f8f9fa')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

titleLabel = Label(root, text=storeName, font=('Helvetica', 30, 'bold'), bd=2, fg='#343a40', bg='#f8f9fa')
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20, sticky="ew")

idLabel = Label(root, text="BOOK_ID", font=('Helvetica', 15), fg='#343a40', bg='#f8f9fa')
nameLabel = Label(root, text="BOOK_Name", font=('Helvetica', 15), fg='#343a40', bg='#f8f9fa')
priceLabel = Label(root, text="Price", font=('Helvetica', 15), fg='#343a40', bg='#f8f9fa')
quantityLabel = Label(root, text="Quantity", font=('Helvetica', 15), fg='#343a40', bg='#f8f9fa')
idLabel.grid(row=1, column=0, padx=10, pady=10, sticky="e")
nameLabel.grid(row=2, column=0, padx=10, pady=10, sticky="e")
priceLabel.grid(row=3, column=0, padx=10, pady=10, sticky="e")
quantityLabel.grid(row=4, column=0, padx=10, pady=10, sticky="e")

entryId = Entry(root, width=25, bd=5, font=('Helvetica', 15))
entryName = Entry(root, width=25, bd=5, font=('Helvetica', 15))
entryPrice = Entry(root, width=25, bd=5, font=('Helvetica', 15))
entryQuantity = Entry(root, width=25, bd=5, font=('Helvetica', 15))
entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")
entryName.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="w")
entryPrice.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="w")
entryQuantity.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="w")

buttonFrame = Frame(root, bg='#f8f9fa')
buttonFrame.grid(row=5, column=1, columnspan=3, pady=20)

buttonEnter = Button(
    buttonFrame, text="Enter", padx=5, pady=5, width=10,
    bd=3, font=('Helvetica', 15), bg="#007bff", fg="white", command=insert_data)
buttonEnter.grid(row=0, column=0, padx=5, pady=5)

buttonUpdate = Button(
    buttonFrame, text="Update", padx=5, pady=5, width=10,
    bd=3, font=('Helvetica', 15), bg="#ffc107", fg="black", command=update_data)
buttonUpdate.grid(row=0, column=1, padx=5, pady=5)

buttonDelete = Button(
    buttonFrame, text="Delete", padx=5, pady=5, width=10,
    bd=3, font=('Helvetica', 15), bg="#dc3545", fg="white", command=delete_data)
buttonDelete.grid(row=0, column=2, padx=5, pady=5)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'), background="#f8f9fa", foreground="#343a40")
style.configure("Treeview", font=('Helvetica', 12), rowheight=25)

my_tree['columns'] = ("ID", "Name", "Price", "Quantity")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=100)
my_tree.column("Name", anchor=W, width=200)
my_tree.column("Price", anchor=W, width=150)
my_tree.column("Quantity", anchor=W, width=150)
my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Price", text="Price", anchor=W)
my_tree.heading("Quantity", text="Quantity", anchor=W)

for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#f8f9fa', font=('Helvetica', 12))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10, sticky="nsew")

root.mainloop()
