from django.core.mail import send_mail
import uuid

def send_email(email, url):
    if email:
        subject = 'A file has been shared with you.'
        content = 'Download the file here: \n\n {}\n' % url
        sender = 'shaurya.cs16@iitp.ac.in'
        send_mail(subject, content, sender, [email], fail_silently=False)

def generate_random_folder(instance, filename):
    return 'files/{}/{}'.format(str(uuid.uuid4()), filename)
