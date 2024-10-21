import pytest
from unittest import mock
import urllib.request
from bs4 import BeautifulSoup
import Scripts.P06_GetMeaning  # Assuming the script is in this module

@pytest.fixture
def mock_dependencies():
    # Mocking urllib.request.urlopen
    mock_urlopen = mock.patch('urllib.request.urlopen').start()
    
    # Mocking BeautifulSoup
    mock_bs4 = mock.patch('bs4.BeautifulSoup').start()

    # Mocking input
    mock_input = mock.patch('builtins.input', return_value='example').start()

    yield {
        'urlopen': mock_urlopen,
        'BeautifulSoup': mock_bs4,
        'input': mock_input,
    }

    # Stop all patches
    mock.patch.stopall()

# happy path - fetch_word_meaning - Test that the word meaning is fetched successfully from vocabulary.com
def test_fetch_word_meaning_success(mock_dependencies):
    mock_dependencies['urlopen'].return_value.read.return_value = '<div class="short">a representative form or pattern</div>'
    mock_dependencies['BeautifulSoup'].return_value.find.return_value.get_text.return_value = 'a representative form or pattern'
    from Scripts.P06_GetMeaning import fetch_word_meaning
    short_meaning, long_meaning = fetch_word_meaning('example')
    assert short_meaning == 'a representative form or pattern'
    assert long_meaning == 'a representative form or pattern of something'


# happy path - print_short_meaning - Test that the short meaning is printed correctly
def test_print_short_meaning(mock_dependencies, capsys):
    from Scripts.P06_GetMeaning import print_short_meaning
    print_short_meaning('a representative form or pattern')
    captured = capsys.readouterr()
    assert 'SHORT MEANING: a representative form or pattern' in captured.out


# happy path - print_long_meaning - Test that the long meaning is printed correctly
def test_print_long_meaning(mock_dependencies, capsys):
    from Scripts.P06_GetMeaning import print_long_meaning
    print_long_meaning('a representative form or pattern of something')
    captured = capsys.readouterr()
    assert 'a representative form or pattern of something' in captured.out


# happy path - print_synonyms_antonyms - Test that synonyms and antonyms are printed correctly
def test_print_synonyms_antonyms(mock_dependencies, capsys):
    from Scripts.P06_GetMeaning import print_synonyms_antonyms
    print_synonyms_antonyms('Synonyms: illustration, model')
    captured = capsys.readouterr()
    assert 'Synonyms: illustration, model' in captured.out


# happy path - generate_url - Test that the input word is correctly appended to the URL
def test_generate_url(mock_dependencies):
    from Scripts.P06_GetMeaning import generate_url
    url = generate_url('example')
    assert url == 'https://www.vocabulary.com/dictionary/example'


# edge case - handle_word_not_found - Test that an error message is printed if the word is not found
def test_handle_word_not_found(mock_dependencies, capsys):
    mock_dependencies['BeautifulSoup'].return_value.find.return_value = None
    from Scripts.P06_GetMeaning import fetch_word_meaning
    fetch_word_meaning('nonexistentword')
    captured = capsys.readouterr()
    assert 'Cannot find such word! Check spelling.' in captured.out


# edge case - exit_on_word_not_found - Test that the program exits gracefully if the word is not found
def test_exit_on_word_not_found(mock_dependencies):
    mock_dependencies['BeautifulSoup'].return_value.find.return_value = None
    with pytest.raises(SystemExit) as e:
        from Scripts.P06_GetMeaning import fetch_word_meaning
        fetch_word_meaning('nonexistentword')
    assert e.type == SystemExit
    assert e.value.code == 1


# edge case - handle_network_error - Test that the program handles network errors gracefully
def test_handle_network_error(mock_dependencies, capsys):
    mock_dependencies['urlopen'].side_effect = urllib.error.URLError('Network error')
    from Scripts.P06_GetMeaning import fetch_word_meaning
    fetch_word_meaning('example')
    captured = capsys.readouterr()
    assert 'Network error occurred' in captured.out


# edge case - handle_unexpected_html - Test that the program handles unexpected HTML structure gracefully
def test_handle_unexpected_html(mock_dependencies, capsys):
    mock_dependencies['BeautifulSoup'].return_value.find.return_value = None
    from Scripts.P06_GetMeaning import fetch_word_meaning
    fetch_word_meaning('example')
    captured = capsys.readouterr()
    assert 'Cannot find such word! Check spelling.' in captured.out


# edge case - handle_empty_input - Test that the program can handle empty input
def test_handle_empty_input(mock_dependencies, capsys):
    mock_dependencies['input'].return_value = ''
    from Scripts.P06_GetMeaning import fetch_word_meaning
    fetch_word_meaning('')
    captured = capsys.readouterr()
    assert 'Cannot find such word! Check spelling.' in captured.out


