import sqlite3
import pandas as pd

db = sqlite3.connect('TEST.db')
cursor=db.cursor()
#cursor.execute('CREATE TABLE FV(ID INT,NAME STR,DESCRIPTION STR,DIVITION STR,SSM INT,SST INT,ESM INT,EST INT,SRM INT,SRT INT,ERM INT,ERT INT,DIFFICULTY INT,CONTINUE INT,CONDN INT,CONUP INT,TEMPDN,TEMPUP INT,SIZE INT);')

#1.S:start,E:end
#2.S:sowing,R:reward
#3.M:month,T:ten day

bf=pd.read_excel('lib.xlsx',sheet_name='果菜類')

for n in range(0,16):
    a="INSERT INTO FV(ID,NAME,DESCRIPTION,DIVITION,SSM,SST,ESM,EST,SRM,SRT,ERM,ERT,DIFFICULTY,CONTINUE,CONDN,CONUP,TEMPDN,TEMPUP,SIZE)VALUES(%d,'%s','%s','%s',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d);"\
       %(int(n+1),str(bf.iat[n,1]),str(bf.iat[n,2]),str(bf.iat[n,3]),int(bf.iat[n,4]),int(bf.iat[n,5]),int(bf.iat[n,6]),int(bf.iat[n,7]),int(bf.iat[n,8]),int(bf.iat[n,9]),int(bf.iat[n,10]),int(bf.iat[n,11]),int(bf.iat[n,12]),int(bf.iat[n,13]),int(bf.iat[n,14]),int(bf.iat[n,15]),int(bf.iat[n,16]),int(bf.iat[n,17]),int(bf.iat[n,18]))
    cursor.execute(a)
    db.commit()
db.close()