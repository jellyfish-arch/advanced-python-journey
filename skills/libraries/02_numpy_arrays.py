import numpy as np

def run_demo():
    """
    Demonstrates NumPy array operations, broadcasting, and linear algebra.
    """
    # 1. Creating arrays
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Original Array: {arr}")
    
    # 2. Vectorized operations
    print(f"Square of elements: {arr**2}")
    
    # 3. Multi-dimensional arrays
    matrix = np.random.rand(3, 3)
    print("\n3x3 Random Matrix:")
    print(matrix)
    
    # 4. Linear Algebra: Matrix multiplication
    identity = np.eye(3)
    product = np.dot(matrix, identity)
    print("\nMatrix * Identity (should be same):")
    print(product)
    
    # 5. Aggregations
    print(f"\nMean: {np.mean(matrix):.4f}")
    print(f"Std Dev: {np.std(matrix):.4f}")

if __name__ == "__main__":
    run_demo()
