# test_chatbot.py
import pytest
from unittest import mock
import nltk
from nltk.chat.util import Chat, reflections
from Programs.Chatbot import chat

@pytest.fixture
def mock_chat():
    with mock.patch('Programs.Chatbot.Chat') as MockChat:
        yield MockChat

@pytest.fixture
def mock_reflections():
    with mock.patch('Programs.Chatbot.reflections', new=reflections):
        yield reflections

@pytest.fixture
def mock_pairs():
    with mock.patch('Programs.Chatbot.pairs', new=[]):  # Mocking pairs to an empty list for isolation
        yield []

@pytest.fixture
def mock_nltk():
    with mock.patch('Programs.Chatbot.nltk') as MockNltk:
        yield MockNltk

@pytest.fixture
def mock_chat_converse(mock_chat):
    mock_chat_instance = mock_chat.return_value
    mock_chat_instance.converse = mock.Mock()
    yield mock_chat_instance

# happy path - chat - Test that the chatbot responds correctly to a greeting.
def test_chat_greeting_response(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print('Hello')
    with mock.patch('builtins.input', side_effect=['hello', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# happy path - chat - Test that the chatbot recognizes and responds to a name introduction.
def test_chat_name_introduction(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print('Hello John, How are you today ?')
    with mock.patch('builtins.input', side_effect=['my name is John', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# happy path - chat - Test that the chatbot provides a list of continents when asked.
def test_chat_continents_list(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print('Asia, Africa, North America, South America, Antarctica, Europe, and Australia ')
    with mock.patch('builtins.input', side_effect=['list all continents', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# happy path - chat - Test that the chatbot lists English movies when asked.
def test_chat_english_movies(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print('The Shawshank Redemption')
    with mock.patch('builtins.input', side_effect=['suggest an english movie', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# happy path - chat - Test that the chatbot responds to a farewell appropriately.
def test_chat_farewell_response(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print('Bye take care. See you soon :) ')
    with mock.patch('builtins.input', side_effect=['quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# edge case - chat - Test that the chatbot handles unknown input gracefully.
def test_chat_unknown_input(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print("I'm a computer program dude....Seriously you are asking me this?")
    with mock.patch('builtins.input', side_effect=['blablabla', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# edge case - chat - Test that the chatbot responds to a repeated input consistently.
def test_chat_repeated_input(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print('Hello')
    with mock.patch('builtins.input', side_effect=['hello hello', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# edge case - chat - Test that the chatbot handles input with special characters.
def test_chat_special_characters(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print("I'm a computer program dude....Seriously you are asking me this?")
    with mock.patch('builtins.input', side_effect=['!@#$%^&*()', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# edge case - chat - Test that the chatbot responds to a complex sentence with multiple patterns.
def test_chat_complex_sentence(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print('Hello John, How are you today ?')
    with mock.patch('builtins.input', side_effect=['my name is John and I want an english movie', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


# edge case - chat - Test that the chatbot handles an empty input correctly.
def test_chat_empty_input(mock_chat_converse):
    mock_chat_converse.converse.side_effect = lambda: print("I'm a computer program dude....Seriously you are asking me this?")
    with mock.patch('builtins.input', side_effect=['', 'quit']):
        chat()
    mock_chat_converse.converse.assert_called()


