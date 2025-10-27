import json
import os

def read_json(file_path):
    """Read and return data from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"✗ File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON in {file_path}: {e}")
        return None


def write_json(data, file_path, indent=4):
    """Write data to a JSON file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        print(f"✓ Written JSON to: {file_path}")
        return True
    except Exception as e:
        print(f"✗ Error writing JSON: {e}")
        return False