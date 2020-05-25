from django.db import models


def object_exists(model: models.Model, limitations=None, **kwargs) -> bool:
    """
        This util function check if an object with given details
        exists in database or not

    :param model:
    :param limitations:
    :param kwargs:
    :return:
    """
    if limitations:
        kwargs = {k: v for k, v in kwargs if k in limitations}
        if not kwargs:
            return False

    available_field_names = [field.name for field in model._meta.fields]
    for field in kwargs:
        if field not in available_field_names:
            return False
    return model.objects.filter(**kwargs).exists()


def send_email(subject, template_name, context, from_email='Art-Online',
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


def generate_n_digit_random_number(digits_count):
    from secrets import choice
    lower_bound = 10 ** (digits_count - 1)
    upper_bound = 10 ** digits_count

    return choice(range(lower_bound, upper_bound))
