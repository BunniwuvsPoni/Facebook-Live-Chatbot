def start_facebook_application(env):
    import threading
    import subprocess
    import os

    # Selects the correct python interperter depending on the environment
    match env:
        case "dev":
            python = os.getcwd() + r"\.venv\Scripts\python.exe"
        case _:
            python = "python.exe"

    # Function to run script
    def run_script(script):
        subprocess.call([python, script])

    # List of scripts to run concurrently, r for "raw string"
    scripts = [os.getcwd() + r"\Modules\flask_facebook.py",
               os.getcwd() + r"\Modules\ngrok_facebook.py"]

    # Create a thread for each script
    threads = []
    for script in scripts:
        thread = threading.Thread(target=run_script, args=(script,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()