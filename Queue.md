


> Written with [StackEdit](https://stackedit.io/).


## Queue


A queue, like a stack is a linear data structure. Unlike a stack, which is Last In First Out (LIFO), a queue is organized in a First In First Out (FIFO) manner. With a queue, whatever has been in the queue the longest is what comes out first.

A queue, like a stack is a linear data structure. Unlike a stack, which is Last In First Out (LIFO), a queue is organized in a First In First Out (FIFO) manner. With a queue, whatever has been in the queue the longest is what comes out first.

A queue in python is represented by a list. To add an item to the queue, or it enqueue the item, you add .append to the end of the queue name: **queue_name.append(value)**. To remove the first item from the queue, or to dequeue the item, you would use **[0]** and **del: item = queue_name[0], del queue_name[0]**. There are many other keywords that are used for queues like **len** and **empty**. **Len** will return the size of the queue and **empty** will return True if the queue is 0. You can also use any keyword that you would use for a normal list like **pop.**


   
| .append |This will add to the end of the queue  |
| len() | This will return the length of the queue|
| .pop[0] | This will remove the first item in the queue |

Example of creating and removing items from a queue:
  
        # A program to demonstrate queue implementation using list
    
    # Initializing a queue
    queue = []
    
    # Adding items to the queue
    queue.append(1)
    queue.append(2)
    queue.append(3)
    
    #what the queue looks like now
    print("What the queue looks like")
    print(queue)
    
    # Removing items from the queue
    print("Removing the first item from the queue")
    print(queue.pop(0))
    print(queue.pop(0))
    print(queue.pop(0))
    
    print("Queue after removing all items")
    print(queue)
    
    # Now the pop command will return an error because the queue is empty

This code will return:

    What the queue looks like
    [1, 2, 3]
    
    Removing the first item from the queue
    1
    2
    3
    
    Queue after removing all items
    []

## Exercise

Append all even numbers from 1-100 then removing all the items one by one add them all together.



 

