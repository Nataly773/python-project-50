def format_stylish(diff_tree, depth=0):
    def stringify(value, depth):
        """Приводит значение к строковому виду."""
        if isinstance(value, dict):
            return stringify_dict(value, depth)
        if value is None:
            return 'null'
        if isinstance(value, bool):
            return str(value).lower()
        return str(value)

    def stringify_dict(value, depth):
        """Превращает словарь в строку с нужным отступом."""
        lines = []
        indent = ' ' * (depth * 4)
        closing_indent = ' ' * ((depth - 1) * 4)
        for k, v in value.items():
            lines.append(
                f"{indent}    {k}: {stringify(v, depth + 1)}"
            )
        return (
            "{\n" + '\n'.join(lines) + "\n" + closing_indent + "    }"
        )

    def process_added(item, depth):
        """Обрабатывает добавленные элементы."""
        return (
            f"{' ' * (depth * 4)}  + {item['key']}: "
            f"{stringify(item['value'], depth + 1)}"
        )

    def process_removed(item, depth):
        """Обрабатывает удалённые элементы."""
        return (
            f"{' ' * (depth * 4)}  - {item['key']}: "
            f"{stringify(item['value'], depth + 1)}"
        )

    def process_unchanged(item, depth):
        """Обрабатывает неизменённые элементы."""
        return (
            f"{' ' * (depth * 4)}    {item['key']}: "
            f"{stringify(item['value'], depth + 1)}"
        )

    def process_changed(item, depth):
        """Обрабатывает изменённые элементы."""
        indent = ' ' * (depth * 4)
        old_value = (
            f"{indent}  - {item['key']}: "
            f"{stringify(item['old_value'], depth + 1)}"
        )
        new_value = (
            f"{indent}  + {item['key']}: "
            f"{stringify(item['new_value'], depth + 1)}"
        )
        return old_value + '\n' + new_value

    def process_nested(item, depth):
        """Обрабатывает вложенные элементы."""
        children = format_stylish(item['children'], depth + 1)
        return (
            f"{' ' * (depth * 4)}    {item['key']}: {children}"
        )

    result = []
    for item in diff_tree:
        type_ = item["type"]
        if type_ == "added":
            result.append(process_added(item, depth))
        elif type_ == "removed":
            result.append(process_removed(item, depth))
        elif type_ == "unchanged":
            result.append(process_unchanged(item, depth))
        elif type_ == "changed":
            result.append(process_changed(item, depth))
        elif type_ == "nested":
            result.append(process_nested(item, depth))

    return "{\n" + "\n".join(result) + f"\n{' ' * (depth * 4)}}}"