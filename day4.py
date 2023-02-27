d={n:n*n for n in range(1,5)}
print(d)
#caluculating product price for 2 units
o={"egg":20,"milk":40}
n={product:price*2 for(product,price) in o.items()}
print(n)
#with checks
o={"egg":20,"milk":40}
n={product:price for(product,price) in o.items() if price>25}
print(n)
#create a list with 8 customer names display a dictonary which has customer names along with dicounts for them from aparticular shop
name=["a","b","c","d","e","f","g","h"]
discount=[]
import random
for i in range(8):
    d=random.randint(1,50)
    discount.append(d)
n={name[i]:discount[i] for i in range(len(name))}
print(n)
#or 2nd process
l=["a","b","c","d","e","f","g","h"]
import random
n={name:random.randint(1,50) for name in l}
print(n)
#or 3rd process
name=["a","b","c","d","e","f","g","h"]
marks=[]
import random
for i in range(8):
    d=random.randint(1,50)
    marks.append(d)
n={name:marks for (name,marks) in zip(name,marks)}
print(n)
#strings
s='I AM \'saranya\''
print(s)
#repetation
print(s*3)
#concatenation
print(s+s)
#upper
print(s.upper())
#lower or casefold
print(s.lower())
print(s.casefold())
#capitalize
print(s.capitalize())
#replace
print(s.replace("a","A"))
#strip
b="    saranya    "
print(b.strip())
#split
print(s.split())
#center
b="saranya"
print(b.center(40,"*"))
#count
print(s.count("a"))
print(s.count("a",5,len(s)))
#endswith
print(s.endswith("a",0,len(s)))
#startswith
print(s.startswith("a",0,len(s)))
#min
print(min("a","b"))
#max
print(max("a","b"))
#mutable--list,set,tuple
#immutable--int,float,string,bool,tuple
#get one string as input along with a character find out and display whether the particular characater is in string or not
s=list(map(str,input("Enter:").split(" ")))
if s[1] in s[0]:
    print("Yes")
else:
    print("NO")
#another process
s=input("Enter:")
c=input("Enter:")
f=0
for i in s:
    if i==c:
        f=1
        #break
    else:
        f=0
if(f==1):
    print('Yes')
else:
    print('No')
#check palindrome or not

s=input("Enter:") 
r=s[::-1]
if s==r:
    print("Yes.It is a palindrome")
else:
    print("No")
#check given string contains space or not i yes count no of spaces and print
s=input("Enter:")
c=0
for i in s:
    if i==" ":
        c=c+1
print("{} occurs {} times".format('space',c))
#create a list with vowels  get string as input count vowels from string
v=['a','e','i','o','u','A','E','I','O','U']
c=0
s=input("Enter:")
for i in s:
    if i in v:
        c=c+1
print(c)
#math
import math
print("ceil value:",math.ceil(12.34))
print("floor value",math.floor(12.34))
print("factorial:",math.factorial(3))
print("Power:",math.pow(2,5))
print("Modulator:",math.fmod(20,3))
a,b=divmod(10,3)
print(a,b)
