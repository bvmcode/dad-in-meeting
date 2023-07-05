from django.db import models


class Meeting(models.Model):
    meeting = models.BooleanField(default=False)
