from django.db import models

class Email(models.Model):
    to_field = models.CharField(max_length=200)
    from_field = models.CharField(max_length=200)
    date = models.DateTimeField()
    subject = models.CharField(max_length=500)
    message_id = models.CharField(max_length=200)

    def __str__(self):
        return self.message_id