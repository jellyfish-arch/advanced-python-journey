from tqdm import tqdm
import time

def run_simulation():
    """
    Demonstrates progress bars with tqdm.
    """
    print("Starting long-running process...")
    
    # Simple loop
    for i in tqdm(range(100), desc="Processing Tasks"):
        time.sleep(0.02)  # Simulate work
        
    # Manual update example
    pbar = tqdm(total=50, desc="Downloading Data", colour="green")
    for i in range(5):
        time.sleep(0.2)
        pbar.update(10)
    pbar.close()

if __name__ == "__main__":
    run_simulation()
