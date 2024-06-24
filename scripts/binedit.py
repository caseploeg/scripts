# Binary data to be written to the file
x = b"\x91\x51\x55\x55\x55\x55"
binary_data = b"C"*16 + x 

# Open the file in write binary mode
with open('output.bin', 'wb') as file:
    # Write the binary data to the file
    file.write(binary_data)

# File is automatically closed when exiting the with block

