def stringify(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)

def walk(tree, path=''):
    lines = []
    for node in tree:
        full_path = f"{path}.{node['key']}" if path else node['key']

        match node['type']:
            case 'added':
                value = stringify(node['value'])
                lines.append(
                    f"Property '{full_path}' was added with value: {value}"
                )

            case 'removed':
                lines.append(f"Property '{full_path}' was removed")

            case 'changed':
                old = stringify(node['old_value'])
                new = stringify(node['new_value'])
                lines.append(
                    f"Property '{full_path}' was updated. "
                    f"From {old} to {new}"
                )

            case 'nested':
                lines.extend(walk(node['children'], full_path))

    return lines

def format_plain(diff_tree):
    return '\n'.join(walk(diff_tree))