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
            self.encoded_data = '0'
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


# To do: convert these to pytest cases
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman = Huffman(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(huffman.encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(huffman.encoded_data))

    decoded_data = huffman.decode()

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "A"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    huffman = Huffman(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(huffman.encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(huffman.encoded_data))

    decoded_data = huffman.decode()

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))