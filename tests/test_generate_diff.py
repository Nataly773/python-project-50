import pytest
from gendiff.diff.generate_diff import generate_diff
from gendiff.diff.diff_builder import build_diff
from gendiff.formattes.plain import format_plain
import os


from gendiff import generate_diff

def test_generate_diff_yaml():
    base_path = os.path.join(os.path.dirname(__file__), 'test_data')

    file1 = os.path.join(base_path, 'file1.yml')
    file2 = os.path.join(base_path, 'file2.yml')

    expected_output = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(file1, file2) == expected_output

def test_generate_diff_rec_yaml():
    base_path = os.path.join(os.path.dirname(__file__), 'test_data')
    file1 = os.path.join(base_path, 'rec_file1.yml')
    file2 = os.path.join(base_path, 'rec_file2.yml')

    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

    assert generate_diff(file1, file2) == expected



def test_generate_diff_plain():
    base_path = os.path.join(os.path.dirname(__file__), 'test_data')
    file1 = os.path.join(base_path, 'rec_file1.json')
    file2 = os.path.join(base_path, 'rec_file2.json')

    expected = """\
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

    result = generate_diff(file1, file2, format_name='plain')
    assert result == expected