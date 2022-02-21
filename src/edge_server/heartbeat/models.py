from django.db import models


class HeartBeat(models.Model):
    service = models.CharField(max_length=30)
    last_seen = models.DateTimeField(auto_now=True)
