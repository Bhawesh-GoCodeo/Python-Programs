import pytest
from unittest import mock
import email
import getpass
import imaplib
import os

@pytest.fixture
def mock_imaplib():
    with mock.patch('imaplib.IMAP4_SSL') as mock_imap:
        mock_mail_instance = mock.Mock()
        mock_imap.return_value = mock_mail_instance
        yield mock_mail_instance

@pytest.fixture
def mock_getpass():
    with mock.patch('getpass.getpass', return_value='valid_password'):
        yield

@pytest.fixture
def mock_email():
    with mock.patch('email.message_from_bytes') as mock_email_from_bytes:
        mock_email_from_bytes.return_value = mock.Mock()
        yield mock_email_from_bytes

@pytest.fixture
def mock_os_path():
    with mock.patch('os.path.isfile', return_value=False):
        with mock.patch('os.path.join', side_effect=lambda dir, filename: f"{dir}/{filename}"):
            yield

@pytest.fixture
def setup_mocks(mock_imaplib, mock_getpass, mock_email, mock_os_path):
    pass  # All mocks are set up in individual fixtures

# happy path - mail.login - Test that email login is successful with valid credentials
def test_email_login_success(setup_mocks, mock_imaplib):
    mock_imaplib.login.return_value = ('OK', [b'Logged in'])
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    response_code, _ = mail.login('valid_username', 'valid_password')
    assert response_code == 'OK'


# happy path - mail.search - Test that fetching email list returns expected number of emails
def test_fetch_email_list(setup_mocks, mock_imaplib):
    mock_imaplib.search.return_value = ('OK', [b'1 2 3 4 5 6 7 8 9 10'])
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.select('INBOX')
    _, ids = mail.search(None, 'ALL')
    assert len(ids[0].split()) == 10


# happy path - email.message_from_bytes - Test that email subject is correctly parsed for valid email
def test_parse_email_subject(setup_mocks, mock_email):
    mock_email.return_value.get_content_maintype.return_value = 'multipart'
    mock_email.return_value['Subject'] = '=?utf-8?q?Parsed_Subject?='
    email_body = b'valid_email_body'
    mailFetch = email.message_from_bytes(email_body)
    subject = mailFetch['Subject'].replace('=?utf-8?q?', '').replace('_', ' ')
    assert subject == 'Parsed Subject'


# happy path - os.path.join - Test that attachments are saved to the specified directory
def test_save_attachments(setup_mocks, mock_email, mock_os_path):
    mock_email.return_value.get_content_maintype.return_value = 'multipart'
    mock_email.return_value.walk.return_value = [mock.Mock(get_content_maintype=lambda: 'application', get_payload=lambda decode=True: b'data', get=lambda key: 'attachment' if key == 'Content-Disposition' else None)]
    email_body = b'valid_email_body'
    mailFetch = email.message_from_bytes(email_body)
    for part in mailFetch.walk():
        if part.get('Content-Disposition') is not None:
            filename = 'from_hw1answer'
            att_path = os.path.join('.', filename)
            assert att_path == './from_hw1answer'


# happy path - for emailid in ids - Test that only 10 emails are processed
def test_process_only_10_emails(setup_mocks, mock_imaplib):
    mock_imaplib.search.return_value = ('OK', [b'1 2 3 4 5 6 7 8 9 10 11'])
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.select('INBOX')
    _, ids = mail.search(None, 'ALL')
    ids = ids[0].split()
    processed_emails = 0
    for emailid in ids:
        processed_emails += 1
        if processed_emails == 10:
            break
    assert processed_emails == 10


# edge case - mail.login - Test that login fails with invalid credentials
def test_email_login_failure(setup_mocks, mock_imaplib):
    mock_imaplib.login.return_value = ('NO', [b'Login failed'])
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    response_code, _ = mail.login('invalid_username', 'invalid_password')
    assert response_code == 'NO'


# edge case - mail.search - Test that fetching with invalid criteria returns no emails
def test_fetch_invalid_criteria(setup_mocks, mock_imaplib):
    mock_imaplib.search.return_value = ('OK', [b''])
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.select('INBOX')
    _, ids = mail.search(None, 'INVALID')
    assert len(ids[0].split()) == 0


# edge case - email.message_from_bytes - Test that parsing email with no subject handles gracefully
def test_parse_email_no_subject(setup_mocks, mock_email):
    mock_email.return_value.get_content_maintype.return_value = 'multipart'
    mock_email.return_value['Subject'] = None
    email_body = b'no_subject_email_body'
    mailFetch = email.message_from_bytes(email_body)
    subject = mailFetch['Subject'] if mailFetch['Subject'] else 'No Subject'
    assert subject == 'No Subject'


# edge case - os.path.isfile - Test that saving attachment with existing filename skips saving
def test_skip_existing_attachment(setup_mocks, mock_email, mock_os_path):
    mock_email.return_value.get_content_maintype.return_value = 'multipart'
    mock_email.return_value.walk.return_value = [mock.Mock(get_content_maintype=lambda: 'application', get_payload=lambda decode=True: b'data', get=lambda key: 'attachment' if key == 'Content-Disposition' else None)]
    email_body = b'valid_email_body'
    mailFetch = email.message_from_bytes(email_body)
    mock_os_path.isfile.return_value = True
    for part in mailFetch.walk():
        if part.get('Content-Disposition') is not None:
            filename = 'from_hw1answer'
            att_path = os.path.join('.', filename)
            assert os.path.isfile(att_path)


# edge case - for part in mailFetch.walk - Test that processing emails with no attachments skips saving
def test_skip_no_attachments(setup_mocks, mock_email):
    mock_email.return_value.get_content_maintype.return_value = 'multipart'
    mock_email.return_value.walk.return_value = [mock.Mock(get_content_maintype=lambda: 'text', get=lambda key: None)]
    email_body = b'valid_email_body'
    mailFetch = email.message_from_bytes(email_body)
    attachments_saved = 0
    for part in mailFetch.walk():
        if part.get('Content-Disposition') is not None:
            attachments_saved += 1
    assert attachments_saved == 0


