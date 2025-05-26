from gendiff.diff.generate_diff import generate_diff
from gendiff.diff.diff_builder import build_diff
from gendiff.formattes.plain import format_plain
import os


def test_generate_diff_yaml(tmp_path):
    file1 = tmp_path / "file1.yml"
    file2 = tmp_path / "file2.yml"

    file1.write_text("""\
follow: false
host: hexlet.io
timeout: 50
""")

    file2.write_text("""\
host: hexlet.io
proxy: 123.234.53.22
timeout: 20
verbose: true
""")

    expected = """\
{
  - follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(str(file1), str(file2)) == expected


def test_build_diff():
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}

    expected = [
        {"key": "a", "type": "removed", "value": 1},
        {"key": "b", "type": "changed", "old_value": 2, "new_value": 3},
        {"key": "c", "type": "added", "value": 4},
    ]
    
    assert build_diff(dict1, dict2) == expected


TEST_PROXY_IP = os.getenv('TEST_PROXY_IP', '123.234.53.22')


def test_format_plain():
    diff = [
        {'key': 'host', 'type': 'unchanged', 'value': 'hexlet.io'},
        {'key': 'timeout', 'type': 'changed', 'old_value': 50, 'new_value': 20},
        {'key': 'proxy', 'type': 'removed', 'value': TEST_PROXY_IP},
        {'key': 'verbose', 'type': 'added', 'value': True},
        {'key': 'group', 'type': 'nested', 'children': [
            {'key': 'name', 'type': 'added', 'value': {'a': 1}}
        ]}
    ]
    
    expected = (
        "Property 'timeout' was updated. From 50 to 20\n"
        "Property 'proxy' was removed\n"
        "Property 'verbose' was added with value: true\n"
        "Property 'group.name' was added with value: [complex value]"
    )

    assert format_plain(diff) == expected
