import random as r
x="saranya k"
print(r.sample(x,4))
#shuffle
a=[1,2,3,4,5]
r.shuffle(a)
print(a)
#choice
print(r.choice(a))
print(r.choice(x))
#choices default only k will be taken
print(r.choices(a,k=10))
#uniform
print(r.uniform(5,10))
#To see all functions
z=dir(r)
print(z)

#calendar
import calendar
#full calendar
print(calendar.calendar(2023))
#partial calendar
print(calendar.month(2023,9))
#setfirstweekday
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2003,9))

#datetime
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y")
print("short:",sv)
fv=a.strftime("%Y")
print("LONG:",fv)

#functions
"""classifications--1.predefined,2.userdefined functions
for code resuability we use functions
types
1.functions without arguments without return value
2.functions without arguments with return value
3.functions with arguments with return value
4.functions with arguments without return value"""
def sample():
    print("saranya")
print("lakshmi")
sample()
print("lakshmi")
sample()
#1.functions without arguments without return value
def multi():
    n1=int(input("enter:"))
    n2=int(input("enter:"))
    print(n1*n2)
multi()
#2.functions without arguments with return value
def multi():
    n1=int(input("enter:"))
    n2=int(input("enter:"))
    return n1*n2
k=multi()
print(k)
#3.functions with arguments with return value
def multi(n1,n2):
    return (n1*n2)
k=multi(3,4)
print(k)
#4.functions with arguments without return value
def multi(n1,n2):
    print(n1*n2)
multi(3,4)
