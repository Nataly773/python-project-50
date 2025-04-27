from gendiff.scripts.gendiff import generate_diff, parse_file
import yaml
import pytest
import argparse



def test_compare_yaml_files():
    # Создаем тестовые YAML файлы
    yaml1 = """
    follow: false
    host: hexlet.io
    timeout: 50
    """
    yaml2 = """
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 20
    verbose: true
    """

    with open('test1.yml', 'w') as f:
        f.write(yaml1)

    with open('test2.yml', 'w') as f:
        f.write(yaml2)

    # Ожидаемый результат
    expected_diff = [
        {'key': 'follow', 'value': False, 'action': '- '},
        {'key': 'proxy', 'value': '123.234.53.22', 'action': '+ '},
        {'key': 'timeout', 'old_value': 50, 'new_value': 20},
        {'key': 'verbose', 'value': True, 'action': '+ '}
    ]

    # Сравниваем файлы
    data1 = parse_file('test1.yml')
    data2 = parse_file('test2.yml')
    diff = generate_diff(data1, data2)

    assert diff == expected_diff
