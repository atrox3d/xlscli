from helpers import files


def test_get_files(temp_dir, fake_files):
    assert files.get_files(temp_dir) == fake_files


def test_get_files_match(temp_dir, fake_files):
    assert files.get_files(temp_dir, match='1') == ['1.xls']


def test_get_files_match_case_sensitive(temp_dir, fake_files):
    assert files.get_files(temp_dir, match='a', case=True) == ['a.xls']
    assert files.get_files(temp_dir, match='A', case=True) == []


def test_get_files_reverse(temp_dir, fake_files):
    assert files.get_files(temp_dir, reverse=True) == sorted(fake_files, reverse=True)


def test_get_files_empty(temp_dir):
    assert files.get_files(temp_dir) == []


