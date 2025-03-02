import sys

def count_set_bits(n):
    return bin(n).count('1')

def reverse_bits_fixed(n, bit_size=8):
    binary_str = bin(n)[2:].zfill(bit_size)  # Convert to binary and pad with leading zeros
    reversed_binary = binary_str[::-1]  # Reverse the string
    return int(reversed_binary, 2)  # Convert back to integer

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

while True:
    try:
        num = int(input("\nEnter an integer (0-255 for 8-bit representation): "))

        if num < 0 or num > 255:
            print("❌ Please enter a number between 0 and 255!")
            continue

        binary_representation = bin(num)[2:].zfill(8)  # Get 8-bit binary representation
        set_bits = count_set_bits(num)
        reversed_num = reverse_bits_fixed(num, 8)
        reversed_binary = bin(reversed_num)[2:].zfill(8)  # Get reversed 8-bit binary
        power_of_two = is_power_of_two(num)

        print(f"\nResults for {num}:")
        print(f"✅ Binary Representation (8-bit): {binary_representation}")
        print(f"✅ Set Bits Count: {set_bits}")
        print(f"✅ Reversed Bits: {reversed_num} (Binary: {reversed_binary})")
        print(f"✅ Power of Two: {'Yes' if power_of_two else 'No'}")

    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")
        continue

    play_again = input("\nDo you want to try another number? (Y/N): ").strip().lower()
    if play_again not in ('y', 'yes'):
        print("🔚 Exiting program. Thanks for using!")
        sys.exit()
