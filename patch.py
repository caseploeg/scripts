#!/usr/bin/env python3

import sys

def replace_string_in_rodata(filename, search_str, replace_str):
    # Ensure the search string and replacement string are the same length
    if len(search_str) != len(replace_str):
        print("Error: The search string and replacement string must be of the same length.")
        return

    try:
        # Read the binary file
        with open(filename, 'rb') as f:
            data = f.read()
        
        # Convert strings to bytes
        search_bytes = search_str.encode()
        replace_bytes = replace_str.encode()
        
        # Find the start index of the .rodata section
        start_index = data.find(search_bytes)
        if start_index == -1:
            print(f"Error: The string '{search_str}' was not found in the binary file.")
            return

        # Replace the found string
        modified_data = data[:start_index] + data[start_index:].replace(search_bytes, replace_bytes, 1)

        # Save the modified binary to a new file
        new_filename = filename + '_edit'
        with open(new_filename, 'wb') as f:
            f.write(modified_data)

        print(f"String '{search_str}' successfully replaced with '{replace_str}'.")
        print(f"Modified file saved as '{new_filename}'.")

    except IOError as e:
        print(f"IOError: {e}")

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python replace_rodata.py <filename> <search_string> <replace_string>")
    else:
        filename = sys.argv[1]
        search_str = sys.argv[2]
        replace_str = sys.argv[3]
        replace_string_in_rodata(filename, search_str, replace_str)

