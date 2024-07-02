import heapq
from collections import defaultdict

# تعريف فئة Node


class Node:
    def __init__(self, symbol=None, frequency=0, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    # مقارنة الترددات في قائمة الأولوية
    def __lt__(self, other):
        return self.frequency < other.frequency

# Function to read the frequencies from a file


def read_frequencies_from_file(file_path):
    frequencies = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    char, freq = line.split('\t')
                    # لتحويل التمثيل النصي للرمز إلى رمز فعلي
                    char = eval(char)
                    frequencies[char] = int(freq)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
    return frequencies

# Function to decode the encoded text using Huffman tree


def decode_text(compressed_file_path, frequencies_file_path):
    frequencies = read_frequencies_from_file(frequencies_file_path)
    if not frequencies:
        return ""

    priority_queue = create_priority_queue(frequencies)
    huffman_tree = build_huffman_tree(priority_queue)

    try:
        with open(compressed_file_path, 'r', encoding='utf-8') as file:
            encoded_text = file.read()
    except FileNotFoundError:
        print(f"Error: The file {compressed_file_path} was not found.")
        return ""
    except IOError as e:
        print(f"Error reading file {compressed_file_path}: {e}")
        return ""

    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        elif bit == '1':
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            decoded_text += current_node.symbol
            current_node = huffman_tree

    return decoded_text

# Function to create a priority queue of nodes sorted by their frequency


def create_priority_queue(frequencies):
    priority_queue = []
    for symbol, freq in frequencies.items():
        heapq.heappush(priority_queue, Node(symbol=symbol, frequency=freq))
    return priority_queue

# Function to build the Huffman tree


def build_huffman_tree(priority_queue):
    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        parent_node = Node(frequency=node1.frequency +
                           node2.frequency, left=node1, right=node2)
        heapq.heappush(priority_queue, parent_node)
    huffman_tree = heapq.heappop(priority_queue)
    return huffman_tree


# Call the decode_text function with the appropriate file paths
compressed_file_path = 'compressed_text.txt'
frequencies_file_path = 'frequencies.txt'
decoded_text = decode_text(compressed_file_path, frequencies_file_path)

print('Decompressed text:', decoded_text)
