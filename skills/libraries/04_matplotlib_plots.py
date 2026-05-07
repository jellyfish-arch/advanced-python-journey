import matplotlib.pyplot as plt
import numpy as np

def create_plot():
    """
    Demonstrates basic plotting with Matplotlib.
    Note: In a terminal environment, this usually saves to a file.
    """
    # Data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    # Create plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='Sine Wave', color='blue', linestyle='--')
    plt.plot(x, y2, label='Cosine Wave', color='red')
    
    # Styling
    plt.title("Wave Visualization")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Output
    print("Plotting data... (Saving to wave_plot.png)")
    plt.savefig("wave_plot.png")
    # plt.show() # Uncomment if running in local GUI environment

if __name__ == "__main__":
    create_plot()
