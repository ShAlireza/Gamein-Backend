from django.conf import settings


def send_email(subject, template_name, context, from_email=settings.EMAIL,
               receipts=None, file_path=None, file_name=None,
               file_content=None, mime_type=None):
    from django.core.mail.message import EmailMultiAlternatives
    from django.core.mail import DEFAULT_ATTACHMENT_MIME_TYPE
    from django.template.loader import render_to_string
    from django.utils.html import strip_tags

    if receipts is None:
        receipts = []

    email_message_html = render_to_string(template_name, context=context)
    email_message_plaintext = strip_tags(email_message_html)

    email = EmailMultiAlternatives(
        subject=subject,
        body=email_message_plaintext,
        from_email=from_email,
        to=receipts
    )
    email.attach_alternative(email_message_html, 'text/html')
    if file_path:
        email.attach_file(file_path, mimetype=DEFAULT_ATTACHMENT_MIME_TYPE)
    if file_content:
        email.attach(filename=file_name, content=file_content,
                     mimetype=mime_type)

    email.send()
