
#GUI code
from tkinter import *    # FOR GUI CREATION      
from tkinter.constants import CENTER
import sqlite3      # FOR DB PROCESS
import threading
from tkinter import messagebox

def auth_dict(usrnme,psswrd):
    global login_cred      
    if usrnme not in login_cred:
        login_cred['usrnme'] = psswrd      # ADDIN VALUES TO DICTIONARY
        return login_cred
    else:
        messagebox.showwarning("oops!" "USERNAME already exists")
    

def clear():                           # CLEARING ENTRY FIELDS
    global entry1,entry2
    entry1.delete(0,END)
    entry2.delete(0,END)
    
    
    # DB CODE

def db_register():  
    global usrnme,psswrd,new_dict
    global a
    a=str(auth_dict(usrnme,psswrd))
    con = sqlite3.connect('chat.db')
    c = con.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chat_table(id INTEGER PRIMARY KEY, usrnme TEXT)''')             # TABLE CREATION
    c.execute("INSERT INTO chat_table VALUES (NULL,x)", a)      # INSERTING VLUES DYNAMICALLY
    con.commit()    # SAVING THE CHANGE
    c.close()       # CURSOR CLOSING
    con.close()     # CONNECTION TO DB CLOSING
    
    clear()         # CALLING cLEAR METHOD TO EMPTY THE ENTRY FIELDS 

def login_auth():
    global usrnme,psswrd,a
    global entry1,entry2
    usrnme=entry1.get()
    psswrd=entry2.get()
    con = sqlite3.connect('chat.db')
    c = con.cursor()
    c.execute('SELECT * FROM chat_table')
    data = c.fetchall()
    if a['usrnme'] in data.values():
        messagebox.showinfo("Notification", "Login Successful!, Welcome to MiniChat")
    else:
        messagebox.showerror("Authentication failed" "check you login credential!")

    clear()         # CALLING CLEAR METHOD TO EMPTY THE ENTRY FIELDS
    
    
def submit():
    global usrnme, psswrd
    global entry1, entry2
    usrnme= entry1.get()
    psswrd= entry2.get()
    db_register()
    messagebox.showinfo("Notification", "Registration Successful!, Welcome to MiniChat")
    
def click1():
    global win
    global entry1,entry2
    win1=Toplevel(win)
    win1.geometry("700x250")
    win1.configure(bg = "azure2")
    label= Label(win1,compound=CENTER,text="Register",font = 'Arial 20 bold',fg = 'Blue',bg='azure2').grid(row=0, column=0)
    uname= Label(win1,compound=LEFT,text= 'Username:',bg = "azure2").grid(row=1, column=0, sticky=E)
    psswd= Label(win1,compound=LEFT,text= 'Password:',bg = "azure2").grid(row=2, column=0, sticky=E)
    entry1= Entry(win1,width=20)
    entry2= Entry(win1,width=20)
    entry1.grid(row=1, column=1,sticky=W)
    entry2.grid(row=2, column=1,sticky=W)
    b1= Button(win1, width=7,text="ok",command=submit).grid(row=4, column=0, sticky=W)
    b2= Button(win1, width=7,text="cancel",command=clear).grid(row=4, column=1, sticky=W)

def click2(): 
    global win
    global entry1,entry2
    win2= Toplevel(win)  
    win2.geometry("700x250")
    win2.configure(bg = "azure2")
    label= Label(win2,compound=CENTER,text="Login",font = 'Arial 20 bold',fg = 'Blue',bg='azure2').grid(row=0, column=0)
    uname= Label(win2,compound=LEFT,text= 'Username:',bg = "azure2").grid(row=1, column=0, sticky=E)
    psswd= Label(win2,compound=LEFT,text= 'Password:',bg = "azure2").grid(row=2, column=0, sticky=E)
    entry1= Entry(win2,width=20)
    entry2= Entry(win2,width=20)
    entry1.grid(row=1, column=1,sticky=W)
    entry2.grid(row=2, column=1,sticky=W)
    b1= Button(win2, width=7,text="ok",command=login_auth).grid(row=4, column=0, sticky=W)
    b2= Button(win2, width=7,text="cancel",command=clear).grid(row=4, column=1, sticky=W)


def main(): 
    global win 
    win = Tk()            #calling window creating function (instance)
    win.title("chat")  
    win.geometry("700x250")          #name of the window
    win.configure(bg = "azure2")
    label= Label(win,compound=CENTER,text="hello, welcome to chat application",font = 'Arial 20 bold',fg = 'Blue',bg='azure2')
    label.pack()
    b1= Button(win,text="Register",command=click1, height=1, width=10,font = 'Arial',fg = 'Blue',bg='azure2').pack()
    b2= Button(win,text="Login",command=click2, height=1, width=10,font = 'Arial',fg = 'Blue',bg='azure2').pack()
    global login_cred
    login_cred={}
    
main()
win.mainloop()              #only then window process starts
