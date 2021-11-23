# Huffman coding program

## Priority queue

The major part of this program is priority queue. I decide to use array 
to accomplish its functionality. The linked list is also the right option, 
its time complexity as same as using array, but the coding is little more 
complex. 

Maybe the min-heap is a better choice for this. I cannot handle the coding 
phase so far. 

For the purpose of lower coasting, the queue (array) must be ordered. 
So I can get the specific item from the head or tail of the queue 
directly, which coasts O(1). 

For the ordered queue, the initial operation of queue cannot avoid. In this 
program so far, I use insert order, it coasts O(n^2).

During the building of the tree in phase of encoding, the two smallest item 
are popped and merged as the new one, and then the new reinserted into the 
queue, which coasts O(n^2). 

At the end of process, the last item of queue is the root of the huffman
tree. 

## Special condition

When the given string contains just one type of character, such as 'a', 
'aaaaa', in this situation, the huffman tree just has its root element. 
It is not meaningful to use the tree to encode and decode data by normal 
steps. 

So, the single bit code '0' or '1' is assigned for encoding phase, the 
next step is to replace the characters of given string with '0' or '1'.
The decoding phase can be also finished by reversed steps.

Eventually, the purpose of compression is reached in this circumstance.

## Time complexity

The worst time complexity of encoding is O(n^2).

algorithms:
- priority queue counts the frequency of each character, O(n)
- the queue initialize itself by insert sort every frequency of character, O(n^2)
- building up the huffman tree by popping and reinserting sorted queue elements, O(n^2)
- huffman tree traversing for every character's binary code, O(n)
- iterate the given string to get the whole string's binary code, O(n)

The worst time complexity of decoding is O(n).

algorithms:
- use the every binary bit for reaching the character at the tree, O(n)


## Space complexity

The worst space complexity of encoding is O(n).

algorithms:
- the frequency of each character, this map costs O(n)
- the binary code for each character, this map costs O(n)
- the huffman tree costs O(n)

The worst space complexity of decoding is O(n).