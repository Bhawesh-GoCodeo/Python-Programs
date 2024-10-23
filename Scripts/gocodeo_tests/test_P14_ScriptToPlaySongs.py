import pytest
from unittest import mock
import pyttsx3
import speech_recognition as sr
import os
import datetime
import random
from Scripts.P14_ScriptToPlaySongs import speak, takedata, wishme

@pytest.fixture
def mock_dependencies():
    # Mocking pyttsx3
    mock_engine = mock.Mock()
    mock_engine.getProperty.return_value = [mock.Mock(id='male_voice'), mock.Mock(id='female_voice')]
    mock_engine.say = mock.Mock()
    mock_engine.runAndWait = mock.Mock()
    
    with mock.patch('pyttsx3.init', return_value=mock_engine):
        yield

    # Mocking speech_recognition
    mock_recognizer = mock.Mock()
    mock_recognizer_instance = mock.Mock()
    mock_recognizer.return_value = mock_recognizer_instance
    
    with mock.patch('speech_recognition.Recognizer', mock_recognizer):
        yield

    # Mocking os functions
    with mock.patch('os.listdir', return_value=['song1.mp3', 'song2.mp3']):
        with mock.patch('os.startfile') as mock_startfile:
            yield

    # Mocking datetime
    with mock.patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value.hour = 9  # Set current hour for testing
        yield

    # Mocking random
    with mock.patch('random.randrange', return_value=0):
        yield

# happy path - speak - Test that speak function calls engine.say and engine.runAndWait with the correct audio
def test_speak_function_calls_engine_methods(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import speak
    mock_engine = mock.patch('pyttsx3.init').start()
    speak('Hello')
    mock_engine.say.assert_called_with('Hello')
    mock_engine.runAndWait.assert_called()


# happy path - takedata - Test that takedata function recognizes speech and returns the correct query
def test_takedata_function_recognizes_speech(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import takedata
    mock_recognizer_instance = mock.patch('speech_recognition.Recognizer').start().return_value
    mock_recognizer_instance.recognize_google.return_value = 'play music'
    query = takedata()
    assert query == 'play music'


# happy path - wishme - Test that wishme function speaks the correct greeting in the morning
def test_wishme_morning_greeting(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import wishme
    mock_engine = mock.patch('pyttsx3.init').start()
    mock_datetime = mock.patch('datetime.datetime').start()
    mock_datetime.now.return_value.hour = 9
    wishme()
    mock_engine.say.assert_any_call('good morning')


# happy path - wishme - Test that wishme function speaks the correct greeting in the afternoon
def test_wishme_afternoon_greeting(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import wishme
    mock_engine = mock.patch('pyttsx3.init').start()
    mock_datetime = mock.patch('datetime.datetime').start()
    mock_datetime.now.return_value.hour = 15
    wishme()
    mock_engine.say.assert_any_call('good afternoon')


# happy path - wishme - Test that wishme function speaks the correct greeting in the evening
def test_wishme_evening_greeting(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import wishme
    mock_engine = mock.patch('pyttsx3.init').start()
    mock_datetime = mock.patch('datetime.datetime').start()
    mock_datetime.now.return_value.hour = 19
    wishme()
    mock_engine.say.assert_any_call('good evening')


# edge case - speak - Test that speak function handles empty audio input gracefully
def test_speak_with_empty_audio(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import speak
    mock_engine = mock.patch('pyttsx3.init').start()
    speak('')
    mock_engine.say.assert_called_with('')
    mock_engine.runAndWait.assert_called()


# edge case - takedata - Test that takedata function returns 'None' when no speech is recognized
def test_takedata_no_speech_recognized(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import takedata
    mock_recognizer_instance = mock.patch('speech_recognition.Recognizer').start().return_value
    mock_recognizer_instance.recognize_google.side_effect = sr.UnknownValueError
    query = takedata()
    assert query == 'None'


# edge case - wishme - Test that wishme function handles boundary time at 12 PM correctly
def test_wishme_boundary_noon_greeting(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import wishme
    mock_engine = mock.patch('pyttsx3.init').start()
    mock_datetime = mock.patch('datetime.datetime').start()
    mock_datetime.now.return_value.hour = 12
    wishme()
    mock_engine.say.assert_any_call('good afternoon')


# edge case - wishme - Test that wishme function handles boundary time at 6 PM correctly
def test_wishme_boundary_evening_greeting(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import wishme
    mock_engine = mock.patch('pyttsx3.init').start()
    mock_datetime = mock.patch('datetime.datetime').start()
    mock_datetime.now.return_value.hour = 18
    wishme()
    mock_engine.say.assert_any_call('good evening')


# edge case - takedata - Test that takedata function handles unexpected exceptions gracefully
def test_takedata_handles_exceptions(mock_dependencies):
    from Scripts.P14_ScriptToPlaySongs import takedata
    mock_recognizer_instance = mock.patch('speech_recognition.Recognizer').start().return_value
    mock_recognizer_instance.recognize_google.side_effect = Exception('error')
    query = takedata()
    assert query == 'None'


