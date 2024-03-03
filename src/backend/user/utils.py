from django.conf import settings
from django.core.mail import EmailMessage
from typing import List, Dict

class EmailUtils:
    
    @staticmethod
    def send_email(recipient_list: List[str], subject:str, message:str, attachements: List[Dict] = None) -> None:
        '''
        attachements = {
                        "filename":"<str>"
                        "content": <byte>,
                        "content_type": "text/plain"
                    }
        '''

        email_from = settings.EMAIL_HOST_USER
        
        mail = EmailMessage(subject, message, email_from, recipient_list)
        if attachements:
            for files in attachements:
                mail.attach(files.filename, files.content, files.content_type)
        mail.send()
        
if __name__ == '__main__':

    EmailUtils.send_email(['richardfranklin41@gmail.com'], 'Test Email', 'This is the message for the said test email')