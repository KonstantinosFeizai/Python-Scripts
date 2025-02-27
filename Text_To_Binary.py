# This script allows you to convert any text into binary
# Convert binary back into readable text
# Takes user input and process it interactively
# Option to Decode any binary message


def text_to_binary(text):
    """Converts a string into binary representation."""
    return " ".join(format(ord(c), "08b") for c in text)  # Ensuring 8-bit binary format

def binary_to_text(binary):
    """Converts binary representation back to a string."""
    try:
        return "".join(chr(int(b, 2)) for b in binary.split(" "))
    except ValueError:
        return "❌ Invalid binary input! Please enter valid 8-bit binary values."

def get_valid_choice():
    """Prompts the user until they enter a valid 'yes' or 'no' response."""
    while True:
        choice = input("\nWould you like to decode a custom binary message? (yes/no): ").strip().lower()
        if choice in ["yes", "no"]:
            return choice
        print("⚠️ Invalid input! Please enter 'yes' or 'no'.")

# Welcome message
print("=" * 50)
print("🖥️  TEXT ↔ BINARY CONVERTER 🖥️".center(50))
print("=" * 50)

# User input for text conversion
message = input("\nEnter the text to convert to binary: ")
binary_message = text_to_binary(message)
print("\n🔹 Converted to Binary:")
print(binary_message)

# Decoding back to text
print("\n🔹 Decoding back to text:")
decoded_text = binary_to_text(binary_message)
print(decoded_text)

# Validating user input for decoding choice
decode_choice = get_valid_choice()
if decode_choice == "yes":
    binary_input = input("\nEnter the binary message to decode: ")
    print("\n🔹 Decoded Message:")
    print(binary_to_text(binary_input))

print("\n✅ Conversion Completed! Thank you for using the script. 🚀")
