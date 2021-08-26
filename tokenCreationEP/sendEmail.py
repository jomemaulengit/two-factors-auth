import logging
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from smtplib import SMTPRecipientsRefused as emailError

logger = logging.getLogger()


def Mail(mail, content):
    try:
        email = EmailMultiAlternatives(
            str(content),
            f'este es tu clave de autenticacion: {content}',
            settings.EMAIL_HOST_USER,
            [mail],
        )
        email.send()
        return True
    except emailError as e:
        return False
    except Exception as e:
        logger.error(type(e))
        return False
