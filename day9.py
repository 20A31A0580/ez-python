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
