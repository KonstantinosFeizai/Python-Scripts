#Implement of Huffman Coding ,  including Encode and Decode funcinalities
import heapq
from collections import Counter, namedtuple

class HuffmanNode(namedtuple("HuffmanNode", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    frequency = Counter(text)  # Count character frequencies
    heap = [HuffmanNode(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0]  # Root of the Huffman tree

def generate_huffman_codes(node, prefix="", code_map={}):
    if node:
        if node.char is not None:
            code_map[node.char] = prefix  # Assign code
        generate_huffman_codes(node.left, prefix + "0", code_map)
        generate_huffman_codes(node.right, prefix + "1", code_map)
    return code_map

def huffman_encode(text):
    root = build_huffman_tree(text)
    code_map = generate_huffman_codes(root)
    encoded_text = "".join(code_map[char] for char in text)
    return encoded_text, root

def huffman_decode(encoded_text, root):
    decoded_text = ""
    node = root
    for bit in encoded_text:
        node = node.left if bit == "0" else node.right
        if node.char:  # Found a character
            decoded_text += node.char
            node = root  # Reset to root for next character
    return decoded_text

# Example usage:
if __name__ == "__main__":
    text = "BCAADDDCCADDFFFACCCACACACACCCAC"
    print("Original Text:", text)
    
    encoded_text, tree = huffman_encode(text)
    print("Encoded Text:", encoded_text)
    
    decoded_text = huffman_decode(encoded_text, tree)
    print("Decoded Text:", decoded_text)
    
    assert text == decoded_text, "Decoding failed!"
