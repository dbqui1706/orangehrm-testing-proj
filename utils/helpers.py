import os
import json
from datetime import datetime 

def load_json(file_name):
    """Load JSON data from a file."""
    data_dir = os.path.join('data', file_name)
    with open(data_dir, 'r') as file:
        return json.load(file)
    
def get_timestamp():
    """Get the current timestamp as a string."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def get_screenshot_name(file_name):
    """Generate a screenshot file name with timestamp."""
    timestamp = get_timestamp()
    return f"{file_name}_{timestamp}.png"

def get_abs_path(filename):
    """Get absolute path from a relative path."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(current_dir)
    return os.path.join(project_dir, filename)