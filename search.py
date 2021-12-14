import sqlite3
import tkinter
win=tkinter.Tk()

db = sqlite3.connect('TEST1.db')
cursor=db.cursor()

def setOpject():
    global name
    name=tkinter.StringVar()
    global SM
    SM=tkinter.IntVar()
    global RM
    RM=tkinter.IntVar()
    global difficulty
    difficulty=tkinter.IntVar()
    global temp
    temp=tkinter.IntVar()
    global size
    size=tkinter.IntVar()
    global listbox
    
    e1=tkinter.Entry(win,textvariable=name)#名稱
    e5=tkinter.Entry(win,textvariable=SM)#播種月份
    e6=tkinter.Entry(win,textvariable=RM)#收穫月份
    e7=tkinter.Entry(win,textvariable=difficulty)#難易度
    e8=tkinter.Entry(win,textvariable=temp)#溫度
    e9=tkinter.Entry(win,textvariable=size)#盆箱大小
    
    l1=tkinter.Label(text='名稱')#名稱
    l5=tkinter.Label(text='播種月份')#播種月份
    l6=tkinter.Label(text='收穫月份')#收穫月份
    l7=tkinter.Label(text='難易度')#難易度
    l8=tkinter.Label(text='溫度')#溫度
    l9=tkinter.Label(text='盆箱大小')#盆箱大小
    
    listbox=tkinter.Listbox(win,width=130)
    
    e1.grid(row=1,column=0)
    e5.grid(row=1,column=1)
    e6.grid(row=1,column=2)
    e7.grid(row=1,column=3)
    e8.grid(row=1,column=4)
    e9.grid(row=1,column=5)
    
    l1.grid(row=0,column=0)
    l5.grid(row=0,column=1)
    l6.grid(row=0,column=2)
    l7.grid(row=0,column=3)
    l8.grid(row=0,column=4)
    l9.grid(row=0,column=5)
    listbox.grid(row=2,column=0,columnspan=7)
    
    btn=tkinter.Button(win, text="search", command=search)
    btn.grid(row=1,column=6)
    
def search():
    #名稱
    s="SELECT * FROM FV WHERE NAME LIKE '%"+name.get()+"%';"
    cursor.execute(s)
    searchName=set(cursor.fetchall())
    print(searchName)
    
    #播種月份
    if int(SM.get())!=0:
        s1=int(SM.get())
        s2="SELECT * FROM FV WHERE SSM <= %d;"%s1
        cursor.execute(s2)
        #print(type(cursor.fetchall()))
        sets2=set(cursor.fetchall())
        s3="SELECT * FROM FV WHERE ESM >= %d;"%s1
        cursor.execute(s3)
        sets3=set(cursor.fetchall())
        searchSM=sets2&sets3
        print(searchSM)
    else:
        cursor.execute("SELECT * FROM FV")
        searchSM=set(cursor.fetchall())
        print(searchSM)
    
    #收穫月份
    if int(RM.get())!=0:
        s1=int(RM.get())
        s2="SELECT * FROM FV WHERE SRM <= %d;"%s1
        cursor.execute(s2)
        sets2=set(cursor.fetchall())
        s3="SELECT * FROM FV WHERE ERM >= %d;"%s1
        cursor.execute(s3)
        sets3=set(cursor.fetchall())
        searchRM=sets2&sets3
        print(searchRM)
    else:
        cursor.execute("SELECT * FROM FV")
        searchRM=set(cursor.fetchall())
        print(searchRM)
    
    #難易度
    if int(difficulty.get())!=0:
        s1=int(difficulty.get())
        s2="SELECT * FROM FV WHERE DIFFICULTY <= %d;"%s1
        cursor.execute(s2)
        searchDifficulty=set(cursor.fetchall())
        print(searchDifficulty)
    else:
        cursor.execute("SELECT * FROM FV")
        searchDifficulty=set(cursor.fetchall())
        print(searchDifficulty)
    
    #溫度
    if int(temp.get())!=0:
        s1=int(temp.get())
        s2="SELECT * FROM FV WHERE TEMPUP <= %d;"%s1
        cursor.execute(s2)
        sets2=set(cursor.fetchall())
        s3="SELECT * FROM FV WHERE TEMPDN >= %d;"%s1
        cursor.execute(s3)
        sets3=set(cursor.fetchall())
        searchTemp=sets2&sets3
        print(searchTemp)
    else:
        cursor.execute("SELECT * FROM FV")
        searchTemp=set(cursor.fetchall())
        print(searchTemp)
        
    #盆箱大小
    if int(size.get())!=0:
        s1=int(size.get())
        s2="SELECT * FROM FV WHERE SIZE >= %d;"%s1
        cursor.execute(s2)
        searchSize=set(cursor.fetchall())
        print(searchSize)
    else:
        cursor.execute("SELECT * FROM FV")
        searchSize=set(cursor.fetchall())
        print(searchSize)
    
    searchResult=searchName&searchSM&searchRM&searchDifficulty&searchTemp&searchSize
    print()
    print()
    print()
    for n in searchResult:
        print(n[1])
        listbox.insert('end',n)

#======================================================
setOpject()

#db.close()
win.mainloop()

