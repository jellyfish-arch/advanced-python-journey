# pyrefly: ignore [missing-import]
import psutil
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def monitor():
    try:
        while True:
            clear_screen()
            print("="*20, "System Monitor", "="*20)
            
            # CPU info
            print(f"CPU Usage: {psutil.cpu_percent()}%")
            
            # Memory info
            svmem = psutil.virtual_memory()
            print(f"Memory: {get_size(svmem.used)} / {get_size(svmem.total)} ({svmem.percent}%)")
            
            # Disk info
            print("\nDisk Usage:")
            for partition in psutil.disk_partitions():
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                except PermissionError:
                    continue
                print(f"  Drive {partition.device}: {get_size(partition_usage.used)} / {get_size(partition_usage.total)} ({partition_usage.percent}%)")
            
            # Network info
            net_io = psutil.net_io_counters()
            print(f"\nNetwork: Sent: {get_size(net_io.bytes_sent)}, Received: {get_size(net_io.bytes_recv)}")
            
            print("\nPress Ctrl+C to stop.")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor()
