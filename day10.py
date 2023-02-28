#stacks
stack=[]
n=int(input("enter the size:"))
def push():
        element=int(input("enter integer:"))
        stack.append(element)
        print(stack)
def pop():
    e=stack.pop()
    print("removed element:",e)
    print(stack)
l=0
while True:
    print("select 1.push 2.pop 3.quit")
    choice=int(input("enter operation"))
    if choice==1:
        if l==n:
            print("overflow")
        else:
            push()
            l=l+1
    elif choice==2:
        if l==0:
            print("underflow")
        else:
            pop()
            l=l-1
    else:
        break
#stacks using linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def display(self):
        temp=self.head
        if temp==None:
            print("underflow")
        else:
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.next
                if(temp!=None):
                    print("->",end=" ")
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def pop(self):
        temp=self.head
        if temp==None:
            print("underflow")
        else:
            self.head=self.head.next
            temp.next=None
            print("\nremoved element",temp.data)
    def peek(self):
        temp=self.head
        if temp==None:
            print("underflow")
        else:
            print("\ntop of the stack is:",temp.data) 
if __name__=="__main__":
    s=stack()
    s.push(11)
    s.push(22)
    s.push(33)
    s.push(44)
    s.display()
    s.pop()
    s.pop()
    s.display()
    s.peek()
#balanced
s=input("enter brackets:")
c=0
d=0
for i in s:
    if i=="(":
        c=c+1
    if i==")":
        c=c+1
    if i=="]":
        d=d+1
    if i=="[":
        d=d+1
if c%2==0 and d%2==0:
    print("balanced")
else:
    print("not balanced")
#balenced brackets another implementation
s=input("enter brackets")
st=[]
balanced=True
for i in s:
    if(i=='{' or i=='[' or i=='('):
        st.append(i)
    elif(i=='}'):
        if(len(st) and st.pop()!='{'):
            balanced=False
            break
    elif(i==']'):
        if(len(st) and st.pop()!='['):
            balanced=False
            break
    elif(i==')'):
        if(len(st) and st.pop()!='('):
            balanced=False
            break
    else:
        balanced=False
        break
if(balanced==False or len(st)):
    print("Not balanced")
else:
    print("Balanced")
#queue
queue=[]
def enqueue():
        element=int(input("enter integer:"))
        queue.append(element)
        print(queue)
def dequeue():
    e=queue.pop(0)
    print("removed element:",e)
    print(queue)
while True:
    print("select 1.enqueue 2.dequeue 3.quit")
    choice=int(input("enter operation"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    else:
        break 
#queue implementation using queue module
import queue
l=queue.Queue(maxsize=5)
l.put(10)
l.put(20)           
print(l.get())
print(l.get())
#stack implementation using queue module
from queue import LifoQueue
s=LifoQueue()
print(s.qsize())
s.put("a")
s.put("b")
s.put("c")
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())
#queues with linked list
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
 
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
 
a= Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeued = a.dequeue()
        if dequeued is None:
            print('Queue is empty.')
        else:
            print('Dequeued element: ', int(dequeued))
    elif operation == 'quit':
        break
