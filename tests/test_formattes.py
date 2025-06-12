from gendiff.formattes import plain
from gendiff.formattes import stylish


def test_stringify_none():
    assert plain.stringify(None) == 'null'


def test_get_indent():
    assert stylish.get_indent(0) == ''
    assert stylish.get_indent(1) == '    '
    assert stylish.get_indent(3) == '            '

def test_stringify_simple():
    assert stylish.stringify(None, 0) == 'null'
    assert stylish.stringify(True, 0) == 'true'
    assert stylish.stringify(False, 0) == 'false'
    assert stylish.stringify(123, 0) == '123'
    assert stylish.stringify('abc', 0) == 'abc'


def test_format_stylish_basic():
    diff = [
        {'key': 'a', 'type': 'added', 'value': 'val'},
        {'key': 'b', 'type': 'removed', 'value': 123},
        {'key': 'c', 'type': 'unchanged', 'value': True},
        {'key': 'd', 'type': 'changed', 'old_value': 'old', 'new_value': 'new'},
        {'key': 'e', 'type': 'nested', 'children': [
            {'key': 'f', 'type': 'added', 'value': 'nested_val'}
        ]},
    ]
    output = stylish.format_stylish(diff)
    assert '+ a: val' in output
    assert '- b: 123' in output
    assert '  c: true' in output
    assert '- d: old' in output
    assert '+ d: new' in output