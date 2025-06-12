import sys
from gendiff.scripts.gendiff import main


def test_main_cli(monkeypatch, capsys, tmp_path):
    
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    
    file1.write_text('{"key": "value"}', encoding='utf-8')
    file2.write_text('{"key": "value"}', encoding='utf-8')

    monkeypatch.setattr(sys, 'argv', ['gendiff', str(file1), str(file2)])

    main()

    captured = capsys.readouterr()
    assert captured.out.strip() == '{\n    key: value\n}'