from rest_framework import serializers
from emails.models import Email

class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ['to_field', 'from_field', 'date', 'subject', 'message_id']