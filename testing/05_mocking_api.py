"""
05_mocking_api.py
------------------
Mocking is crucial for testing code that depends on external services (APIs, Databases, etc).
This script shows how to use 'unittest.mock' to simulate API responses without making actual HTTP requests.

Concepts:
- unittest.mock.patch
- Mock objects
- assert_called_with
"""

import unittest
from unittest.mock import patch, MagicMock

# The function we want to test
def get_weather_report(city):
    """
    Imagine this function uses the 'requests' library to call an API.
    Since we don't want to rely on the internet during tests, we will mock 'requests'.
    """
    import requests  # Local import for demonstration
    response = requests.get(f"https://api.weather.com/v1/{city}")
    if response.status_code == 200:
        data = response.json()
        return f"The weather in {city} is {data['condition']}."
    return "Weather data unavailable."

class TestWeatherAPI(unittest.TestCase):
    
    @patch('requests.get')
    def test_get_weather_success(self, mock_get):
        """Mocking a successful API response."""
        # 1. Setup the mock response object
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"condition": "Sunny"}
        
        # 2. Tell the mock_get to return our fake response
        mock_get.return_value = mock_response
        
        # 3. Call the function
        result = get_weather_report("London")
        
        # 4. Assertions
        self.assertEqual(result, "The weather in London is Sunny.")
        mock_get.assert_called_with("https://api.weather.com/v1/London")

    @patch('requests.get')
    def test_get_weather_failure(self, mock_get):
        """Mocking a failed API response (e.g., 404)."""
        mock_get.return_value.status_code = 404
        
        result = get_weather_report("Atlantis")
        
        self.assertEqual(result, "Weather data unavailable.")

if __name__ == "__main__":
    # Note: If 'requests' is not installed, the test might fail at the import.
    # In a real environment, you'd have requirements.txt.
    print("Running Mocking Tests...")
    unittest.main()
