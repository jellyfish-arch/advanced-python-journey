import os
import time
import platform
import shutil

try:
    import psutil
except ImportError:
    print("Warning: 'psutil' library not found. System monitoring will be limited.")
    psutil = None

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format (e.g., KB, MB, GB, etc.)
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def monitor_system():
    print("="*20, "System Information", "="*20)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

    if psutil:
        print("\n" + "="*20, "CPU Usage", "="*20)
        print(f"Physical cores: {psutil.cpu_count(logical=False)}")
        print(f"Total cores: {psutil.cpu_count(logical=True)}")
        print(f"Total CPU Usage: {psutil.cpu_percent()}%")

        print("\n" + "="*20, "Memory Usage", "="*20)
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}")
        print(f"Available: {get_size(svmem.available)}")
        print(f"Used: {get_size(svmem.used)}")
        print(f"Percentage: {svmem.percent}%")
    else:
        # Fallback using standard libraries
        total, used, free = shutil.disk_usage("/")
        print("\n" + "="*20, "Disk Usage (Root)", "="*20)
        print(f"Total: {get_size(total)}")
        print(f"Used: {get_size(used)}")
        print(f"Free: {get_size(free)}")

    print("\n" + "="*20, "Network Info", "="*20)
    print(f"Hostname: {platform.node()}")
    print(f"Python Version: {platform.python_version()}")

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        monitor_system()
        print("\nMonitoring... (Ctrl+C to stop)")
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
            break
