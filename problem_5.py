from hashlib import sha256
from datetime import datetime
import pytest

class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, block):
        if not self.head or not self.tail:
            self.head = block
            self.tail = block

        self.tail.next = block
        block.previous = self.tail
        self.tail = block
        self._size += 1

    def search(self, data):
        needle = None
        block = self.head

        while block:
            if data == block.data:
                needle = block
                break
            block = block.next

        return needle

    def pop(self):
        result = self.tail

        # when: only one item
        if not self.tail.previous:
            self.head = None
            self.tail = None
            return result

        self.tail.previous.next = None
        self.tail = self.tail.previous
        return result

    def size(self):
        return self._size

    def to_list(self):
        result = []
        block = self.head

        while block:
            result.append(block)
            block = block.next

        return result

    class Block:

        def __init__(self, timestamp, data):
            self.timestamp = timestamp
            self.data = data
            self.hash = self.calc_hash()
            self.next = None
            self.previous = None

        def __repr__(self):
            return self.timestamp.strftime('%m/%d/%Y, %H:%M:%S ') + self.data

        def calc_hash(self):
            sha = sha256()
            sha.update(str(self).encode('utf-8'))
            return sha.hexdigest()

        def __eq__(self, other):
            return self.timestamp == self.timestamp and self.data == self.data and self.hash == self.hash


@pytest.fixture
def new_blockchain():
    return BlockChain()

@pytest.fixture
def blockchain_with_data():
    blockchain = BlockChain()

    block = BlockChain.Block(datetime.utcnow(), 'Amount: 1234 Krakens. From: Alice Doe. To: Bob Doe')
    blockchain.append(block)

    block2 = BlockChain.Block(datetime.utcnow(), 'Amount: 5678 Krakens. From: Bob Doe. To: Alice Doe')
    blockchain.append(block2)

    block3 = BlockChain.Block(datetime.utcnow(), 'Amount: 4321 Krakens. From: John Smith. To: Tammy Smith')
    blockchain.append(block3)

    block4 = BlockChain.Block(datetime.utcnow(), 'Amount: 8888 Krakens. From: Tammy Smith. To: Alice Doe')
    blockchain.append(block4)

    # Note: Returning tuple to get the items for comparisons
    return [block, block2, block3, block4], blockchain


def test_block_creation():
    block = BlockChain.Block(datetime.utcnow(), 'Amount: 1243 Krakens. From: John Doe. To: Jane Doe')

    assert block.timestamp <= datetime.utcnow()
    assert block.data == 'Amount: 1243 Krakens. From: John Doe. To: Jane Doe'
    assert block.hash is not None
    assert block.next is None
    assert block.previous is None

def test_blockchain_creation(new_blockchain):
    assert new_blockchain.head is None
    assert new_blockchain.tail is None
    assert new_blockchain.size() == 0

def test_append(new_blockchain):
    block = BlockChain.Block(datetime.utcnow(), 'Amount: 1243 Krakens. From: John Doe. To: Jane Doe')
    new_blockchain.append(block)

    assert new_blockchain.head == block
    assert new_blockchain.tail == block
    assert  new_blockchain.size() == 1

    block2 = BlockChain.Block(datetime.utcnow(), 'Amount: 1103 Krakens. From: Jane Doe. To: John Doe')
    new_blockchain.append(block2)

    assert new_blockchain.head == block
    assert new_blockchain.tail == block2
    assert new_blockchain.head.next == block2
    assert new_blockchain.tail.previous == block
    assert new_blockchain.size() == 2

def test_search(blockchain_with_data):
    block3 = blockchain_with_data[0][2]  # index 2 is 3rd item in list from test data
    blockchain = blockchain_with_data[1]

    result = blockchain.search('Amount: 4321 Krakens. From: John Smith. To: Tammy Smith')
    assert result == block3

    bad_search_result = blockchain.search('Data that is bad!')
    assert bad_search_result is None

def test_pop(blockchain_with_data):
    block4 = blockchain_with_data[0][3]  # index 3 is last item
    blockchain = blockchain_with_data[1]

    result = blockchain.pop()
    assert result == block4
    assert blockchain.tail == blockchain_with_data[0][2]

def test_size(blockchain_with_data):
    blockchain = blockchain_with_data[1]

    assert blockchain.size() == 4

def test_to_list(blockchain_with_data):
    list_values = blockchain_with_data[0]
    blockchain = blockchain_with_data[1]

    assert list_values == blockchain.to_list()
