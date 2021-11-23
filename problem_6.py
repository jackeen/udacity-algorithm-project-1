# Union and intersection

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, array=[]):
        self.size = 0
        self.head = None
        self.tail = None

        for v in array:
            self.append(v)

    def __str__(self):
        output = ""
        node = self.head
        while node:
            output += f"{node.value} "
            node = node.next
        return output

    def count(self):
        return self.size

    def append(self, value):
        node = Node(value)
        if self.size != 0:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        
        self.size += 1


def union(list_a, list_b):
    u = set()

    if list_a and list_b:
        node = list_a.head
        while node:
            u.add(node.value)
            node = node.next

        node = list_b.head
        while node:
            u.add(node.value)
            node = node.next

    return LinkedList(list(u))


def intersection(list_a, list_b):
    result = set()
    
    if list_a and list_b:
        # store the elements that existed in set of a
        dict_a = dict()
        node = list_a.head
        while node:
            dict_a[node.value] = True
            node = node.next

        # check out the elements of set of b whether or not existed in a
        # if so, this element is what the program to find 
        node = list_b.head
        while node:
            v = node.value
            if v in dict_a:
                result.add(v)
            node = node.next

    return LinkedList(list(result))


def test_function(list_a, list_b):
    linked_list_a = LinkedList()
    linked_list_b = LinkedList()

    for v in list_a:
        linked_list_a.append(v)
    for v in list_b:
        linked_list_b.append(v)

    print('union: {}'.format(union(linked_list_a, linked_list_b)))
    print('intersection: {}'.format(intersection(linked_list_a, linked_list_b)))


# Test case 1
print('--- test 1 ---')
test_function([3, 2, 4, 35, 6, 65, 6, 4, 3, 21], [6, 32, 4, 9, 6, 1, 11, 21, 1])
# expected result: 
#   union [32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21]
#   intersection [4, 6, 21]


# Test case 2
print('--- test 2 ---')
test_function([1, 2, 2, 3, 4, 5, 7], [6, 6])
# expected result: 
#   union [1, 2, 3, 4, 5, 6, 7]
#   intersection empty


# Test case 3
print('--- test 3 ---')
test_function([], [])
# expected result: both of union and interaction is empty


# Test case 4
print('--- test 4 ---')
print('union ', union(None, None))
print('intersection: ', intersection(None, None))
# expected result: both of union and interaction is empty