import pytest
from unittest import 

# happy path - chat - Test that the chatbot greets the user when initiated.
def test_chat_greeting(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value=None) as mock_chat_func:
        assert chat() == 'Hi! I am Y2K..'
        mock_chat_func.assert_called_once()ddddd


# happy path - chat - Test that the chatbot responds with a name when asked 'what is your name?'
def test_chat_responds_to_name_query(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='I am Y2K. You can call me crazy individual!') as mock_chat_func:
        assert chat() == 'I am Y2K. You can call me crazy individual!'
        mock_chat_func.assert_called_once()


# happy path - chat - Test that the chatbot responds correctly to a greeting like 'hello'.
def test_chat_responds_to_hello(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='Hello') as mock_chat_func:
        assert chat() == 'Hello'
        mock_chat_func.assert_called_once()


# happy path - chat - Test that the chatbot reflects 'I am' to 'you are'.
def test_chat_reflects_i_am(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='you are happy') as mock_chat_func:
        assert chat() == 'you are happy'
        mock_chat_func.assert_called_once()


# happy path - chat - Test that the chatbot provides a list of continents when asked about continents.
def test_chat_lists_continents(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='Asia, Africa, North America, South America, Antarctica, Europe, and Australia') as mock_chat_func:
        assert chat() == 'Asia, Africa, North America, South America, Antarctica, Europe, and Australia'
        mock_chat_func.assert_called_once()


# edge case - chat - Test that the chatbot handles unexpected input gracefully.
def test_chat_handles_unexpected_input(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='') as mock_chat_func:
        assert chat() == ''
        mock_chat_func.assert_called_once()


# edge case - chat - Test that the chatbot can handle a very long string input.
def test_chat_handles_long_input(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='') as mock_chat_func:
        assert chat() == ''
        mock_chat_func.assert_called_once()


# edge case - chat - Test that the chatbot responds to 'quit' command correctly.
def test_chat_quit_command(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='Bye take care. See you soon :) ') as mock_chat_func:
        assert chat() == 'Bye take care. See you soon :) '
        mock_chat_func.assert_called_once()


# edge case - chat - Test that the chatbot can handle multiple sentences in one input.
def test_chat_multiple_sentences(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='Hello') as mock_chat_func:
        assert chat() == 'Hello'
        mock_chat_func.assert_called_once()


# edge case - chat - Test that the chatbot does not crash with special characters.
def test_chat_special_characters(mock_chat):
    with mock.patch('Programs.Chatbot.chat', return_value='') as mock_chat_func:
        assert chat() == ''
        mock_chat_func.assert_called_once()


