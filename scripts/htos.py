#!/usr/bin/env python3

def hex_to_string(hex_str):
    # Convert hex string to bytes
    bytes_obj = bytes.fromhex(hex_str)
    # Decode bytes to string

    return bytes_obj.decode('utf-8')

print(hex_to_string(input()))
