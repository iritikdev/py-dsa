# py-dsa : Custom Data Structures using python
This project implements custom data structures such as dynamic array, linked list, and stack linked list in Python. These data structures are used for storing and managing data in a flexible and efficient way.

## Dynamic Array
A dynamic array is a data structure that can resize itself during runtime. 
It has a fixed initial capacity but can grow or shrink depending on the number of elements it contains. 
The dynamic array implementation in this project is based on Python's built-in list data type.

### Usage
```
from dynamic_array import Array

numbers = Array(3)

numbers.append(10)
numbers.append(20)
numbers.append(30)

print(numbers)  # [10, 20, 30]

print(len(numbers))  # 3

print(numbers[0]) # 10
print(numbers[2]) # 30

```

## Linked List
A linked list is a data structure that consists of a sequence of nodes, where each node stores a reference to an object and a reference to the next node in the sequence. The linked list implementation in this project is a singly linked list.

### usage
```
from linked_list import LinkedList

list = LinkedList()

list.addLast(10)
list.addLast(20)

list.addFirst(5)

print(list)
```
