# The least recently used cache

class CandidateNode():
    """
    This is the double linked list node for 'CandidateQueue'. 
    """

    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class CandidateQueue():
    """
    This is the priority queue.
    
    The queue organizes the candidates as a linked list for choosing, 
    the highest priority (least used recently) of item is located 
    at the head of the list.
    """
    
    def __init__(self):
        
        # This is the local cache for getting related data. 
        # The key is the real value that user provided.
        # The value of the dictionary is the reference of the node (CandidateNode).
        self.dict = dict()
        
        self.head = None
        self.tail = None
    
    def _add_node_to_tail(self, node):
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        node.next = None

    def _pop_head(self):
        """
        Cut off the current linked-list head and return it. 
        """
        
        old_head = self.head
        new_head = old_head.next
        new_head.prev = None
        old_head.next = None
        self.head = new_head
        return old_head

    def _cut_off_middle_node(self, node):
        """
        Cut off the node from the linked list, and reconnect the list. 
        """

        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None
        
    def move_to_tail(self, key):
        selected_node = self.dict[key]
        
        if selected_node is self.tail:
            return

        if selected_node is self.head:
            self._add_node_to_tail(self._pop_head())
        else:
            self._cut_off_middle_node(selected_node)
            self._add_node_to_tail(selected_node)
    
    def enque(self, key):
        """
        To add the new value into the priority queue.
        
        This function add the new node on the end of the linked list, 
        if the key is existed, its relative node will moved to the end.
        """
        
        if key in self.dict:
            self.move_to_tail(key)
            return

        new_node = CandidateNode(key)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self._add_node_to_tail(new_node)
        
        # update the reference for quick access in future
        self.dict[key] = new_node

    def deque(self):
        old_head = self._pop_head()
        key = old_head.value
        del self.dict[key]
        return key


class LRU_Cache(object):

    def __init__(self, capacity=10):

        if capacity is None or capacity < 0:
            capacity = 10

        self.cache = dict()
        self.capacity = capacity
        self.count = 0
        self.candidates = CandidateQueue()

    def get(self, key):
        """
        Retrieve item based on provided key. 
        
        returns:
            -1: if the key is not existed. 
            user data: if the key is found. 
        """

        value = self.cache.get(key)
        if value is None:
            return -1
        else:
            self.candidates.move_to_tail(key)
            return value
        
    def set(self, key, value):
        """
        Set the key-value data in cache.  
        
        If the cache is reached at the highest capacity, 
        the least used item will be removed for the new one. 
        """
        
        if self.count == self.capacity:
            candidate_key = self.candidates.deque()
            del self.cache[candidate_key]
        else:
            self.count += 1

        self.candidates.enque(key)
        self.cache[key] = value
        

def test_case_1():
    cache = LRU_Cache(5)
    result = list()
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    result.append(cache.get(1))
    result.append(cache.get(2))
    result.append(cache.get(9))

    cache.set(5, 5) 
    cache.set(6, 6)

    result.append(cache.get(3))
    result.append(cache.get(4))

    print('result: ', result)

print('--- test 1 ---')
print('set:1,2,3,4; get: 1,2,9; set:5,6; get:3,4; capacity input is 5')
test_case_1()
# expected result: [1, 2, -1, -1, 4]


def test_case_2():
    cache = LRU_Cache(5)
    result = list()
    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)

    result.append(cache.get(3))
    result.append(cache.get(2))
    result.append(cache.get(9))
    
    cache.set(5, 5) 
    cache.set(6, 6)

    result.append(cache.get(3))
    result.append(cache.get(1))
    
    print('result: ', result)

print('--- test 2 ---')
print('set:1,2,3,4; get: 3,2,9; set:5,6; get:3,1; capacity input is 5')
test_case_2()
# expected result: [3, 2, -1, 3, -1]


def test_case_3():
    cache = LRU_Cache(5)
    result = list()
    cache.set(1, 1)
    cache.set(2, 2)

    result.append(cache.get(2))

    cache.set(3, 3)
    cache.set(4, 4)

    result.append(cache.get(3))
    
    cache.set(5, 5) 
    cache.set(6, 6)

    result.append(cache.get(3))
    result.append(cache.get(1))
    
    print('result: ', cache.capacity, result)

print('--- test 3 ---')
print('set: 1,2; get: 2; set: 3,4; get: 3; set: 5,6; get: 3,1; capacity input is 5')
test_case_3()
# expected result: 5 [2, 3, 3, -1]


def test_case_4():
    cache = LRU_Cache()
    result = list()

    result.append(cache.get(3))
    result.append(cache.get(1))
    
    print('result: ', cache.capacity, result)

print('--- test 4 ---')
print('get: 3,1; no capacity input')
test_case_4()
# expected result: 10 [-1, -1]


def test_case_5():
    cache = LRU_Cache(None)
    result = list()
    
    result.append(cache.get(3))
    
    print('result: ', cache.capacity, result)

print('--- test 5 ---')
print('get: 3; capacity input is None')
test_case_5()
# expected result: 10 [-1]