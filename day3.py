#lists
l=[1,4,7.4,"sara"]
print(l)
print(l[2])
print(l[2:4])
print(l[:3])
print(l[:])
print(l[-3:-1])
#append
l.append(28)
print(l)
#extend
l.extend((3,4,5))
print(l)
#remove
l.remove(1)
print(l)
#pop
l.pop(2)
print(l)
#sort
l.sort()
print(l)
#reverse
l.reverse()
print(l)
#create a list with 10 elements and print one by one
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i)
#create a list with 5 float numbers find the sum and avg of list
l=[1.1,2.2,3.3,4.4,5.5]
print(sum(l))
print(sum(l)/len(l))
#after creating the list with 6 elements fron the user extract only even numbers and print
l=list(map(int,input("enter:").split()))[:6]
for i in l:
    if i%2==0:
        print(i)
#read list of numbers as input and find the product ,if product less than 750 then print product else print sum
n=int(input("size:"))
l=list(map(int,input("enter:").split()))[:n]
p=1
for i in l:
    p=p*i
if p<750:
    print(p)
else:
    print(sum(l))
#list comprehensions-accesing list from existing list
n=[i for i in "saranya"]
print(n)
n=[i for i in range(100,200,20)]
print(n)
n=[i for i in range(1,10) if i%2==0]
print(n)
n=[2**i for i in range(2,5)]
print(n)
#set
s={1,2,3}
print(type(s))
#add
s.add(99)
print(s)
#update
s.update([22,33])
print(s)
#iscard will not throw error if element is not present
s.discard(12)
print(s)
#emove will throw error if element is not present
s.remove(33)
print(s)
s1={1,2,3,4}
s2={2,3,6}
#union
print(s1|s2)  
print(s1.union(s2))
#intersection
print(s1&s2)  
print(s1.intersection(s2))
#difference
print(s1-s2)
#issuperset
print(s1.issuperset(s2))
#symmetric_difference
print(s1^s2)
print(s1.symmetric_difference(s2))
#tuple-ordered
t=(1,2,3,3,4)
print(type(t))
#count
print(t.count(3))
#index
print(t.index(4))
#dict contains elements with 2 units key,values(*keys must be unique)
d={1:"saranya",2:"lakshmi"}
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d[1])
print(d.get(1))
#fromkeys
l=["hi","hello"]
print(dict.fromkeys(l))
#setdefault
d.setdefault(3,"d")
print(d)
#update
d.update({3:"e"})
print(d)
#pop
d.pop(3)
print(d)
