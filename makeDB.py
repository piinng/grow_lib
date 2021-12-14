import sqlite3
import pandas as pd

db = sqlite3.connect('TEST1.db')
cursor=db.cursor()
#cursor.execute('CREATE TABLE FV(ID INT,NAME STR,DESCRIPTION STR,DIVITION STR,SSM INT,SST INT,ESM INT,EST INT,SRM INT,SRT INT,ERM INT,ERT INT,DIFFICULTY INT,TEMPDN,TEMPUP INT,SIZE INT);')

#1.S:start,E:end
#2.S:sowing,R:reward
#3.M:month,T:ten day

bf=pd.read_excel('lib.xlsx')

for n in range(0,16):
    #a="INSERT INTO FV(ID,NAME,DESCRIPTION,DIVITION,SSM,SST,ESM,EST,SRM,SRT,ERM,ERT,DIFFICULTY,TEMPDN,TEMPUP,SIZE) VALUES(" +str(n+1)+","+str((bf.iat[n,1]))+","+str((bf.iat[n,2]))+","+str((bf.iat[n,3]))+"," +str(int(bf.iat[n,4]))+","+str(int(bf.iat[n,5]))+","+str(int(bf.iat[n,6]))+","+str(int(bf.iat[n,7]))+","+str(int(bf.iat[n,8]))+","+str(int(bf.iat[n,9]))+","+str(int(bf.iat[n,10]))+","+str(int(bf.iat[n,11]))+str(int(bf.iat[n,12]))+","+str(int(bf.iat[n,16]))+","+str(int(bf.iat[n,17]))+","+str(int(bf.iat[n,18]))+");"
    #                                                                                         ID                     NAME           DESCRIPTION              DIVITION                SSM                          SST                 ESM                     EST                       SRM                 SRT                  ERM                           ERT
    #print(bf)
    #print(bf.iat[n,12])
    a="INSERT INTO FV(ID,NAME,SSM,SST,ESM,EST,SRM,SRT,ERM,ERT,DIFFICULTY,TEMPDN,TEMPUP,SIZE) VALUES(%d,'%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d);"\
    %(int(n+1),str(bf.iat[n,1]),int(bf.iat[n,2]),int(bf.iat[n,3]),int(bf.iat[n,4]),int(bf.iat[n,5]),int(bf.iat[n,6]),int(bf.iat[n,7]),int(bf.iat[n,8]),int(bf.iat[n,9]),int(bf.iat[n,10]),int(bf.iat[n,14]),int(bf.iat[n,15]),int(bf.iat[n,16]))
    #print(a)
    cursor.execute(a)
    db.commit()


