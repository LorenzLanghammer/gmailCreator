from abc import ABC, abstractmethod
import json
import requests
import random
import string
import zendriver as zd
import asyncio
from country_values import *
from smsactivate.api import SMSActivateAPI
from helper import *
import imaplib
import email


class EmailInterface(ABC):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @abstractmethod
    def getCode(self):
        pass

class ImapInterface(EmailInterface):
    def getCode(self):
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(self.email, self.password)
        mail.select("INBOX")
        status, message_numbers = mail.search(None, 'FROM', '"instagram"')

        if status == 'OK':
            for num in message_numbers[0].split():
                status, msg_data = mail.fetch(num, '(RFC822)')
                if status == 'OK':
                    msg = email.message_from_bytes(msg_data[0][1])#
                    subject = msg['subject']
                    code = subject.split()[0]
                    print(f"Instagram code: {code}")
                    return code
                    
        mail.logout()



