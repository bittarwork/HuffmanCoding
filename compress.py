# Function to count the frequency of each character in the text
def count_frequencies(text):
    frequencies = {}
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

# Function to create a list of nodes sorted by their frequency
def create_sorted_node_list(frequencies):
    keys = list(frequencies.keys())
    keys.sort()
    node_list = []
    for key in keys:
        thisDict = {"symbol": key, "frequency": frequencies[key]}
        node_list.append(thisDict)
    return node_list

# Function to build the Huffman tree
def build_huffman_tree(node_list):
    while len(node_list) > 1:
        node1 = node_list[0]
        node2 = node_list[1]
        node_list = node_list[2:]

        parent_node = {
            'frequency': node1['frequency'] + node2['frequency'],
            'left': node1,
            'right': node2
        }

        node_list.append(parent_node)

    huffman_tree = node_list[0]
    return huffman_tree

# Function to generate Huffman codes for each symbol
def generate_huffman_codes(node, code, codes):
    if 'symbol' in node:
        codes[node['symbol']] = code
    else:
        generate_huffman_codes(node['left'], code + '0', codes)
        generate_huffman_codes(node['right'], code + '1', codes)

# Function to encode the text using Huffman codes
def encode_text(text, codes):
    encoded_text = ""
    for char in text:
        if char in codes:
            encoded_text += codes[char]
    return encoded_text
# Function to save the encoded text and Huffman tree to files
def compress_and_save(input_file_path, frequencies_file_path, output_file_path):
    # Read the contents of the input file
    with open(input_file_path, 'r') as file:
        text = file.read()

    # Step 1: Count the frequencies of each character
    frequencies = count_frequencies(text)

    # Step 2: Write the frequencies to the frequencies file
    with open(frequencies_file_path, 'w') as file:
        for char, frequency in frequencies.items():
            file.write(f"{char}\t{frequency}\n")

    # Step 3: Create a sorted node list based on the frequencies
    node_list = create_sorted_node_list(frequencies)

    # Step 4: Build the Huffman tree
    huffman_tree = build_huffman_tree(node_list)

    # Step 5: Generate Huffman codes for each symbol
    codes = {}
    generate_huffman_codes(huffman_tree, '', codes)

    # Step 6: Encode the text using the Huffman codes
    encoded_text = encode_text(text, codes)

    # Step 7: Write the encoded text to the output file
    with open(output_file_path, 'w') as file:
        file.write(encoded_text)


# Call the compress_and_save function with the appropriate file paths
input_file_path = 'input.txt'
frequencies_file_path = 'frequencies.txt'
output_file_path = 'compressed_text.txt'
compress_and_save(input_file_path, frequencies_file_path, output_file_path)

