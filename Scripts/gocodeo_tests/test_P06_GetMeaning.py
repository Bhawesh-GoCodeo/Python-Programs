import pytest
from unittest import mock
import urllib.request
from bs4 import BeautifulSoup
import Scripts.P06_GetMeaning as get_meaning

@pytest.fixture
def mock_urlopen():
    with mock.patch('urllib.request.urlopen') as mock_urlopen:
        yield mock_urlopen

@pytest.fixture
def mock_beautifulsoup():
    with mock.patch('bs4.BeautifulSoup') as mock_bs:
        yield mock_bs

@pytest.fixture
def mock_input(monkeypatch):
    def mock_input_func(word):
        monkeypatch.setattr('builtins.input', lambda _: word)
    return mock_input_func

@pytest.fixture
def mock_soup_find(mock_beautifulsoup):
    mock_soup = mock.Mock()
    mock_beautifulsoup.return_value = mock_soup
    return mock_soup

@pytest.fixture
def mock_get_text(mock_soup_find):
    mock_soup_find.find.return_value.get_text.return_value = "a representative form or pattern"
    return mock_soup_find

@pytest.fixture
def mock_exit():
    with mock.patch('builtins.exit') as mock_exit:
        yield mock_exit

# happy path - get_short_meaning - Test that a valid word returns a short meaning
def test_get_short_meaning_valid_word(mock_input, mock_urlopen, mock_get_text):
    mock_input('example')
    mock_urlopen.return_value = mock.Mock()
    mock_get_text.find.return_value.get_text.return_value = 'a representative form or pattern'
    import Scripts.P06_GetMeaning as get_meaning
    assert get_meaning.soup1 == 'a representative form or pattern'


# happy path - get_long_meaning - Test that a valid word returns a long meaning
def test_get_long_meaning_valid_word(mock_input, mock_urlopen, mock_get_text):
    mock_input('example')
    mock_urlopen.return_value = mock.Mock()
    mock_get_text.find.return_value.get_text.return_value = 'a representative form or pattern'
    import Scripts.P06_GetMeaning as get_meaning
    assert get_meaning.soup2 == 'a representative form or pattern'


# happy path - get_word_instances - Test that a valid word returns synonyms and antonyms
def test_get_word_instances_valid_word(mock_input, mock_urlopen, mock_get_text):
    mock_input('example')
    mock_urlopen.return_value = mock.Mock()
    mock_get_text.find.return_value.get_text.return_value = 'synonyms, antonyms'
    import Scripts.P06_GetMeaning as get_meaning
    assert get_meaning.txt1 == 'synonyms, antonyms'


# happy path - form_url - Test that the URL is correctly formed for a valid word
def test_form_url_valid_word(mock_input):
    mock_input('example')
    import Scripts.P06_GetMeaning as get_meaning
    expected_url = 'https://www.vocabulary.com/dictionary/example'
    assert get_meaning.url == expected_url


# happy path - parse_html - Test that BeautifulSoup parses the HTML correctly for a valid word
def test_parse_html_valid_word(mock_urlopen, mock_beautifulsoup):
    html = "<div class='short'>a representative form or pattern</div>"
    mock_urlopen.return_value.read.return_value = html
    mock_soup = mock.Mock()
    mock_beautifulsoup.return_value = mock_soup
    mock_soup.find.return_value.get_text.return_value = 'a representative form or pattern'
    import Scripts.P06_GetMeaning as get_meaning
    assert get_meaning.soup1 == 'a representative form or pattern'


# edge case - get_short_meaning - Test that an invalid word returns an error message
def test_get_short_meaning_invalid_word(mock_input, mock_urlopen, mock_soup_find, mock_exit):
    mock_input('xyzabc')
    mock_urlopen.return_value = mock.Mock()
    mock_soup_find.find.return_value = None
    import Scripts.P06_GetMeaning as get_meaning
    mock_exit.assert_called_once()
    assert get_meaning.soup1 is None


# edge case - get_short_meaning - Test that an empty input returns an error message
def test_get_short_meaning_empty_input(mock_input, mock_urlopen, mock_soup_find, mock_exit):
    mock_input('')
    mock_urlopen.return_value = mock.Mock()
    mock_soup_find.find.return_value = None
    import Scripts.P06_GetMeaning as get_meaning
    mock_exit.assert_called_once()
    assert get_meaning.soup1 is None


# edge case - get_short_meaning - Test that a special character input returns an error message
def test_get_short_meaning_special_chars(mock_input, mock_urlopen, mock_soup_find, mock_exit):
    mock_input('@#$%')
    mock_urlopen.return_value = mock.Mock()
    mock_soup_find.find.return_value = None
    import Scripts.P06_GetMeaning as get_meaning
    mock_exit.assert_called_once()
    assert get_meaning.soup1 is None


# edge case - get_short_meaning - Test that a numerical input returns an error message
def test_get_short_meaning_numerical_input(mock_input, mock_urlopen, mock_soup_find, mock_exit):
    mock_input('12345')
    mock_urlopen.return_value = mock.Mock()
    mock_soup_find.find.return_value = None
    import Scripts.P06_GetMeaning as get_meaning
    mock_exit.assert_called_once()
    assert get_meaning.soup1 is None


# edge case - get_short_meaning - Test that a very long word returns an error message
def test_get_short_meaning_long_word(mock_input, mock_urlopen, mock_soup_find, mock_exit):
    mock_input('supercalifragilisticexpialidocious')
    mock_urlopen.return_value = mock.Mock()
    mock_soup_find.find.return_value = None
    import Scripts.P06_GetMeaning as get_meaning
    mock_exit.assert_called_once()
    assert get_meaning.soup1 is None


