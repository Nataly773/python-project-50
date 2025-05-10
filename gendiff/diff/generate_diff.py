from .parse_file import parse_file
from .diff_builder import build_diff
from gendiff.formattes.stylish import  format_stylish
from gendiff.formattes.plain import format_plain
from gendiff.formattes.json import format_json

def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return format_stylish(diff)
    if format_name == 'plain':
        return format_plain(diff)
    if format_name == 'json':
        return format_json(diff)
    raise ValueError(f"Unknown format: {format_name}")