import os
import sys
import subprocess
import shutil
import time

def install_dependencies():
    try:
        if not shutil.which("ollama"):
            print("Ollama not found. Installing...")
            os.system("curl -fsSL https://ollama.ai/install.sh | sh")
            time.sleep(5)  

        required_libs = ["ollama"]
        for lib in required_libs:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

        print("All dependencies installed successfully!")

    except Exception as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()
