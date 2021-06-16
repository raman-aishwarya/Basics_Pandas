# creating a dictionary and converting it into pandas

import pandas as pd
import numpy as np
import string as s
from random import shuffle
# create a sample dataset

# student scheme
# student id, name, age, gender, phone, email, city, gpa

def genData(n):
    sid = np.arange(1,n+1)
    age = np.random.randint(19,30, n)
    phone = np.random.randint(90000,99999,n)
    gpa = np.round(np.random.uniform(1,5, n),1)
    
    letters = list(s.ascii_letters)
    shuffle(letters)
    
    domain=['@yahoo.co.in','@gmail.com','@hotmail.com',
            '@mail.in','@rediffmail.com','@office.co.in']
    
    places = ['pune','mumbai','thane','delhi','kolkata','bangalore']
    
    # empty list to store the data
    name=[]; email=[]; city=[]; gender=[]
    
    for i in range(n):
        # name
        rnd = int(np.random.randint(0,20,1))
        NAME = ''.join(letters[rnd:rnd+6])
        name.append(NAME)
        shuffle(letters) # to avoid duplicate names/email
        
        # email
        rnd = int(np.random.randint(0,len(domain),1))
        EMAIL = NAME + domain[rnd]
        email.append(EMAIL)
        
        # city
        rnd = int(np.random.randint(0,len(places),1))
        city.append(places[rnd])
        
        # gender
        rnd = int(np.random.randint(2,100,1))
        # if rnd is odd, "M", else "F"
        if rnd%2==0:
            gender.append("F")
        else:
            gender.append("M")
        
       
    # create the dictionary
    d_stud = {'studid':sid, 'name':name,
              'age':age, 'phone':phone,
              'email':email, 'city':city, 'gpa':gpa, 'gender':gender}        
    
    # convert the dictionary into Pandas
    df_stud = pd.DataFrame(d_stud)
    
    return(df_stud)

# create data
student = genData(300)

print(student)
type(student)

# save the data into a file

student.to_csv("myStudentdata.csv", index=False)

# file will be saved in default working directory

import os
os.getcwd()

# read CSV file into pandas

student = pd.read_csv("mystudentdata.csv")
print(student)

# dimension
student.shape

# rows
student.shape[0]

# columns
student.shape[1]
student.columns
len(student.columns)

# data types of the columns
student.dtypes
    # object : string or factor

# information about the dataset
student.info()

# basic statistical info on numeric data
student.describe()[1:] # skips the rowcount

# statistical info on selected columns
round(student.describe()[1:][['age','gpa']],2)

# row and column names
student.columns
student.index.values

# head / tail
student.head() # returns the first 5 rec (default)
student.head(2)

student.tail() # returns the last 5 rec (default)
student.tail(10)


# access the data (columns)
# select all cols
print(student)
# head/tail

# select 1 col
student.name
student['name']

# select multiple cols
# 1
student[['studid','name','age']]

# 2
cols=['name','age','phone','gpa']
student[cols]


educ=['BS']*55 + ['MS']*30 + ['BE']*50 + ['BTech']*57 + ['ME']*18 + ['MTech']*24 + ['PhD']*5 + ['BCom']*39 + ['MCom']*22


# -------
# index
# -------

# studid as index; not part of columns
student = student.set_index('studid')
print(student)

# index on multiple columns
student = student.set_index(['studid','city'])
print(student)

# reset the index
student = student.reset_index()
print(student)

# studid as index and part of columns
student = student.set_index('studid',drop=False)
print(student)

# reset the index
student = student.reset_index(drop=True)
print(student)

# add the new columns
student['educ'],student['exp'],student['cert']=educ, np.random.randint(0,11,len(student)), np.random.randint(0,4,len(student))

print(student)

student.dtypes

# delete columns
# add some dummy values to be deleted later
student['a'],student['b'],student['c'],student['d']= -1, None,0,'d'
print (student)

# 1)
student = student.drop(['a','b'], axis=1)
student.dtypes #axis=1 defines column

# 2)
student.drop(columns=['c','d'],inplace=True) # inplace=true will assign value back in student

#-----------
### queries
#-----------

# 1) relational operators (==,>,>=,<,<=)

# select student info where stud edu is 'BTech'

student[student.educ == 'BTech']

# selected columns

cols=['studid','name','age','gender','educ','exp']
student[cols][student.educ== 'PhD']

# 2) get al stud data where exp is atleast 3 years
student[cols][student.exp >= 3]

# 3) get all stud data where exp is atmost 3 yrs

student[cols][student.exp <=3 ]


# 2] logical operators (and, or, not)
# select stud data where educ ='BS' and gpa is more than 2.5

cols=['studid','name','educ','gpa']

student[cols][(student.educ == 'BS') & (student.gpa > 2.5)]

# OR

#select stud data where educ is MCom or certif is more than 3

cols=['studid','name','educ','cert']
student[cols][(student.educ == 'MCom') | (student.cert > 3)]


# NOT
# select stud info who are not from 'kolkata'

cols=['studid','name','city']
student[cols][(student.city != "kolkata")]


# IN operator
# select stud data who have an engineering degree
eng = ['BE', 'BTech', 'ME', 'MTech']
student.educ.unique()


cols=['studid','name','city','educ']
student[cols][student.educ.isin(eng)]

# NOT IN
# select all stud data who dont have an engg degree

student[cols][~student.educ.isin(eng)]


# sorting the data
# select all students who are from west; sort result by city name

w_city=['thane','pune','mumbai']
cols = ['studid','name','age','city']

student[cols][student.city.isin(w_city)].sort_values('city')

# default sort order= ascending/alphabetical


# descending sort

student[cols][student.city.isin(w_city)].sort_values('city', ascending=False)

# sorting data on multiple cols
# sort based on non engg educ, and gpa


cols=['studid','name','educ','gpa']
student[cols][~student.educ.isin(eng)].sort_values(['educ','gpa'])


# descending sort
student[cols][~student.educ.isin(eng)].sort_values(['educ','gpa'],ascending=False)


#--------------
# update pandas
#--------------


student.head()

# update student records with their name

# rec1: update the name with my name

student.name[student.studid == 1] = 'aishwarya'


print(student.head())

# marital status
student.mst[student.studid==1] = 'S'

student[student.studid == 1]


# change the email of the student to match the pattern name n domain
student[['studid','name','email']]

out = student[['name','email']][student.studid ==1]
name = out.name[0]
em = out.email[0]

em.split("@")[1]


student.email[student.studid==1]= name + "@" + em.split("@")[1]

student[['studid','name','email']][student.studid==1]