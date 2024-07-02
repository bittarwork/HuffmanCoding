import heapq
from collections import defaultdict


class Node:
    def __init__(self, symbol=None, frequency=0, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    # Comparison method for priority queue
    def __lt__(self, other):
        return self.frequency < other.frequency

# Function to count the frequency of each character in the text


def count_frequencies(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
    return frequencies

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

# Function to generate Huffman codes for each symbol


def generate_huffman_codes(node, code='', codes=None):
    if codes is None:
        codes = {}
    if node.symbol is not None:
        codes[node.symbol] = code
    else:
        generate_huffman_codes(node.left, code + '0', codes)
        generate_huffman_codes(node.right, code + '1', codes)
    return codes

# Function to encode the text using Huffman codes


def encode_text(text, codes):
    return ''.join(codes[char] for char in text)

# Function to save the encoded text and Huffman tree to files


def compress_and_save(input_file_path, frequencies_file_path, output_file_path):
    try:
        # Read the contents of the input file with UTF-8 encoding
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
        return
    except UnicodeDecodeError:
        print(f"Error: The file {
              input_file_path} could not be decoded using UTF-8.")
        return

    # Step 1: Count the frequencies of each character
    frequencies = count_frequencies(text)

    # Step 2: Write the frequencies to the frequencies file
    try:
        with open(frequencies_file_path, 'w', encoding='utf-8') as file:
            for char, frequency in frequencies.items():
                file.write(f"{repr(char)}\t{frequency}\n")
    except IOError as e:
        print(f"Error writing to file {frequencies_file_path}: {e}")
        return

    # Step 3: Create a priority queue based on the frequencies
    priority_queue = create_priority_queue(frequencies)

    # Step 4: Build the Huffman tree
    huffman_tree = build_huffman_tree(priority_queue)

    # Step 5: Generate Huffman codes for each symbol
    codes = generate_huffman_codes(huffman_tree)

    # Step 6: Encode the text using the Huffman codes
    encoded_text = encode_text(text, codes)

    # Step 7: Write the encoded text to the output file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(encoded_text)
    except IOError as e:
        print(f"Error writing to file {output_file_path}: {e}")


# Call the compress_and_save function with the appropriate file paths
input_file_path = 'input.txt'
frequencies_file_path = 'frequencies.txt'
output_file_path = 'compressed_text.txt'
compress_and_save(input_file_path, frequencies_file_path, output_file_path)
