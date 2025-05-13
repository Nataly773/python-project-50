def format_stylish(diff_tree, depth=0):
    def stringify(value, depth):
        if not isinstance(value, dict):
            return str(value).lower() if isinstance(value, bool) or value is None else str(value)
        lines = []
        indent = ' ' * (depth * 4)
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {stringify(v, depth + 1)}")
        return f"{{\n" + '\n'.join(lines) + f"\n{indent}}}"

    indent = ' ' * (depth * 4)
    result = []

    for item in diff_tree:
        key = item["key"]
        type_ = item["type"]
        if type_ == "added":
            result.append(f"{indent}  + {key}: {stringify(item['value'], depth + 1)}")
        elif type_ == "removed":
            result.append(f"{indent}  - {key}: {stringify(item['value'], depth + 1)}")
        elif type_ == "unchanged":
            result.append(f"{indent}    {key}: {stringify(item['value'], depth + 1)}")
        elif type_ == "changed":
            result.append(f"{indent}  - {key}: {stringify(item['old_value'], depth + 1)}")
            result.append(f"{indent}  + {key}: {stringify(item['new_value'], depth + 1)}")
        elif type_ == "nested":
            children = format_stylish(item['children'], depth + 1)
            result.append(f"{indent}    {key}: {{\n{children}\n{indent}    }}")
    return "{\n" + "\n".join(result) + f"\n{indent}}}"