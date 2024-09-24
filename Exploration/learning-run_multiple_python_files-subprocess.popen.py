import os

working_directory = os.getcwd() 

# r for "raw string"
python_file = working_directory + r"\Exploration\learning-Hello_World.py"

python_command = "python.exe " + '"' + python_file + '"'

# Recommended best practice
# Executed as a separate process within file

# Import subprocess module
import subprocess

# List of commands to run
commands = [
    python_command,
    python_command,
    python_command
]

# Join commands with '&&' to run them sequentially
cmd = " && ".join(commands)

# Run the commands
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Live output
for line in iter(process.stdout.readline, ''):
    print(line)

# Get the output and error (if any)
stdout, stderr = process.communicate()

print("Output:\n", stdout)
print("Error:\n", stderr)