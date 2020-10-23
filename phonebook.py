import tkinter as tk
root=tk.Tk()
root.title("MY PHONEBOOK")
root.configure(bg='black')
tk.Label(root,text="PHONEBOOK",font='times 30 bold',fg='orange',bg='black').grid(row=1,column=0)
tk.Label(root,bg='black').grid(row=2,column=0)
logo=tk.PhotoImage(file = r"C:\Users\Ashish Gupta\Documents\Python\Project Phonebook\my.gif")
tk.Label(root,image=logo).grid(row=3,column=0)
tk.Label(root,bg='black').grid(row=4,column=0)
tk.Label(root,text='    NAME= ASHISH GUPTA     ',font='times 20 bold',fg='orange',bg='black').grid(row=5,column=0)
tk.Label(root,text='    ER_NO=181B054     ',font='times 20 bold',fg='orange',bg='black').grid(row=6,column=0)
def fun():
    root.destroy()
    root1=tk.Tk()
    root1.title('CHOICE')
    root1.configure(bg='black')
    
    import sqlite3
    con=sqlite3.Connection('phonne')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS PBOOK(ID INTEGER PRIMARY KEY AUTOINCREMENT,FNAME VARCHAR(20),LNAME VARCHAR(20),DOB DATE,CITY VARCHAR(20),PINCODE INT,EMAIL_ID VARCHAR(15),COMPANY VARCHAR(30),WEBSITE_URL VARCHAR(20),PHONE_NO NUMBER(10))')
    
    def close():
        root1.destroy()
    def add():
        root2=tk.Tk()
        root2.title('ADD CONTACT')
        root2.configure(bg='black')

        tk.Label(root2,text=' __New Contact__ ',font='times 15 bold',fg='orange',bg='black').grid(row=1,column=0)
        tk.Label(root2,bg='black').grid(row=3,column=0)
        tk.Label(root2,text='FIRST NAME:',fg='orange',bg='black',font='times 10 bold').grid(row=5,column=0,sticky=tk.W)
        a1=tk.Entry(root2)
        a1.grid(row=5,column=1)
        tk.Label(root2,text='LAST NAME:',fg='orange',bg='black',font='times 10 bold').grid(row=6,column=0,sticky=tk.W)
        a2=tk.Entry(root2)
        a2.grid(row=6,column=1)
        tk.Label(root2,text='DOB:',fg='orange',bg='black',font='times 10 bold').grid(row=7,column=0,sticky=tk.W)
        a3=tk.Entry(root2)
        a3.grid(row=7,column=1)
        tk.Label(root2,text='CITY:',fg='orange',bg='black',font='times 10 bold').grid(row=8,column=0,sticky=tk.W)
        a4=tk.Entry(root2)
        a4.grid(row=8,column=1)
        tk.Label(root2,text='PINCODE:',fg='orange',bg='black',font='times 10 bold').grid(row=9,column=0,sticky=tk.W)
        a5=tk.Entry(root2)
        a5.grid(row=9,column=1)
        tk.Label(root2,text='EMAIL_ID:',fg='orange',bg='black',font='times 10 bold').grid(row=10,column=0,sticky=tk.W)
        a6=tk.Entry(root2)
        a6.grid(row=10,column=1)
        tk.Label(root2,text='COMPANY:',fg='orange',bg='black',font='times 10 bold').grid(row=11,column=0,sticky=tk.W)
        a7=tk.Entry(root2)
        a7.grid(row=11,column=1)
        tk.Label(root2,text='WEBSITE URL:',fg='orange',bg='black',font='times 10 bold').grid(row=12,column=0,sticky=tk.W)
        a8=tk.Entry(root2)
        a8.grid(row=12,column=1)
        tk.Label(root2,text='PHONE NO:',fg='orange',bg='black',font='times 10 bold').grid(row=13,column=0,sticky=tk.W)
        a9=tk.Entry(root2)
        a9.grid(row=13,column=1)
        tk.Label(root2,bg='black').grid(row=14,column=0)

        def save():
            a,b,c,d,e,f,g,h,i=a1.get(),a2.get(),a3.get(),a4.get(),a5.get(),a6.get(),a7.get(),a8.get(),a9.get()
            a1.delete(0,tk.END)
            a2.delete(0,tk.END)
            a3.delete(0,tk.END)
            a4.delete(0,tk.END)
            a5.delete(0,tk.END)
            a6.delete(0,tk.END)
            a7.delete(0,tk.END)
            a8.delete(0,tk.END)
            a9.delete(0,tk.END)
            cur.execute('INSERT INTO PBOOK (FNAME,LNAME,DOB,CITY,PINCODE,EMAIL_ID,COMPANY,WEBSITE_URL,PHONE_NO) VALUES (?,?,?,?,?,?,?,?,?)',(a,b,c,d,e,f,g,h,i))
            con.commit()
            cur.execute('SELECT * FROM PBOOK')
            root5=tk.Tk()
            root5.title('SAVED')
            root5.configure(bg='black')
            root5.geometry('190x120')
            tk.Label(root5,bg='black').grid(row=0,column=0)
            tk.Label(root5,bg='black').grid(row=1,column=0)
            def ok1():
                root5.destroy()
                root2.destroy()
            tk.Label(root5,text='                Contact Saved                 ',bg='black',fg='orange').grid(row=3,column=0)
            tk.Button(root5,text='  OK  ' ,fg='orange',bg='black',command=ok1).grid(row=4,column=0)
        tk.Button(root2,text='SAVE',fg='orange',bg='black',font='times 15 bold',command=save).grid(row=15,column=0,sticky=tk.E)
        
    def search():
        root4=tk.Tk()
        root4.title('SEARCH')
        root4.configure(bg='black')
        tk.Label(root4,text='__ENTER NAME__',fg='orange',bg='black',font='times 15 bold').grid(row=1,column=0)
        x1=tk.Entry(root4,width=50)
        x1.grid(row=2,column=0,columnspan=66)
        lb=tk.Listbox(root4,height=15,width=50,highlightcolor='orange',selectbackground='orange',selectforeground='black')
        tk.Label(root4,bg='black').grid(row=3,column=0)
        lb.grid(row=4,column=0)
        x=cur.execute('SELECT FNAME,LNAME FROM PBOOK')
        for i in x:
            lb.insert(tk.END,i)
        def  fun1(l=1):
            f=[1]
            f[0]=['%'+x1.get()+'%']
            lb.delete(0,tk.END)
            h=cur.execute('SELECT FNAME,LNAME FROM PBOOK WHERE FNAME LIKE ?',(f[0]))
            for i in h:
                lb.insert(tk.END,i)
        root4.bind('<Key>',fun1)
        def fn():
            root6=tk.Tk()
            root6.configure(bg='black')
            root6.title('DETAILS')
            root6.geometry('370x320')
            v1=lb.curselection()
            v2=lb.get(v1)
            cur.execute('SELECT ID FROM PBOOK WHERE FNAME=(?) AND LNAME=(?)',(v2[0],v2[1]))
            x=cur.fetchall()
            for i in x:
                for j in i:
                    sn=j
            val1=cur.execute('SELECT  * FROM PBOOK WHERE ID=(?)',(sn,))
            for i in val1:
                tk.Label(root6,text='__CONTACT DETAILS__',bg='black',fg='orange',font='times 12 bold').grid(row=1,column=0,sticky=tk.W)
                tk.Label(root6,bg='black').grid(row=2,column=0)
                
                tk.Label(root6,text='FIRST NAME : ',bg='black',fg='orange',font='times 12 bold').grid(row=3,column=0,sticky=tk.W)
                tk.Label(root6,text=i[1],bg='black',fg='orange',font='times 10 bold').grid(row=3,column=1)
                
                tk.Label(root6,text='LAST NAME : ',bg='black',fg='orange',font='times 12 bold').grid(row=4,column=0,sticky=tk.W)
                tk.Label(root6,text=i[2],bg='black',fg='orange',font='times 10 bold').grid(row=4,column=1)

                tk.Label(root6,text='DOB : ',bg='black',fg='orange',font='times 12 bold').grid(row=5,column=0,sticky=tk.W)
                tk.Label(root6,text=i[3],bg='black',fg='orange',font='times 10 bold').grid(row=5,column=1)
                
                tk.Label(root6,text='CITY : ',bg='black',fg='orange',font='times 12 bold').grid(row=6,column=0,sticky=tk.W)
                tk.Label(root6,text=i[4],bg='black',fg='orange',font='times 10 bold').grid(row=6,column=1)
                
                tk.Label(root6,text='PINCODE : ',bg='black',fg='orange',font='times 12 bold').grid(row=7,column=0,sticky=tk.W)
                tk.Label(root6,text=i[5],bg='black',fg='orange',font='times 10 bold').grid(row=7,column=1)
                
                tk.Label(root6,text='EMAIL_ID : ',bg='black',fg='orange',font='times 12 bold').grid(row=8,column=0,sticky=tk.W)
                tk.Label(root6,text=i[6],bg='black',fg='orange',font='times 10 bold').grid(row=8,column=1)
                
                tk.Label(root6,text='COMPANY: ',bg='black',fg='orange',font='times 12 bold').grid(row=9,column=0,sticky=tk.W)
                tk.Label(root6,text=i[7],bg='black',fg='orange',font='times 10 bold').grid(row=9,column=1)
                
                tk.Label(root6,text='WEBSITE_URL: ',bg='black',fg='orange',font='times 12 bold').grid(row=10,column=0,sticky=tk.W)
                tk.Label(root6,text=i[8],bg='black',fg='orange',font='times 10 bold').grid(row=10,column=1)
                
                tk.Label(root6,text='PHONE_NO : ',bg='black',fg='orange',font='times 12 bold').grid(row=11,column=0,sticky=tk.W)
                tk.Label(root6,text=i[9],bg='black',fg='orange',font='times 10 bold').grid(row=11,column=1)

            def remove():
                cur.execute('DELETE FROM PBOOK WHERE ID=(?)',(sn,))
                con.commit()
                root6.destroy()
                root4.destroy()
                search()
            tk.Label(root6,bg='black').grid(row=13,column=0)   
            tk.Button(root6,text='DELETE',command=remove,font='times 10 bold',bg='black',fg='orange').grid(row=14,column=0,sticky=tk.W)
            
            def ok():
                root6.destroy()
            tk.Button(root6,text='      OK     ',font='times 10 bold',bg='black',fg='orange',command=ok).grid(row=14,column=1)
        lb.bind("<<ListboxSelect>>",lambda x:fn() )
        
    def delete():
        search()
         
    tk.Label(root1,text=' WELCOME TO PHONEBOOK',font='times 15 bold',fg='orange',bg='black').grid(row=1,column=0)
    tk.Label(root1,text='-----------------------------------------',font='times 15 bold',fg='orange',bg='black').grid(row=2,column=0)
    tk.Label(root1,bg='black').grid(row=3,column=0)
    tk.Button(root1,text='      ADD CONTACT      ',font='times 10 bold',fg='orange',bg='black',command=add).grid(row=4,column=0,sticky=tk.W)
    tk.Button(root1,text='            SEARCH             ',font='times 10 bold',fg='orange',bg='black',command=search).grid(row=6,column=0,sticky=tk.W)
    tk.Button(root1,text='             DELETE              ',font='times 10 bold',fg='orange',bg='black',command=delete).grid(row=7,column=0,sticky=tk.W)
    tk.Button(root1,text='                EXIT                 ',font='times 10 bold',fg='orange',bg='black',command=close).grid(row=8,column=0,sticky=tk.W)
    tk.Label(root1,bg='black').grid(row=9,column=0)
    tk.Label(root1,bg='black').grid(row=10,column=0)

tk.Label(root,bg='black').grid(row=7,column=0)
tk.Button(root,text='PRESS',font='times 15 bold',command=fun,fg='orange',bg='black').grid(row=8,column=0)
tk.Label(root,bg='black').grid(row=9,column=0)
root.mainloop()
