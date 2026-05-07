import pandas as pd
import io

def run_demo():
    """
    Demonstrates Pandas Series/DataFrame, filtering, and aggregation.
    """
    # Simulate a CSV file
    csv_data = """Name,Age,Role,Salary
Alice,30,Dev,90000
Bob,25,Designer,70000
Charlie,35,Dev,110000
David,28,QA,65000
Eve,32,Dev,105000
"""
    
    # Load data
    df = pd.read_csv(io.StringIO(csv_data))
    
    print("--- Full DataFrame ---")
    print(df)
    
    # Filtering
    devs = df[df['Role'] == 'Dev']
    print("\n--- Filtering: Developers Only ---")
    print(devs)
    
    # Aggregation
    avg_salary = df.groupby('Role')['Salary'].mean()
    print("\n--- Average Salary by Role ---")
    print(avg_salary)
    
    # Adding a column
    df['Senior'] = df['Age'] > 30
    print("\n--- After adding 'Senior' column ---")
    print(df)

if __name__ == "__main__":
    run_demo()
