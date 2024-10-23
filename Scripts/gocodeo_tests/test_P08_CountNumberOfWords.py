import pytest
from unittest import mock
from Scripts.P08_CountNumberOfWords import countWords

@pytest.fixture
def mock_open_file():
    mock_file = mock.mock_open(read_data='This is a test file.\nIt has multiple lines.\n')
    with mock.patch('builtins.open', mock_file):
        yield mock_file

@pytest.fixture
def mock_countWords():
    with mock.patch('Scripts.P08_CountNumberOfWords.countWords') as mock_count:
        yield mock_count

# happy path - countWords - Test that countWords correctly counts words, lines, and characters in a typical file
def test_count_words_typical_file(mock_open_file):
    mock_open_file.return_value.read_data = 'word ' * 100 + '\n' * 9
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('typical_file.txt')
            mock_print.assert_any_call('Words: ', 100)
            mock_print.assert_any_call('Lines: ', 10)
            mock_print.assert_any_call('Characters: ', 600)


# happy path - countWords - Test that countWords correctly handles a file with a single line of text
def test_count_words_single_line(mock_open_file):
    mock_open_file.return_value.read_data = 'word ' * 10
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('single_line.txt')
            mock_print.assert_any_call('Words: ', 10)
            mock_print.assert_any_call('Lines: ', 1)
            mock_print.assert_any_call('Characters: ', 50)


# happy path - countWords - Test that countWords correctly counts an empty file
def test_count_words_empty_file(mock_open_file):
    mock_open_file.return_value.read_data = ''
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('empty_file.txt')
            mock_print.assert_any_call('Words: ', 0)
            mock_print.assert_any_call('Lines: ', 0)
            mock_print.assert_any_call('Characters: ', 0)


# happy path - countWords - Test that countWords correctly counts a file with multiple empty lines
def test_count_words_multiple_empty_lines(mock_open_file):
    mock_open_file.return_value.read_data = '\n' * 5
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('multiple_empty_lines.txt')
            mock_print.assert_any_call('Words: ', 0)
            mock_print.assert_any_call('Lines: ', 5)
            mock_print.assert_any_call('Characters: ', 10)


# happy path - countWords - Test that countWords correctly counts a file with special characters
def test_count_words_special_characters(mock_open_file):
    mock_open_file.return_value.read_data = '@#$%^&*()_+!\n' * 3
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('special_characters.txt')
            mock_print.assert_any_call('Words: ', 15)
            mock_print.assert_any_call('Lines: ', 3)
            mock_print.assert_any_call('Characters: ', 100)


# edge case - countWords - Test that countWords handles a file with very long lines without crashing
def test_count_words_long_lines(mock_open_file):
    mock_open_file.return_value.read_data = 'word ' * 500
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('long_lines.txt')
            mock_print.assert_any_call('Words: ', 500)
            mock_print.assert_any_call('Lines: ', 1)
            mock_print.assert_any_call('Characters: ', 3000)


# edge case - countWords - Test that countWords handles a non-existent file gracefully
def test_count_words_non_existent_file():
    with mock.patch('builtins.open', side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            countWords('non_existent.txt')


# edge case - countWords - Test that countWords handles a binary file without crashing
def test_count_words_binary_file():
    with mock.patch('builtins.open', mock.mock_open(read_data=b'\x00\x01\x02')):
        with pytest.raises(UnicodeDecodeError):
            countWords('binary_file.bin')


# edge case - countWords - Test that countWords handles a file with only whitespace characters
def test_count_words_whitespace_only(mock_open_file):
    mock_open_file.return_value.read_data = ' ' * 30 + '\n' * 10
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('whitespace_only.txt')
            mock_print.assert_any_call('Words: ', 0)
            mock_print.assert_any_call('Lines: ', 10)
            mock_print.assert_any_call('Characters: ', 30)


# edge case - countWords - Test that countWords handles a file with mixed line endings
def test_count_words_mixed_line_endings(mock_open_file):
    mock_open_file.return_value.read_data = 'word\rword\nword\r\n' * 10
    with mock.patch('builtins.open', mock_open_file):
        with mock.patch('builtins.print') as mock_print:
            countWords('mixed_line_endings.txt')
            mock_print.assert_any_call('Words: ', 50)
            mock_print.assert_any_call('Lines: ', 10)
            mock_print.assert_any_call('Characters: ', 300)


