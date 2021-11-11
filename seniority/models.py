from django.db import models
from datetime import datetime


class Seniority(models.Model):
    report_name = models.CharField(max_length=100)
    datetime_created = models.CharField(max_length=100)
    agent_name = models.CharField(max_length=100)
    agent_email = models.EmailField()
    seniority_number = models.PositiveIntegerField()

    def __str__(self):
        return self.agent_name
