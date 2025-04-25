import argparse
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

def generate_diff(data1, data2):
    diff = []
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key in data1 and key not in data2:
            diff.append({'key': key, 'value': data1[key], 'action': '- '})
        elif key not in data1 and key in data2:
            diff.append({'key': key, 'value': data2[key], 'action': '+ '})
        elif data1[key] != data2[key]:
            diff.append({'key': key, 'old_value': data1[key], 'new_value': data2[key]})
    return diff

def format_diff(diff):
    output = []
    for item in diff:
        if 'old_value' in item and 'new_value' in item:
            output.append(f"  - {item['key']}: {item['old_value']}")
            output.append(f"  + {item['key']}: {item['new_value']}")
        else:
            output.append(f"{item['action']} {item['key']}: {item['value']}")
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='Path to the first file to compare.')
    parser.add_argument('second_file', help='Path to the second file to compare.')
    args = parser.parse_args()
    
    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)
    diff = generate_diff(data1, data2)
    print(format_diff(diff))

if __name__ == '__main__':
    main()

