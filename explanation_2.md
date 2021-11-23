# The file recursion program

## Overall

Because of the hierarchy of dir and each level has several items including 
dirs and files, It might be better to use iteration to deal with the items 
at the same level. For the depth of dir, recursion might a better choice, 
which causes the concise code. 

## Time complexity

The worst time complexity is O(n * m).

Suppose 'n' is the average number of files at each level, and there are 
'm' levels in the dir hierarchy. So the amount of the the files will be 
accessed is 'm * n'.

## Space complexity

The space complexity is O(n + m).

Suppose 'n' is files' number and 'm' is depth of recursion.

algorithms:
- different level selection for target files needs linear space, which is O(n)
- recursive function has the hierarchy of dir needs O(m) space
