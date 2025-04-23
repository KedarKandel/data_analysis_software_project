import requests
import json
from pathlib import Path



def fetch_zoo_data(api_url: str) -> dict:
    """Fetch data from zoo API"""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"API request failed: {str(e)}")

def save_to_json(data: dict, filepath: str) -> None:
    """Save data to JSON file"""
    try:
        Path(filepath).parent.mkdir(exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except (IOError, TypeError) as e:
        raise RuntimeError(f"Failed to save data: {str(e)}")