from django.http.response import HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from django import forms

import threading

from django.urls import reverse_lazy
from django.urls import reverse

from django.core.mail import send_mail
from django.conf import settings

from shift.models import Shift
from seniority.models import Seniority

from .response_handler import handle_response_submission


urlpatterns = []
report_name = ""


def test_run():
    get_report_name()


def get_report_name():
    report_name_list = []
    report_names_query = list(
        Shift.objects.values_list('report_name').distinct())
    for report_name in report_names_query:
        for report in report_name:
            report_name_list.append(report)

    for data in report_name_list:
        # t = threading.Thread(
        #     target=spawn_child_elements, args=(data,), kwargs={})
        # t.setDaemon(True)
        # t.start()
        spawn_child_elements(data)


def spawn_child_elements(report_name):
    shift_query = Shift.objects.filter(report_name__iexact=report_name)
    seniority_query = Seniority.objects.filter(report_name__iexact=report_name)
    form_query = Shift.objects.filter(report_name__iexact=report_name).exclude(
        agent_email__contains='@email.com')

    create_url(report_name)
    email_function(report_name, seniority_query)


def create_url(report_name):
    urlpatterns.append(path(
        f"shiftbid_response/{report_name}", create_view, name=f"{report_name}-reponse_path"))


class ShiftbidResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.report_name = kwargs.pop('report_name')
        super(ShiftbidResponseForm, self).__init__(*args, **kwargs)
        self.fields["shift_choice"] = forms.ModelMultipleChoiceField(Shift.objects.filter(report_name__iexact=self.report_name).exclude(
            agent_email__contains='@email.com'))

    agent_email = forms.EmailField()


def create_view(request, report_name):
    report_name = report_name
    form = ShiftbidResponseForm(report_name=report_name)
    if request.method == "POST":
        form = (ShiftbidResponseForm(report_name=report_name), request.POST)[1]
        print(form)
        report_name = report_name
        email = form['agent_email']
        shift = form['shift_choice']
        print(shift)
        print(email)
        handle_response_submission(report_name, shift, email)
        return HttpResponseRedirect(reverse_lazy('shiftbid_thanks'))

    else:
        return render(request, "shiftbid/shiftbid_response.html", {'form': form, 'report_name': report_name})


def email_function(report_name, seniority_query):
    recipients = query_to_list(seniority_query)
    print(recipients)
    link = f'shiftbid/shiftbid_response/{report_name}'
    message = f"This is the Shiftbid for - {report_name}; Use this link: {link}"
    subject = f"This is the Shiftbid for - {report_name}"

    send_mail(subject=subject, message=message,
              from_email=settings.EMAIL_HOST_USER, recipient_list=recipients)


def query_to_list(query):
    recipients = []
    for i in list(query):
        recipients.append(i.agent_email)
    # print(recipients)
    return ['tanleybench@gmail.com'] if len(recipients) == 0 else recipients
