
# Tree

### Intro-

Trees work similarly to linked lists in the sense that there’s a starting item that points to other points in memory. It differs because it will point to many different points in memory moving down the structure where a linked list only points to one.

### Defining a Binary Tree-

A Binary Tree is a data structure that every node has at most two children. A Binary Tree can be represented by different data structures (int, dictionary, or list) and class representations for each node.

### How a Tree Works-

A tree starts at the Root or the top of the tree. There is a parent child relationship in a tree. The “parent” is any node that has connected nodes. The connected nodes are the “child” of the node they are connected to. Each step down from the root is called a “subtree”. Though, nodes that are not connected to any other nodes are called “leaf” nodes. These are going the be at the bottom of whatever branch you are following.

<img src="https://i.ibb.co/bH8wJhn/tree.jpg" alt="tree" border="0">


### Moving through Trees-

Moving or Traversing through a BST is done when we want to show all the data that the tree holds in order from smallest to largest. Similarly, we can traverse the tree in reverse which will show all the data in the tree from largest to smallest. This is done using **__iter__**, **yield**, and an **if** loop. Code shown below:

`def __iter__(self):
	yield from self._traverse_forward(self.root)
 def _traverse_forward(self, node):
	 if node is not None:
		 yeild from self._traverse_forward(node.left)
		 yeild node.data
		 yield from self._traverse_forward(node.right)`

And reverse:
		 
`def __iter__(self):
	yield from self._traverse_backward(self.root)
 def _traverse_backward(self, node):
	 if node is not None:
		 yeild from self._traverse_backward(node.right)
		 yeild node.data
		 yield from self._traverse_backward(node.left)`

### BST in Python-

There are many functions that can be used to help you in building and traversing a BST. As well as, many different packages from different developers. Below are some of the more common functions used:

__Table of functions__
| Operation | Description |
|--|--|
| insert(value) | Insert a value into the tree |
| remove(value) | removes value from tree |
| contains(value) | determine out if value is in tree |
| traverse_forward() | Visit all objects from smallest to largest |
| traverse_reverse() | visite all objects from largest to smallest |
| height(node) | Determine the height of a node |
| size() | return the size |
| empty() | Returns true if node is empty |


### Exercise-

Create a **BST** of all even numbers from 2-10




> Written with [StackEdit](https://stackedit.io/).
