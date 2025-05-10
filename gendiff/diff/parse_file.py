import os
import yaml
import json

def parse_file(filepath):
    ext = os.path.splitext(filepath)[1]
    with open(filepath, 'r') as file:
        if ext in ['.yml', '.yaml']:
            return yaml.safe_load(file)
        elif ext == '.json':
            return json.load(file)
        else:
            raise ValueError("Unsupported file format")