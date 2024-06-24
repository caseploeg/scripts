def int_to_twos_complement(value, bit_length):
    """Convert an integer to its two's complement binary representation."""
    if value >= 0:
        # For non-negative values, just format it as binary
        binary_representation = f'{value:0{bit_length}b}'
    else:
        # For negative values, calculate the two's complement
        # Add the value to 2^bit_length and format it as binary
        binary_representation = f'{(1 << bit_length) + value:0{bit_length}b}'
    return binary_representation

def binary_to_bytes(binary_string):
    """Convert a binary string to a bytes object."""
    # Convert binary string to an integer
    integer_value = int(binary_string, 2)
    # Calculate the number of bytes needed
    num_bytes = (len(binary_string) + 7) // 8
    # Convert the integer to bytes
    byte_array = integer_value.to_bytes(num_bytes, byteorder='big')
    return byte_array

# Given value

low_order = int(input())
high_order = int(input()) 


bit_length = 32

def print_info(value):
  # Convert to two's complement binary representation
  binary_representation = int_to_twos_complement(value, bit_length)

  # Convert the binary representation to bytes
  byte_array = binary_to_bytes(binary_representation)

  print(f"Value: {value}")
  print(f"Two's complement binary representation ({bit_length}-bit): {binary_representation}")
  print(f"Bytes: {byte_array}")
  print(f"Hexadecimal: {byte_array.hex()}")

print_info(high_order)
print_info(low_order)
