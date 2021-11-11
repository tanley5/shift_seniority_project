from django.db import models


class Shift (models.Model):
    report_name = models.CharField(max_length=100)
    datetime_created = models.CharField(max_length=100)
    shift = models.CharField(max_length=100)
    agent_email = models.EmailField(blank=True)

    def __str__(self):
        return f"Report Name: {self.report_name}; Shift: {self.shift}"
