from gendiff.diff.generate_diff import generate_diff


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