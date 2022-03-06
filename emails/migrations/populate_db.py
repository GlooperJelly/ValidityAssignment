from django.db import migrations
from emails.email_parser import parse_file
from email import utils


FILENAME = "emails/sampleEmails.tar.gz"

def create_initial_data(apps, schema_editor):
    emails = parse_file(FILENAME)
    Email = apps.get_model('emails', 'Email')
    for message in emails:
        message_datetime = utils.parsedate_to_datetime( message.get('Date') )
        email_db = Email( to_field=message.get('To'), from_field=message.get('From'), date=message_datetime, subject=message.get('subject'), message_id=message.get('Message-ID'))
        email_db.save()

class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0001_alter_email_subject'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
