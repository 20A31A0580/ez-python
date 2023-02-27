class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printlist(self):
        temp=self.head
        if not temp:
            print("Linked list is empty")
            return
        else:
            print("Start:",end=" ")
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("End")
    def insert(self,data):
       new_node=Node(data)
       if self.head is None:
           self.head=new_node
       elif self.head.data>=new_node.data:
           new_node.next=self.head
           self.head=new_node
       else:
          current=self.head
          while current.next and new_node.data>current.next.data:
              current=current.next
          new_node.next=current.next
          current.next=new_node
    def delete(self,key):
       if self.head is None:
          print("Deletion not possible")
          return
       if self.head.data==key:
          self.head=self.head.next
          return
       current=self.head
       while current:
           if current.data==key:
               break
           previous=current
           current=current.next
       if current is None:
          print("Deletion error:key not found")
       else:
          previous.next=current.next
if __name__=='__main__':
    obj=LinkedList()
    print('')
    obj.insert(10)
    obj.insert(12)
    obj.insert(8)
    obj.insert(11)
    obj.insert(10)
    obj.printlist()
    obj.delete(12)
    obj.delete(10)
    obj.delete(8)
    obj.printlist()
#lot of functions in same project you can give all definitions at one place you can give all function calls inside the main then it is easy too read
print("Before function")
def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=='__main__':
    f1()
    f2()
    f3()

#DOUBLY LINKED LIST 
#INSERTING AT START
class Node:
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next = None
class dLinkedList:
    def __init__(self):
        self.head = None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def display(self):
        temp=self.head
        if not temp:
            print("Linked list is empty")
            return
        else:
            print("Start:",end=" ")
        while temp:
            print(temp.data,end="->")                                                                                  
            temp=temp.next
        print("End")
     
if __name__=='__main__':
    obj=dLinkedList()
    n1=Node(100)
    obj.head=n1
    n2=Node(200)
    n2.prev=n1
    n1.next=n2
    obj.insert_start()
    obj.display()
#INSERTING AT END
class Node:
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next = None
class dLinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self):
        n=Node(300)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp         
    def display(self):
        temp=self.head
        if not temp:
            print("Linked list is empty")
            return
        else:
            print("Start:",end=" ")
        while temp:
            print(temp.data,end="->")                                                                                  
            temp=temp.next
        print("End")
     
if __name__=='__main__':
    obj=dLinkedList()
    n1=Node(100)
    obj.head=n1
    n2=Node(200)
    n2.prev=n1
    n1.next=n2
    obj.insert_end()
    obj.display()
#insert at pos
class Node:
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next = None
class dLinkedList:
    def __init__(self):
        self.head = None
    def insert_pos(self,pos):
        n=Node(300)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def display(self):
        temp=self.head
        if not temp:
            print("Linked list is empty")
            return
        else:
            print("Start:",end=" ")
        while temp:
            print(temp.data,end="->")                                                                                  
            temp=temp.next
        print("End")     
if __name__=='__main__':
    obj=dLinkedList()
    n1=Node(100)
    obj.head=n1
    n2=Node(200)
    n2.prev=n1
    n1.next=n2
    obj.insert_pos(1)
    obj.display()
#Deletion
class Node:
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next = None
class dLinkedList:
    def __init__(self):
        self.head = None
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def display(self):
        temp=self.head
        if not temp:
            print("Linked list is empty")
            return
        else:
            print("Start:",end=" ")
        while temp:
            print(temp.data,end="->")                                                                                  
            temp=temp.next
        print("End")    
if __name__=='__main__':
    obj=dLinkedList()
    n1=Node(100)
    obj.head=n1
    n2=Node(200)
    n2.prev=n1
    n1.next=n2
    obj.delete_begining()
    obj.display()
#del at end
class Node:
    def __init__(self, data):
        self.data = data
        self.prev=None
        self.next = None
class dLinkedList:
    def __init__(self):
        self.head = None
    def delete_end(self):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.prev.next=None
        temp.prev=None
    def display(self):
        temp=self.head
        if not temp:
            print("Linked list is empty")
            return
        else:
            print("Start:",end=" ")
        while temp:
            print(temp.data,end="->")                                                                                  
            temp=temp.next
        print("End")    
if __name__=='__main__':
    obj=dLinkedList()
    n1=Node(100)
    obj.head=n1
    n2=Node(200)
    n2.prev=n1
    n1.next=n2
    obj.delete_end()
    obj.display()
