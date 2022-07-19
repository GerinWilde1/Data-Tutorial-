
## Linked Lists

### intro

Linked Lists are not lists in the sme way as normal Python lists. Though, they may be made up of normal lists. A linked List is a sequence of data which are connected together through a link or pointer. One item pointing to the position of the next item in memory only moving forward. Doubly-Linked Lists on the other hand differ from linked lists because they point both forward and backward in the sequence (prev, next). Lastly, with Circulay-Linked Lists the Tail points to the head creating a full loop.

<img src="https://i.ibb.co/wszDdy5/Linked-Lists.jpg" alt="Linked-Lists" border="0">

### Hot to make and amend a Linked List (Insert/Remove)


While appending a linked list you will need to reset the pointers. Taking the item before and after the point in the linked list you wish to place the new item and changing them to point to it instead of each other and having the new item point to the item before it’s new location (prev) and the item after its new location (next).

The first node in a Linked list is called the **Head** and the end if called the **Tail**.  Inserting at these pounts creats a new **Head** or **Tail**. Remamber, when creating a head the link leading to the prev needs to = None and for the tail the link leading to the next needs to = None.

Similarly, with removing an item from the linked list. You will need to have the item before and after the item that is desired to be removed to skip over the undesired item and point to each other.

### Linked Lists in Python

Python does have a linked list that can be used called a **daque**. To start you’ll need to **import daque**. Then, to create a new empty **daque** use: **NameOfLinkedList = daque**. But to create a linked list you do not need to use **daque**.

| Python Code |Desvription  |
|:--|:--|
| nameOfDeque.appendleft(value) | Adds "value" before the head |
| nameOfDeque.append(value) | Adds "value" after the tail |
| nameOfDeque.insert(i, value) | Adds "value" after node "i". |
| value = nameOfDeque.popleft() | Removes the first item (the head) |
| value = nameOfDeque.pop() | Removes the last item (the tail) |
| del nameOfDeque[i] | Removes node "i". |
| length = len(nameOfDeque) | Return the size of the linked list |
| if len(nameOfDeque) == 0: | Returns true if the length of the linked list is zero |

### Example of Linked List Code
    class Node:
     def __init__(self, dataval=None):
       self.data = dataval
       self.next = None

    class SLinkedList:
     def __init__(self):
      self.head = None

    list1 = SLinkedList()
    list1.head = Node("Mon")
    e2 = Node("Wed")
    e3 = Node("Fri")
    #Link first Node to second node 
    list1.headval.next = e2 
    # Link second Node to third node 
    e2.next = e3


### Exercise

Finish the week names in the Linked List by appending the days that are left in the correct location




> Written with [StackEdit](https://stackedit.io/).
