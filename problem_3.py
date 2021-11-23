# Huffman coding

import sys


class PriorityItem:
    """
    This is the priority queue item, and is also the huffman tree node. 
    
    As the inside item of the tree, its char property is None, 
    which will be used for determining whether the leaf is reached.  
    """

    def __init__(self, f, c=None, left=None, right=None):
        self.frequency = f
        self.char = c
        self.left = left
        self.right = right


class Tree:
    """
    The wrapped information about the huffman tree.
    """

    def __init__(self, root):
        self.root = root
        self.is_single_type_character = False
        self.single_type_character = ''

    def set_single_character(self, char):
        """
        To record the character, when the given string for encoding is containing 
        a only one character. For simplifying the next phase of encoding and decoding.
        """
        
        self.is_single_type_character = True
        self.single_type_character = char


class MiniPriorityQueue:
    """
    Maintain the minimun priority queue.

    Its item with smallest frequency always locates at the first of the ordered queue.
    """
    
    def __init__(self):
        self.queue = []

    def init_queue(self, string):
        """
        Build up the ordered queue. 
        """

        frequency = dict()
        for char in string:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        for c, f in frequency.items():
            self.insert(PriorityItem(f, c))

    def insert(self, item):
        """
        Insert priority item in the queue by finding the proper position.

        Argus:
            item(PriorityItem): using its property 'frequency' to find the right position.
        """

        count = len(self.queue)
        if count == 0:
            self.queue.append(item)
            return

        index = 0
        current_item = self.queue[0]
        
        # sort by frequency for items in the queue, 
        # from smallest to biggest
        while current_item:
            if item.frequency < current_item.frequency:
                self.queue.insert(index, item)
                break
            index += 1
            if index < count:
                current_item = self.queue[index]
            else:
                self.queue.append(item)
                break
    
    def pop(self):
        """
        Pop the first item of the queue.
        
        Returns:
            None: if the queue is empty.
            minimun value: the smallest one of the queue.  
        """
        
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def count(self):
        return len(self.queue)


def huffman_tree_traversing(root, code_map, current_code=""):
    """
    Traversing one code (char) by accessing the tree 
    from the highest item to its leaf. 
    
    Argus:
        root: the tree's root.
        code_map: for storing the binary code of char.
        current_code: current binary code of the traversing path. 
    """

    if root.char is not None:
        code_map[root.char] = current_code
        return
    
    # left move forward
    if root.left:
        huffman_tree_traversing(root.left, code_map, current_code + '0')
    
    # right move forward
    if root.right:
        huffman_tree_traversing(root.right, code_map, current_code + '1')
    

def huffman_encoding(string):
    if string == '' or string is None:
        return '', None

    mpq = MiniPriorityQueue()
    mpq.init_queue(string)
    
    # assign a bit for single type of character at given string
    if mpq.count() == 1:
        root = mpq.pop()
        tree = Tree(root)
        tree.set_single_character(root.char)
        return len(string) * '0', tree

    # set up the tree by retraving priority items from the queue
    while mpq.count() >= 2:
        
        first = mpq.pop()
        second = mpq.pop()
        
        # merge the two smallest items and reinsert into the queue
        new_item = PriorityItem(first.frequency + second.frequency)
        new_item.left = first
        new_item.right = second
        mpq.insert(new_item)
    
    root = mpq.pop()
    
    # traversing every leaf of the tree to find out the chars' binary codes
    code_map = dict()
    huffman_tree_traversing(root, code_map)

    # convert the given string into binary codes
    codes = ""
    for char in string:
        codes += code_map[char]

    return codes, Tree(root)


def huffman_decoding(codes, tree):
    if tree is None or codes is None or codes == '':
        return ''

    if tree.is_single_type_character:
        return len(codes) * tree.single_type_character

    string = ""
    node = tree.root
    
    for code_bit in codes:
        
        if code_bit == '0':
            node = node.left
        elif code_bit == '1':
            node = node.right

        # once reach a char, then reset the path
        if node.char:
            string += node.char
            node = tree.root

    return string


def text_function(a_great_sentence):

    print("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    encoded_size = sys.getsizeof(encoded_data)
    if tree:
        encoded_data_binary = int(encoded_data, base=2)
        encoded_size = sys.getsizeof(encoded_data_binary)

    print("The size of the encoded data is: {}".format(encoded_size))
    print("The content of the encoded data is: {}".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}".format(decoded_data))



# the following test cases' expected output is that the encoded data 
# can reverse back to the original form by decoding

# Test 1
print('--- test_1 ---')
text_function('AAAAAAABBBCCCCCCCDDEEEEEE')

# Test 2
print('--- test_2 ---')
text_function('This is the special program, and it is so useful.')

# Test 3
print('--- test_3 ---')
text_function('aaaaa')

# Test 4
print('--- test_4 ---')
text_function('a')

# Test 5
print('--- test_5 ---')
text_function('')