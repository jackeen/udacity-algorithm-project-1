# Block chain

import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def convert_to_string(self):
        t = "Timestamp:{}\nData:{}\nPrev_Hash:{}"
        return t.format(self.timestamp, self.data, self.previous_hash)

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_string = self.convert_to_string()
        sha.update(hash_string.encode("utf-8"))
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    def __repr__(self):

        if self.count == 0:
            return 'This is a empty block chain. '

        string = ''
        node = self.head
        while node:
            string += '[{}] -> '.format(node.data)
            node = node.next
        
        string += 'None'
        return string

    def append(self, data):
        ct = datetime.now()
        timestamp = ct.timestamp()
        
        if self.tail:
            pre_hash = self.tail.hash
            block = Block(timestamp, data, pre_hash)
            self.tail.next = block
            self.tail = block
        else:
            block = Block(timestamp, data, "0")
            self.head = block
            self.tail = block

        self.count += 1


# test 1
# expected result: [a] -> [b] -> [c] -> [4] -> None
bc = BlockChain()
bc.append("a")
bc.append("b")
bc.append("c")
bc.append(4)
print(bc)

# test 2
# expected result: [None] -> [] -> None
bc2 = BlockChain()
bc2.append(None)
bc2.append('')
print(bc2)

# test 3
# expected result: empty chain information
bc3 = BlockChain()
print(bc3)