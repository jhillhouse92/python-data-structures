# Show Me the Data Structures

This is my Udacity Project for Data Structures and Algorithms:
Show Me the Data Structures.

## Getting Started

As an alternative to printing out tests to the console, I used
`pytest` and wrote unit tests for each of the problems. 

### Prerequisites

Execute the following in the project directory to get started to install pytest:

```
pip install -r requirements.txt
```

## Execute Tests

To run the tests, go to the project directory and execute:
 
```
pytest *.py
```

There are 27 tests in total with 100% passing.

## Problem 1: LRU Cache

The LRU Cache uses an `OrderedDict` from Python's `collections` module because
the `OrderedDict` maintains insertion order into the dictionary. This allows
sets, even when capacity is exceeded, to be O(1) and gets, to be O(1) as items
are just moved to the end of the `OrderedDict` when accessed or updated.

The decision to extend from `OrderedDict` rather than use it as an object property
is because it gives the flexibility of treating the `LRUCache` as a Python dictionary
for convenient access by being able to set and retrieve values just a like a normal 
dictionary.

## Problem 2: File Recursion

The solution uses a top-down tree traversal approach via recursion going through
each directory and when at the last directory adding the files that match
the file type to the result. Error handling is incorporated to ensure invalid file types
are not considered. Because each file/folder in the tree is traversed, it is O(n).

## Problem 3: Huffman Coding

The solution is based off of [Data Compression with Huffman’s Algorithm](https://freecontent.manning.com/data-compression-with-huffmans-algorithm/ "Data Compression with Huffman’s Algorithm") 
from the book *Algorithms and Data Structures in Action* by Marcello La Rocca.

I first use a `Counter` from Python's `collections` module to count the frequency of
each character. This is an O(n) operation where n is the size of the string.

Secondly, it uses a `heapq` (or priority queue) to automatically get the smallest frequency
with each pop. This is O(log n). From this, a tree is built to capture the encoding
scheme. Because there is O(log n) for each character, the total time complexity is O(n log n).

## Problem 4: Active Directory

I changed the users iterable in the `Group` class from a list to a set. This allows
membership tests to operate in O(1) time. From there, it uses a tree traversal approach
via recursion looking through each group and sub-group until there are no more groups
or membership has been confirmed. The worst case, is the user is not in the group, which causes
iteration through each group and all of it's children recursively which is an O(n) operation.

## Problem 5: Blockchain

This uses a Doubly LinkedList implementation with the following methods:

```
- append
- search
- pop
- size
- to_list
```

### Append

Append is to add items to the list. Occurs in O(1) time.

### Search

Search was added in case a specific block transaction needs to be looked up.
It requires the data to perform a lookup. Because each node
in the list may have to be searched, it is worst-time O(n).

### Pop

Pop was added in case the last transaction was added in error. It removes the block
from the chain. It was for this reason, it's implemented via a Doubly LinkedList as 
opposed to a single LinkedList resulting in O(1) time.

### Size

Size is to get the size of the LinkedList. It is O(1)

### To List

It may be needed to perform list operations against the blockchain.
This method was added for that purpose. It is O(n) because it needs
to loop through all nodes in the LinkedList.

## Problem 6: Union and Intersection

This solution modified the starting template slightly to make the methods
static methods of the LinkedList class.

The union method iterates through the first LinkedList adding node values to a set.
This is because a set doesn't have duplicates and membership tests are O(1).
Then, it loops through the second LinkedList and adds to the set as well.
This in effect, creates a union of the two, because duplicates are ignored.

The intersection method iterates through the first LinkedList adding node values to a
temporary set. This is to remove duplicates in the first LinkedList.
Then, it loops through the second LinkedList and if its in the temporary set, adds the node
value to the result set. This result set, represents the intersection.

Both methods are O(n).

