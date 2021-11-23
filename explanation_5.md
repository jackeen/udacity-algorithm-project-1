# Block chain

## Time complexity

When the chain grows up, the block has to calculate by constant step, 
including hash, timestamp, and operation of the linked list. These actions 
will not increase along with the growth of data, which means that the time
complexity of appending is O(1).

## Space complexity

Because the block chain is the linked list, its usage of space will increase 
as the growth of the chain, so its space complexity is O(n).