import threading
import subprocess
import os

working_directory = os.getcwd() 

# r for "raw string"
python_file = working_directory + r"\Exploration\learning-Hello_World.py"

# Function to run script
def run_script(script):
    subprocess.call(['python', script])

# List of scripts to run concurrently
scripts = [python_file,
           python_file,
           python_file]

# Create a thread for each script
threads = []
for script in scripts:
    thread = threading.Thread(target=run_script, args=(script,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()