
import json
import yaml


from gendiff.scripts.diff.parse_file import parse_file 

def test_parse_json(tmp_path):
    test_data = {"name": "test", "value": 123}
    file = tmp_path / "data.json"
    file.write_text(json.dumps(test_data), encoding="utf-8")

    result = parse_file(str(file))
    assert result == test_data

def test_parse_yaml(tmp_path):
    test_data = {"foo": "bar", "nested": {"a": 1}}
    file = tmp_path / "data.yaml"
    file.write_text(yaml.dump(test_data), encoding="utf-8")

    result = parse_file(str(file))
    assert result == test_data