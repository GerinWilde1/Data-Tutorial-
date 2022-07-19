


class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None

   def listprint(self):
      printval = self.head
      while printval is not None:
         print (printval.data)
         printval = printval.next

list = LinkedList()
list.head = Node("Sun")
e2 = Node("Mon")
e3 = Node("Tue")
e4 = Node("Wed")
e5 = Node("Thu")
e6 = Node("Fri")
e7 = Node("Sat")

# Link first Node to second node
list.head.next = e2

# Link second Node to third node
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = None

list.listprint()