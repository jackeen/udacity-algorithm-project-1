# Union and intersection

## Idea

Union function uses 'set' data structure to collect all elements 
that exists in one or two sets. 
Plus, it can filter the multiple elements.

Intersection function uses 'map' to record the element that exists 
in first collection, then using it to check out the elements exist 
in second collection. The purpose of usage of 'set' is as same as 
the union used.

## Time complexity

Suppose the one linked list's length is m, and another one's is n, 
the two programs need to access the every items of these two linked lists, 
so they will costs O(m + n).

## Space complexity

As the length of two linked list above mentioned, these functions needs 
O(m + n) space. 
