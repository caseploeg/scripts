#!/bin/bash

# Function to clean up temporary files
cleanup() {
    rm -f "$temp_file" "$temp_obj" "$temp_dis"
}

# Trap to ensure cleanup is always performed
trap cleanup EXIT

# Check if a file name is provided as an argument
if [ -n "$1" ]; then
    # If a file name is provided
    file="$1"
    
    # Check if the file exists
    if [ ! -f "$file" ]; then
        echo "Error: File '$file' does not exist."
        exit 1
    fi
    
    # Compile the assembly file to an object file
    gcc -c "$file" -o temp.o
    
    # Disassemble the object file and output to a .d file
    objdump -d temp.o > "${file%.*}.d"
    
    # Clean up the temporary object file
    rm -f temp.o

    echo "Disassembly output written to ${file%.*}.d"
else
    # If no file name is provided, read assembly code from stdin
    echo "Reading assembly code from stdin..."
    
    # Create a temporary assembly file
    temp_file=$(mktemp --suffix=.s)
    temp_obj=$(mktemp --suffix=.o)
    temp_dis=$(mktemp --suffix=.d)
    
    # Read assembly code from stdin and write to the temporary file
    cat > "$temp_file"
    
    # Compile the temporary assembly file to an object file
    gcc -c "$temp_file" -o "$temp_obj"
    
    # Disassemble the object file and output to a .d file
    objdump -d "$temp_obj" > "$temp_dis"
    
    # Print the disassembly output
    cat "$temp_dis"
    
    # Temporary files are automatically cleaned up by the trap
fi

