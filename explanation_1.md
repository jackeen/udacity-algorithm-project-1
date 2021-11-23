# The least recently used cache

There are two parts of this program.
 - a priority queue, which is the double linked list
 - a cache with properties including count and capacity

## Priority queue idea

This part is a major one. It provides the least recently used candidates for replacement, 
when the cache capacity is reached. 

For this reason, it is necessary to maintain an order of the list, 
and the order depends on the accessing of data recently, including reading and writing. 

Naturally, array can be used for these ordered elements. It is easy to access the priority 
one, at the end or head of the array. 

However, the priority is dynamic as accessing of data. Because it is regularly to 
maintain the order of the element in the array, which means replacing item will 
along with every reading or writing operation. Ideally, these operations' costs should be O(1), 
but to replace each element will cost much more in this data structure. 

There is also having the same reason for choosing stack and queue. 

So linked list sames better under this situation. Firstly, to access the head or the end of it 
seems as easy as using array. Secondly, it is much quickly to replace the selected element to anywhere of the list, which costs O(1). 

So far, there is more one problem has to solve. When one element needs to move to another 
place, searching is necessary. But in this structure, searching will coast O(n). So an 
assistant data structure is used for accelerating of searching. A dictionary is used for 
storing the elements' references. When the chosen element need to replace (change it priority), 
it can be access directly without any searching. 

In practice, when one element of the linked list cuts off from the list, the reconnecting has 
to be done. In other words, the previous and next references of items should be stored in the 
selected element for lower time complexity. 

Eventually, double linked list seems better for priority queue.

## Cache

This is the place where the user's data is contained. The core of it is a dictionary, 
which allowed user to set or get their data for O(1). 

## Time complexity

The worst time complexity is O(1).

algorithms for storing key-value data:

- to set up the priority item, which puts one element into the list 
or move the existed element position, O(1)
- to store the key-value data in the dict, O(1)

algorithms for retrieving data:

- to update the priority of data (move the linked list element to the end), O(1)
- to retrieve the data from the dict, O(1)

## Space complexity

The space complexity is O(n)

- a double linked list for priority queue, O(n)
- a dict for storing the list references, O(n)
- a dict for user key-value data, O(n)




