import compress


def read_frequencies_from_file(file_path):
    frequencies = {}
    with open(file_path, 'r') as file:
        for line in file:
            if (line == "\n" ) : continue
            else : 
                thisLine = line.strip("\n").split('\t')
                char = thisLine[0]
                freq = int(thisLine[1])
                frequencies[char] = freq
    return frequencies

# Function to decode the encoded text using Huffman tree
def decode_text(compressed_file_path, huffman_tree_file_path, frequencies_file_path):
    frequencies = read_frequencies_from_file(frequencies_file_path)
    node_list = compress.create_sorted_node_list(frequencies)
    huffman_tree = compress.build_huffman_tree(node_list)
    with open(compressed_file_path, 'r') as file:
        encoded_text = file.read()

    decoded_text = ""
    current_node = huffman_tree

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node['left']
        elif bit == '1':
            current_node = current_node['right']

        if 'left' not in current_node and 'right' not in current_node:
            decoded_text += current_node['symbol']
            current_node = huffman_tree

    return decoded_text
compressed_file_path = 'compressed_text.txt'
huffman_tree_file_path = 'huffman_tree.txt'
frequencies_file_path = 'frequencies.txt'
decoded_text = decode_text(
    compressed_file_path, huffman_tree_file_path, frequencies_file_path)
print('Decompressed text:', decoded_text)
