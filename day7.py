#lambda function- its called as anonymous function.when we want to use function concept without using function name there we apply the concept of lambda function
l=[1,2,3]
result=map(lambda x:x+x,l)
print(list(result))
r=map(lambda x:pow(x,2),l)
print(list(r))
name='saranya'
(lambda name:print(name))(name)
#write a program after creating a list with even numbers within the range 1 to 15 ,now apply lambda function and create a new list which should have squareroots of the elements
l=[]
for i in range(1,15):
    if i%2==0:
        l.append(i)
r=map(lambda x:pow(x,1/2),l)
print(list(r))
#pillars of oops -1.abstraction,2.encapsulation,3.inheritance,4.polymorphism
#hiding the implementation part showing what is required for the users --abstraction ex:exe file
#we can make class/method as abstract ,opposite to abstract is concrete
import abc 
class abstractdemo(abc.ABC):
    @abc.abstractmethod#called the decorator to make the method abstract one
    def display(self):
        None
    @abc.abstractmethod
    def show(self):
        None
#changing the abstract to concrete
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()
#encapsulation- binding data and function into a single entity
#there are 3 types
#public-one class info can be accessed by any other class
#private-can be used where it is declared not in inherited classes
#protected-can be used where it is declared ,whichever clas is inherited from this class also we can use
#inheritance--derived class will inherit properties of base class
#1.single inheritance
#2.multiple inheritance
#3.multilevel inheritance
#4.heirarichial inheritance
#5.hybrid inheritance
#one parent one child class
class parent:
    def display(self):
        print("parent class")
class child(parent):
    def show(self):
        print("child class")
obj=child()
obj.display()
obj.show()
#1.single inheritance
class a:
    n=30
class b(a):
    def calc(self):
        c=self.n+70
        print(c)
o=b()
o.calc()
#2.multiple inheritance
class mom:
    def mdisplay(self):
        print("mom class")
class dad:
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
o=child()
o.cdisplay()
o.mdisplay()
o.ddisplay()
#happy number
n=int(input("enter:"))
t=n
while(t>1):
    s=0
    while(t>0):
        k=t%10
        s=s+pow(k,2)
        t=t//10
    t=s
    print(t)
if t==1:
    print("happy number")
else:
    print("not a happy number")
