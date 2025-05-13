def format_stylish(diff_tree, depth=0):
    def stringify(value, depth):
        if isinstance(value, dict):
            lines = []
            indent = ' ' * (depth * 4)
            closing_indent = ' ' * ((depth - 1) * 4)
            for k, v in value.items():
                lines.append(f"{indent}    {k}: {stringify(v, depth + 1)}")
            return "{\n" + '\n'.join(lines) + "\n" + closing_indent + "    }"
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)

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
            result.append(f"{indent}    {key}: {children}")
    return "{\n" + "\n".join(result) + f"\n{indent}}}"