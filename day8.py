#protected
class encap:
    _a=10
    c=20
    def encapfunc(self):
        _b=200
        print("encap function-accessing protected")
        print(self._a+10)
o=encap()
print(o._a)
o.encapfunc()
print(o.c)
#private
class encap:
    __a=10
    print(__a)
    def encapfunc(self):
        print("encap function")
        print(self.__a)
o=encap()
o.encapfunc()
#print(o.__a)#wil throw an error because a is private cannot be accessed outside the class
#polymorphism-one item or same item are used for different purposes
#types -1.overloading(a.operator overloading(+) b.method overloading)
#       2.overriding
#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
o=moverload()
print("without arguments")
o.display()
print("with all arguments")
o.display(10,20)
print("with one arguments")
o.display(10)
#overriding-if a method is defective or cannot be used inside derived class it will take it from its base class or parents class
class parent():
    def __init__(self):
        self.value="inside parent"
    def show(self):
        print(self.value)
class child(parent):
    def __init__(self):
        self.value="inside child"
    def show(self):
        print(self.value)
o1=parent()
o2=child()
o1.show()
o2.show()
#polymorphism
class a:
    def a1(self):
        print("a1")
    def a2(self):
        print("a2")
    def a3(self):
        print("a3")
class b:
    def a1(self):
        print("b1")
    def a2(self):
        print("b2")
    def a3(self):
        print("b3")
o1=a()
o2=b()
for i in (o1,o2):
    i.a1()
    i.a2()
    i.a3()
#datastructures
#helps to write efficient programs
#linear-arrays,linkedlist,stack,queue-storing data sequentially
#non-linear-trees,graphs,tables,sets-no sequential style required
#static-arrays
#Dynamic-linkedlist,stack,queue
#linkedlist-ex:train--list of items which are linked with one another
#creating linked list
#step1:create the node
#step2:particoner the node with 2 segments data and none
#step3:add value into the blank node
#step4:mark the node as head
#step5:create the next node by following the above steps
#step6:establish link btw 1st node and the 2nd node
#displaying linked list
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
o=singlelinkedlist()
n=node(10)
o.head=n
n1=node(20)
o.head.next=n1
n2=node(30)
n1.next=n2
o.display()
-----------
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
 
obj.display()       

#Operations
#insertion:Beg end pos
#Deletion
#Search

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_Atend(self,data):
        nb=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nb
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.insert_beginning("Saranya")
obj.insert_Atend("Hai")
obj.display()        

#INsert at pos

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insertatpos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.insertatpos(3,100)
obj.display()
#insertion at runtime
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def addNode(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_Atend(self,data):
        nb=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nb
    def insertatpos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->")
                temp=temp.next
obj=singlelinkedlist()
n = int(input('enter the number of elements in linked list : '))
for i in range(n):
    data=input("Enter data:")
    obj.addNode(data)
obj.insert_beginning("saranya")
obj.insert_Atend("Hai")
obj.insertatpos(3,100)
obj.display()   
