from celery import Task


class SendEmailTask(Task):
    name = 'send_email'

    def run(self):
        return self.send_email()

    def send_email(self):
        print('**sending email')
        return
