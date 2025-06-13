from gendiff.scripts.diff.diff_builder import build_diff


def test_build_diff():
    data1 = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
        'nested': {
            'key1': 'value1',
            'key2': 'value2',
        }
    }
    data2 = {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io',
        'nested': {
            'key1': 'value1',
            'key3': 'value3',
        }
    }

    expected = [
        {'key': 'follow', 'type': 'removed', 'value': False},
        {'key': 'host', 'type': 'unchanged', 'value': 'hexlet.io'},
        {'key': 'nested', 'type': 'nested', 'children': [
            {'key': 'key1', 'type': 'unchanged', 'value': 'value1'},
            {'key': 'key2', 'type': 'removed', 'value': 'value2'},
            {'key': 'key3', 'type': 'added', 'value': 'value3'},
        ]},
        {'key': 'proxy', 'type': 'removed', 'value': '123.234.53.22'},
        {'key': 'timeout', 'type': 'changed', 'old_value': 50, 'new_value': 20},
        {'key': 'verbose', 'type': 'added', 'value': True},
    ]

    diff = build_diff(data1, data2)
    assert diff == expected