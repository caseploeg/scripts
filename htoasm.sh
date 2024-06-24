#!/bin/bash

# Check if the user provided a hex value as input
if [ -z "$1" ]; then
    echo "Usage: $0 <hex value>"
    exit 1
fi

# Get the hex value from the input
hex_value=$1

# Create a temporary binary file
bin_file=$(mktemp --suffix=.bin)
asm_file=$(mktemp --suffix=.s)

# Convert hex value to binary and write to the binary file
echo -n $hex_value | xxd -r -p > "$bin_file"

# Create a temporary assembly file that loads the binary data
cat <<EOF > "$asm_file"
.global _start
_start:
    .incbin "$bin_file"
    ret
EOF

# Compile the assembly code to an object file
obj_file=$(mktemp --suffix=.o)
gcc -c "$asm_file" -o "$obj_file"

# Use gdb to disassemble the instructions
gdb -batch -ex "file $obj_file" -ex "disassemble /r _start"

# Clean up temporary files
rm -f "$bin_file" "$asm_file" "$obj_file" 

