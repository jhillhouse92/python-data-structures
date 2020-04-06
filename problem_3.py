import sys
from collections import Counter
import heapq


class Huffman:

    class Node:
        def __init__(self, character, freq):
            self.left = None
            self.right = None
            self.character = character
            self.freq = freq

        # This is to add to heapq
        def __lt__(self, other):
            return self.freq < other.freq

    def __init__(self, data):
        self.root = None
        self.encoded_data = ''

        if data:
            self.encode(data)

    def encode(self, data):  # O(n log n)
        frequencies = Counter(data)  # O(n) where n is length of string
        priority_q = []
        for char, count in frequencies.items():  # O(n) where n is length of string
            heapq.heappush(priority_q, self.Node(char, count))  # O(log n) where n is length of string

        if len(priority_q) == 1:
            self.root = self.Node(data, 1)
            self.root.left = priority_q[0]
            self.encoded_data = '0' * priority_q[0].freq # repeat for each frequency of the single node
            return self.encoded_data

        while len(priority_q) > 1:  # O(n)
            left = heapq.heappop(priority_q)  # O(log n)
            right = heapq.heappop(priority_q)  # O(log n)
            parent = self.Node(left.character + right.character, left.freq + right.freq)
            parent.left = left
            parent.right = right
            heapq.heappush(priority_q, parent)  # O(log n)

        self.root = priority_q[0]
        encoded_table = {}

        def _encode(node, binary):  # O(n) where n is number of nodes
            if len(node.character) == 1:
                encoded_table[node.character] = binary
            else:
                if node.left:
                    _encode(node.left, binary + '0')
                if node.right:
                    _encode(node.right, binary + '1')

        _encode(heapq.heappop(priority_q), '')
        self.encoded_data = ''.join([encoded_table[char] for char in data])
        return self.encoded_data

    def decode(self):
        node = self.root

        result = ''
        for bit in self.encoded_data:
            if bit == '0':
                node = node.left
            else:
                node = node.right

            if not node.left and not node.right:
                result += node.character
                node = self.root

        return result


def test_encode():
    a_great_sentence = 'The bird is the word'

    assert sys.getsizeof(a_great_sentence) == 69

    huffman = Huffman(a_great_sentence)

    assert sys.getsizeof(int(huffman.encoded_data, base=2)) == 36
    assert huffman.encoded_data == '1000111111100100001101110000101110110110100011111111001101010011100001'

def test_decode():
    a_great_sentence = 'The bird is the word'
    huffman = Huffman(a_great_sentence)
    original_str = huffman.decode()

    assert sys.getsizeof(original_str) == 69
    assert original_str == 'The bird is the word'

def test_encode_decode_with_one_char():
    a_great_sentence = 'A'

    assert sys.getsizeof(a_great_sentence) == 50

    huffman = Huffman(a_great_sentence)

    assert sys.getsizeof(int(huffman.encoded_data, base=2)) == 24
    assert huffman.encoded_data == '0'

    original_str = huffman.decode()

    assert sys.getsizeof(original_str) == 50
    assert original_str == 'A'

def test_encode_decode_with_repeating_char():
    a_great_sentence = 'aaaaaa'

    assert sys.getsizeof(a_great_sentence) == 55

    huffman = Huffman(a_great_sentence)

    assert sys.getsizeof(int(huffman.encoded_data, base=2)) == 24
    assert huffman.encoded_data == '000000'

    original_str = huffman.decode()

    assert sys.getsizeof(original_str) == 55
    assert original_str == 'aaaaaa'