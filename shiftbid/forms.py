from django import forms
import datetime

import pandas as pd

from .utils.file_upload_handlers import seniority_upload, shift_upload
from .utils.response_handler import handle_response_submission
from shift.models import Shift


class ShiftbidCreateForm(forms.Form):
    report_name = forms.CharField(max_length=100)
    datetime_created = forms.DateTimeField(initial=datetime.datetime.today())
    seniority_file = forms.FileField()
    shift_file = forms.FileField()

    def handle_seniority_file(self):
        file_name = self.cleaned_data['seniority_file']
        report_name = self.cleaned_data["report_name"]
        datetime_created = self.cleaned_data["datetime_created"]

        seniority_upload(file_name, report_name, datetime_created)

    def handle_shift_file(self):
        file_name = self.cleaned_data['shift_file']
        report_name = self.cleaned_data["report_name"]
        datetime_created = self.cleaned_data["datetime_created"]

        shift_upload(file_name, report_name, datetime_created)


class ShiftbidResponseForm(forms.Form):
    agent_email = forms.EmailField()
    shift_choice = forms.ModelMultipleChoiceField(
        queryset=Shift.objects.exclude(agent_email__contains='@email.com'))

    def handle_response(self):
        report_name = ''
        shift = ''
        for data in self.cleaned_data["shift_choice"]:
            report_name = data.report_name
            shift = data.shift
        #print(f'Report Name: {report_name}; Shift: {shift}')
        email = self.cleaned_data['agent_email']
        handle_response_submission(report_name, shift, email)
