import pytest
from unittest import mock
import smtplib
from Scripts.P07_ScriptToSendMail import server  # Adjust the import based on your actual code structure

@pytest.fixture
def smtp_mock():
    with mock.patch('smtplib.SMTP') as mock_smtp:
        instance = mock_smtp.return_value
        instance.ehlo.return_value = None
        instance.starttls.return_value = None
        instance.login.return_value = None
        instance.sendmail.return_value = {}
        yield instance

def test_send_email_success(smtp_mock):
    smtp_mock.sendmail.return_value = {}
    # Your test code here

def test_smtp_connection(smtp_mock):
    smtp_mock.connect.return_value = (250, 'OK')
    # Your test code here

def test_start_tls(smtp_mock):
    smtp_mock.starttls.return_value = None
    # Your test code here

def test_login_success(smtp_mock):
    smtp_mock.login.return_value = None
    # Your test code here

def test_ehlo_command(smtp_mock):
    smtp_mock.ehlo.return_value = (250, 'OK')
    # Your test code here

# happy path - server.sendmail - Test that email is sent successfully with valid credentials and message.
def test_send_email_success(smtp_mock):
    smtp_mock.sendmail.return_value = {}
    result = smtp_mock.sendmail('valid_sender@example.com', 'valid_receiver@example.com', 'Mail sent through Python!')
    assert result == {}


# happy path - server.connect - Test that server connects to SMTP server with correct host and port.
def test_smtp_connection(smtp_mock):
    smtp_mock.connect.return_value = (250, 'OK')
    response = smtp_mock.connect('smtp.gmail.com', 587)
    assert response == (250, 'OK')


# happy path - server.starttls - Test that server starts TLS successfully after EHLO command.
def test_start_tls(smtp_mock):
    smtp_mock.ehlo.return_value = (250, 'OK')
    smtp_mock.starttls.return_value = None
    smtp_mock.ehlo()
    result = smtp_mock.starttls()
    assert result is None


# happy path - server.login - Test that server logs in with correct username and password.
def test_login_success(smtp_mock):
    smtp_mock.login.return_value = None
    result = smtp_mock.login('valid_username', 'valid_password')
    assert result is None


# happy path - server.ehlo - Test that EHLO command is sent successfully to the server.
def test_ehlo_command(smtp_mock):
    smtp_mock.ehlo.return_value = (250, 'OK')
    response = smtp_mock.ehlo()
    assert response == (250, 'OK')


# edge case - server.sendmail - Test that email sending fails with invalid sender email address.
def test_send_email_invalid_sender(smtp_mock):
    smtp_mock.sendmail.side_effect = smtplib.SMTPException('Invalid sender address')
    with pytest.raises(smtplib.SMTPException, match='Invalid sender address'):
        smtp_mock.sendmail('invalid_sender', 'valid_receiver@example.com', 'Mail sent through Python!')


# edge case - server.sendmail - Test that email sending fails with invalid receiver email address.
def test_send_email_invalid_receiver(smtp_mock):
    smtp_mock.sendmail.side_effect = smtplib.SMTPException('Invalid receiver address')
    with pytest.raises(smtplib.SMTPException, match='Invalid receiver address'):
        smtp_mock.sendmail('valid_sender@example.com', 'invalid_receiver', 'Mail sent through Python!')


# edge case - server.login - Test that login fails with incorrect password.
def test_login_invalid_password(smtp_mock):
    smtp_mock.login.side_effect = smtplib.SMTPAuthenticationError(535, 'Authentication failed')
    with pytest.raises(smtplib.SMTPAuthenticationError, match='Authentication failed'):
        smtp_mock.login('valid_username', 'invalid_password')


# edge case - server.connect - Test that connection fails with incorrect SMTP server address.
def test_smtp_invalid_host(smtp_mock):
    smtp_mock.connect.side_effect = smtplib.SMTPConnectError(421, 'Connection failed')
    with pytest.raises(smtplib.SMTPConnectError, match='Connection failed'):
        smtp_mock.connect('invalid.smtp.com', 587)


# edge case - server.starttls - Test that TLS start fails if EHLO command is not acknowledged.
def test_start_tls_without_ehlo(smtp_mock):
    smtp_mock.ehlo.return_value = None
    smtp_mock.starttls.side_effect = smtplib.SMTPException('EHLO not acknowledged')
    smtp_mock.ehlo()
    with pytest.raises(smtplib.SMTPException, match='EHLO not acknowledged'):
        smtp_mock.starttls()


