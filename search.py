import sqlite3
import tkinter
win=tkinter.Tk()

db = sqlite3.connect('TEST.db')
cursor=db.cursor()
hart=["簡單","適中","困難"]
T=["上旬","中旬","下旬"]
def CurSelet(evt):
    deta.delete(0,'end')
    lineNum=int(listbox.curselection()[0])
    lineDeta=searchlist[lineNum]
    print(searchlist)
    print(lineDeta)
    for i in lineDeta:
        print(type(i))
    ################################
    a="ID："+str(lineDeta[0])
    deta.insert('end',a)
    a="植物名稱："+str(lineDeta[1])
    deta.insert('end',a)
    a="敘述："+str(lineDeta[2])
    deta.insert('end',a)
    a="科別："+str(lineDeta[3])
    deta.insert('end',a)
    a="播種期："+str(lineDeta[4])+"月"+str(T[lineDeta[5]-1])+"~"+str(lineDeta[6])+"月"+str(T[lineDeta[7]-1])
    deta.insert('end',a)
    a="收割期："+str(lineDeta[8])+"月"+str(T[lineDeta[9]-1])+"~"+str(lineDeta[10])+"月"+str(T[lineDeta[11]-1])
    deta.insert('end',a)
    a="難易度："+str(hart[lineDeta[12]-1])
    deta.insert('end',a)
    if lineDeta[14]==lineDeta[15]:
        a="連作間隔時間："+"間隔"+str(lineDeta[14])+"年"
        deta.insert('end',a)
    else:
        a="連作間隔時間："+"間隔"+str(lineDeta[14])+"~"+str(lineDeta[15])+"年"
        deta.insert('end',a)
    a="溫度："+"攝氏"+str(lineDeta[16])+"~"+str(lineDeta[17])+"度"
    deta.insert('end',a)
    if lineDeta[18]>0:
        a="盆箱大小："+str(lineDeta[18])+"公升以上"
        deta.insert('end',a)
    else:
        a="盆箱大小："+"無法盆箱栽培"
        deta.insert('end',a)
    
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
    global deta
    
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
    
    listbox=tkinter.Listbox(win,width=40)
    deta=tkinter.Listbox(win,width=80)
    
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

    listbox.grid(row=2,column=0,columnspan=2)
    deta.grid(row=2,column=2,columnspan=4)
    listbox.bind('<<ListboxSelect>>',CurSelet)
    

    btn=tkinter.Button(win, text="search", command=search)
    btn.grid(row=1,column=6)
    
def search():
    #名稱
    listbox.delete(0,'end')
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
    global searchlist
    searchlist=list(searchResult)
    searchlist.sort()
    for n in searchlist:
        print(n[1])
        a=str(n[0])+n[1]+'：'+n[2]
        listbox.insert('end',a)

setOpject()

win.mainloop()
db.close()

