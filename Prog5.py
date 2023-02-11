#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:22:26 2021

@author: mohanthapa
"""

def zeller(dmy):
    century=20
    month = int(dmy[2:4])-2
    year = int(dmy[:2])
    if month<= 0:
        month=month+12
        year-=1
    d = int(dmy[4:])
    w=(13*month-1)//5
    x=year//4
    y=century//4
    z=w+x+y+d-(2*century)+year
    r = z%7
    days =['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    return days[r]
    

   

fd = open("2015HomicideLog_FINAL.txt", "r")
ax = fd.read().splitlines()
days =['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
d=[]
dayscount={'Sunday':0,'Monday':0,'Tuesday':0,'Wednesday':0,'Thrusday':0,'Friday':0,'Saturday':0}

age_cat={"0-10":0,"10-20":0,"20-30":0,"30-40":0,"40-50":0,"50-60":0,"60-70":0,"70-80":0,"80-90":0,"90<":0}
race={}
racep={}
pgenrace={}
genracep = {}
gender={"M":0,"F":0}
genderp={"M":"%","F":"%"}
timecount={'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,'0':0}

for lines in ax:
    alllines = lines.split("\t")
    print(alllines)
    print(alllines[0])
    day = (zeller(alllines[0]))
    print("This occured on",day)    #Homicide occured in each day.
     
    



for line in ax:
    dmy =line.split("\t")[0]
    a=zeller(dmy)
    d.append(a)
    dayscount[a]+=1
    
print(dayscount) # Number of homicide each day
  


for line in ax:
    time =line.split("\t")[2].split(":")[0]
    if(time in timecount.keys()):
        timecount[time]=timecount[time]+1
    else:
        timecount[time] =1
print(timecount)  #Number of Homicide occured in each hour in 24 hr clock.  


                               




for line in ax:
    genrace=""
    age =""
    if(len(line.split("\t"))>5):
        genrace = line.split("\t")[4]
        age = line.split("\t")[5][0:2]
        
    else:
        genrace = line.split()[3]
        age = line.split()[4][0:2]
    rac = genrace[0]
    age=int(age)
    if(age>=0 and age<10):age_cat["0-10"]+=1
    if(age>=10 and age<20):age_cat["10-20"]+=1
    if(age>=20 and age<30):age_cat["20-30"]+=1
    if(age>=30 and age<40):age_cat["30-40"]+=1
    if(age>=40 and age<50):age_cat["40-50"]+=1
    if(age>=50 and age<60):age_cat["50-60"]+=1
    if(age>=60 and age<70):age_cat["60-70"]+=1
    if(age>=70 and age<80):age_cat["70-80"]+=1
    if(age>=80 and age<90):age_cat["80-90"]+=1
    if(age>=90):age_cat["90<"]+=1
    gen=genrace[1:]
    gender[gen]=gender[gen]+1
    if(rac in race.keys()):
        race[rac] = race[rac]+1
    else:
        race[rac] =1
        
    if genrace in pgenrace.keys():
        pgenrace[genrace] +=1
    else:
        pgenrace[genrace] =1
print(race) #number of homicide based om race.
print(gender)#number of homicide based on sex.
print(age_cat,"Age Total")#number of homicide based on age category.
for key in race:
    racep[key] = "{:.2f}%".format((race[key]/133)*100)
    
for key in gender:
    genderp[key]="{:.2f}%".format((gender[key]/133)*100)
for key in pgenrace.keys():
    genracep[key]= "{:.2f}%".format((pgenrace[key]/133)*100)
   
    
    
print("Race Percentage:\t",racep)#percentage of homicide based on race
print("Gender percentage:\t",genderp)#percentage of homicide based on sex.
print("Genrace percentage:\t",genracep)





import pylab
bar_width=0.5
x_values=[1,2,3,4,5,6,7]
y_values=[13,25,17,26,19,14,19]
tlabel=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
pylab.title("Homicide Occurrence by Day of Week")
pylab.bar(x_values,y_values,width=bar_width,tick_label=tlabel, align='center',color='b')
pylab.show()


import pylab
pylab.axes(aspect=1) # make aspect ratio even so we get a circle
values=[29.32,8.27,23.31,4.51,0.75,0.75,21.80,11.28]
pie_labels=["BM","BF","HM","HF","AM","AF","WM","WF"]
color_list=['purple','green','blue','cyan','yellow','maroon','red','white']
pylab.pie(values,autopct='%1.f%%',labels=pie_labels,colors=color_list)
pylab.title("Pie Chart Showing Racial and Gender Breakdown")
pylab.show()






import pylab
bar_width=0.5
x_values=[1,2,3,4,5,6,7,8,9,10]
y_values=[4,7,27,41,25,15,7,5,2,0]
tlabel=["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90<"]
pylab.title("Homicide Occurrence by each age range category")
pylab.bar(x_values,y_values,width=bar_width,tick_label=tlabel, align='center',color='b')
pylab.show()






import pylab
bar_width=0.5
x_values=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
y_values=[3,7,1,4,6,4,4,4,5,5,3,8,4,5,2,5,13,10,6,7,5,13,6,3]
tlabel=["1hr","2hr","3hr","4hr","5hr","6hr","7hr","8hr","9hr","10hr","11hr","12hr","13hr","14hr","15hr","16hr","17hr","18hr","19hr","20hr","21hr","22hr","23hr","0hr"]
pylab.title("Homicide occurence by each hour of 24-hour clock ")
pylab.bar(x_values,y_values,width=bar_width,tick_label=tlabel, align='center',color='b')
pylab.show()

