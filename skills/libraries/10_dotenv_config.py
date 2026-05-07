import os

def run_demo():
    """
    Demonstrates environment variable management.
    (Simulates .env behavior using os.environ)
    """
    # 1. Setting environment variables (Simulating .env load)
    os.environ["API_KEY"] = "sk-1234567890abcdef"
    os.environ["DB_URL"] = "postgresql://user:pass@localhost:5432/mydb"
    
    # 2. Accessing variables
    api_key = os.getenv("API_KEY")
    db_url = os.getenv("DB_URL")
    debug_mode = os.getenv("DEBUG", "False") # With default value
    
    print("--- Configuration Loaded ---")
    print(f"API Key: {api_key[:5]}... (hidden)")
    print(f"Database: {db_url}")
    print(f"Debug Mode: {debug_mode}")
    
    if not api_key:
        print("Warning: API_KEY is missing!")

if __name__ == "__main__":
    run_demo()
