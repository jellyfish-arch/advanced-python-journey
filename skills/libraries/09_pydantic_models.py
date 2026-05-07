# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field, EmailStr, ValidationError
from typing import List, Optional

class User(BaseModel):
    """
    Demonstrates data validation and type enforcement with Pydantic.
    """
    id: int
    name: str = Field(min_length=2)
    email: str
    tags: List[str] = []
    is_active: bool = True

def validate_data():
    # Valid data
    valid_data = {
        "id": 101,
        "name": "Jelly Fish",
        "email": "jelly@example.com",
        "tags": ["python", "dev"]
    }
    
    try:
        user = User(**valid_data)
        print("✅ Validation Success!")
        print(user.model_dump_json(indent=2))
    except ValidationError as e:
        print(f"❌ Validation Error: {e.json()}")

    # Invalid data
    invalid_data = {"id": "abc", "name": "J"}
    print("\nAttempting to validate invalid data...")
    try:
        User(**invalid_data)
    except ValidationError as e:
        print("Caught expected error:")
        print(e.errors()[0]['msg'])

if __name__ == "__main__":
    validate_data()
