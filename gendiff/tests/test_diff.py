from gendiff.diff import generate_diff


def test_generate_test(case_data):
    result = case_data.read()
    assert generate_diff('gendiff/file1.json', 'gendiff/file2.json') == result
