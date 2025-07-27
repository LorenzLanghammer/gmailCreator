import zendriver as zd
from zendriver.cdp import fetch
import asyncio
import imaplib
import email

EMAIL = "juliamghrt28@gmail.com"
APP_PASSWORD = "rsno dxsw kjjp fula".replace(" ", "") 


mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)
mail.select("INBOX")
status, message_numbers = mail.search(None, 'FROM', '"instagram"')

if status == 'OK':
    for num in message_numbers[0].split():
        status, msg_data = mail.fetch(num, '(RFC822)')
        if status == 'OK':
            msg = email.message_from_bytes(msg_data[0][1])
            subject = msg['subject']
            code = subject.split()[0]
            print(f"Instagram code: {code}")
            break

mail.logout()


#status, data = mail.search(None, "ALL")
#print("Number of emails:", len(data[0].split()))





