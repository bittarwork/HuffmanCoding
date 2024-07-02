# Huffman Compression and Decompression Project

## Introduction

This project implements the Huffman algorithm for compressing and decompressing text files. The Huffman algorithm constructs a Huffman Tree based on the frequency of characters in the input text, and then uses this tree to generate binary codes for each character in the original text.

## Project Structure

- `compress.py`: Contains functions for compressing text using the Huffman algorithm.
- `decompress.py`: Contains functions for decompressing text using the Huffman Tree.
- `input.txt`: A sample text file containing the text to be compressed.
- `frequencies.txt`: A file that stores the frequencies of characters extracted from the input text.
- `compressed_text.txt`: A file that contains the compressed binary text.

## How to Use

### Compressing Text

1. Place the text you want to compress in the `input.txt` file.
2. Run the `compress.py` script using the following command:
   ```bash
   python compress.py
   ```
3. The script will generate two files:
   - `frequencies.txt`: Contains the frequency of each character in the input text.
   - `compressed_text.txt`: Contains the compressed binary representation of the text.

### Decompressing Text

1. Ensure that `frequencies.txt` and `compressed_text.txt` are present in the same directory.
2. Run the `decompress.py` script using the following command:
   ```bash
   python decompress.py
   ```
3. The decompressed text will be displayed in the terminal.

## Code Details

### compress.py

This file contains functions for compressing text:

- `count_frequencies(text)`: Counts the frequency of each character in the text.
- `create_priority_queue(frequencies)`: Creates a priority queue of nodes sorted by their frequencies.
- `build_huffman_tree(priority_queue)`: Builds the Huffman Tree from the priority queue.
- `generate_huffman_codes(node, code='', codes=None)`: Generates Huffman codes for each symbol.
- `encode_text(text, codes)`: Encodes the text using the Huffman codes.
- `compress_and_save(input_file_path, frequencies_file_path, output_file_path)`: Executes the compression steps and saves the resulting files.

### decompress.py

This file contains functions for decompressing text:

- `read_frequencies_from_file(file_path)`: Reads the character frequencies from a file.
- `decode_text(compressed_file_path, frequencies_file_path)`: Decompresses the text using the Huffman Tree.

### Node Class

The `Node` class is used to create nodes for the Huffman Tree:

- `__init__(self, symbol=None, frequency=0, left=None, right=None)`: Initializes a node.
- `__lt__(self, other)`: Compares nodes based on their frequencies for the priority queue.

## Requirements

- Python 3.6 or higher

## Contributing

Contributions are welcome! Please open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
