import gdb
import re

class DisassembleAndGrep(gdb.Command):
    """Disassemble a function and grep for a specific pattern"""

    def __init__(self):
        super(DisassembleAndGrep, self).__init__("disassemble_grep", gdb.COMMAND_USER)

    def invoke(self, arg, from_tty):
        args = gdb.string_to_argv(arg)
        if len(args) != 2:
            print("Usage: disassemble_grep <function> <pattern>")
            return

        function_name = args[0]
        pattern = args[1]

        # Disassemble the function
        try:
            disassembly = gdb.execute("disassemble {}".format(function_name), to_string=True)
        except gdb.error as e:
            print("Error disassembling function: {}".format(e))
            return

        # Search for the pattern and print matching lines
        lines = disassembly.split('\n')
        matches = [line for line in lines if re.search(pattern, line)]

        # Print the results
        if matches:
            print("Found pattern '{}':".format(pattern))
            for match in matches:
                print(match)
        else:
            print("No matches found for pattern '{}'".format(pattern))

# Register the command with GDB
DisassembleAndGrep()

print("Command 'disassemble_grep' loaded. Usage: disassemble_grep <function> <pattern>")

