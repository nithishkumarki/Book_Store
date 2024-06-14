from tkinter import *
import tkinter.messagebox as MessageBox

import mysql.connector as mysql

#tinker window
root= Tk ()
root.geometry("500x300")
root.title("BookStore")

#inser function
def Insert():
    id=id_entry.get()
    name=name_entry.get()
    cost=cost_entry.get()
    
    if(id=="" or name=="" or cost==""):
        MessageBox.showinfo("ALERT","Please enter all info")
    else:
        db=mysql.connect(host="localhost",user="root",password="password",database="bookstore_db")
        cursor=db.cursor()
        cursor.execute("insert into bookinfo values('" +id+"', '"+name+"', '"+cost+"' )")
        cursor.execute("commit")

        MessageBox.showinfo("Status","Purchase Sucessfull")
        db.close()
#delete fundtion
def delete():
 
    if(id_entry.get()==""):
        MessageBox.showinfo("ALERT","Please enter book id to remove")
    else:
        db=mysql.connect(host="localhost",user="root",password="password",database="bookstore_db")
        cursor=db.cursor()
        cursor.execute("delete from bookinfo where bookid='"+id_entry.get()+"'")
        cursor.execute("commit")

        id_entry.delete(0,'end')
        name_entry.delete(0,'end')
        cost_entry.delete(0,'end')
        
        MessageBox.showinfo("Status","Removed Sucessfull")


        db.close()
#update function
def update():
    id=id_entry.get()
    name=name_entry.get()
    cost=cost_entry.get()
    
    if(id=="" or name=="" or cost==""):
        MessageBox.showinfo("ALERT","Please enter all info")
    else:
        db=mysql.connect(host="localhost",user="root",password="password",database="bookstore_db")
        cursor=db.cursor()
        cursor.execute("update bookinfo set bookname='"+name+"', bookCost='"+cost+"' where bookid='"+id+"'")
        cursor.execute("commit")

        MessageBox.showinfo("Status","Book's info updated!!")
        db.close()
    
def select():
    id=id_entry.get()
    
    
    if(id==""):
        MessageBox.showinfo("ALERT","Please id to diplay book's info")
    else:
        db=mysql.connect(host="localhost",user="root",password="password",database="bookstore_db")
        cursor=db.cursor()
        cursor.execute("select * from bookinfo where bookid='"+id+"'")
        rows=cursor.fetchall()

        for row in rows:
            name_entry.insert(0,row[1])
            cost_entry.insert(0,row[2])
            
        cursor.execute("commit")

        # MessageBox.showinfo("Status","Book's info updated!!")
        db.close()
    

#UI
id=Label(root,text="BookID:",font=("verdana 15"))
id.place(x=50,y=30)
id_entry=Entry(root,font=("verdana 15"))
id_entry.place(x=150,y=30)

name=Label(root,text="BookTitle:",font=("verdana 15"))
name.place(x=50,y=80)
name_entry=Entry(root,font=("verdana 15"))
name_entry.place(x=150,y=80)

cost=Label(root,text="BookCost:",font=("verdana 15"))
cost.place(x=50,y=130)
cost_entry=Entry(root,font=("verdana 15"))
cost_entry.place(x=150,y=130)

btnInsert=Button(root,text="Buy",command=Insert,font=("verdana 15"))
btnInsert.place(x=80,y=190)

btnDelte=Button(root,text="Remove",command=delete,font=("verdana 15")).place(x=160,y=190)
btnDelte=Button(root,text="Update",command=update,font=("verdana 15")).place(x=280,y=190)
btnDelte=Button(root,text="display",command=select,font=("verdana 15")).place(x=400,y=190)


root.mainloop()