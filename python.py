import csv, json
import pandas as pd
import numpy  as np
import urllib.request as url
import matplotlib.pyplot as pt
import requests
response=url.urlopen("https://api.covid19india.org/raw_data.json")
temp_data=json.load(response)
file=pd.DataFrame(temp_data["raw_data"])

print('covid data is READY TO USE :')
print()
file.fillna("undefined", inplace = True) 
#line graph
print('In this line graph the gender is represented:')
f=0
m=0
ud=0
for i in file['gender']:
    if(i=='M'):m=m+1
    elif(i=='F'):f=f+1
    else:ud=ud+1
print("-----> male :",m)
print("-----> female :",f)
print("-----> undefined :",ud)

gender=["Male","Female","Undefined"]
value=[m,f,ud]
pt.title("COVID_19 DATA")
pt.xlabel("Gender")
pt.ylabel("Total number of people")
pt.plot(gender,value,color='red')
pt.grid(True)
pt.show()


#bar graph
print('In this bar graph the current status is represented:')
rec=0
hop=0
dea=0
mig=0
uda=0
for i in file['currentstatus']:
    if(i=='Recovered'):rec=rec+1
    elif(i=='Hospitalized'):hop=hop+1
    elif(i=='Deceased'):dea=dea+1
    elif(i=='Migrated'):mig=mig+1
    else:uda+=1
print("-----> Recovered :",rec)
print("-----> Hospitalized :",hop)
print("-----> Deceased :",dea)
print("-----> Migrated :",mig)
print("-----> Undefined :",uda)

pt.title("COVID_19 DATA")
ob=("Recovered","Hospitalized","Deceased","Migrated","Undefined")
z=np.arange(len(ob))
val=[rec,hop,dea,mig,uda]
pt.xlabel("Current Status")
pt.ylabel("Total number of people")
toplabel=pt.bar(z,val,color=['green', 'orange', 'black', 'red', 'blue'])
pt.xticks(z,ob)
pt.grid(True)
for i in toplabel:
    height = i.get_height()
    pt.text(i.get_x() + i.get_width()/2, 1*height,height,ha='center', va='bottom')

pt.show()


#pie chart
print('In this pie chart the age is represented:')
un=0
a1=0
a2=0
a3=0
a4=0
a5=0
for i in file['agebracket']:
    if(i>='0' and i<='20'):a1+=1
    elif(i>='21' and i<='40'):a2+=1
    elif(i>='41' and i<='60'):a3+=1
    elif(i>='61' and i<='80'):a4+=1
    elif(i>='81' and i<='100'):a5+=1
    else:un+=1
print("-----> 0-20 :",a1)
print("-----> 21-40 :",a2)
print("-----> 41-60 :",a3)
print("-----> 61-80 :",a4)
print("-----> 81-100 :",a5)
print("-----> Undefined :",un)
fig = pt.figure()
ax = fig.add_axes([0,0,1,1])
lab = ['0-20', '21-40', '41-60', '61-80', '81-100','Undefined']
coviddata = [a1,a2,a3,a4,a5,un]
pt.title("COVID_19 DATA")
pt.grid(True)
ax.pie(coviddata, labels = lab,autopct='%1.2f%%')
pt.show()
