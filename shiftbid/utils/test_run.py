from django.http.response import HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from django import forms

import threading

from django.urls.base import reverse_lazy

from shift.models import Shift
from seniority.models import Seniority
# from shiftbid.forms import ShiftbidResponseForm

from .response_handler import handle_response_submission


urlpatterns = []
report_name = ""


def test_run():
    # print('Ran on click')
    get_report_name()


def get_report_name():
    report_name_list = []
    report_names_query = list(
        Shift.objects.values_list('report_name').distinct())
    for report_name in report_names_query:
        for report in report_name:
            report_name_list.append(report)

    # print(report_name_list)

    for data in report_name_list:
        t = threading.Thread(
            target=spawn_child_elements, args=(data,), kwargs={})
        t.setDaemon(True)
        t.start()


def spawn_child_elements(report_name):
    shift_query = Shift.objects.filter(report_name__iexact=report_name)
    seniority_query = Seniority.objects.filter(report_name__iexact=report_name)
    form_query = Shift.objects.filter(report_name__iexact=report_name).exclude(
        agent_email__contains='@email.com')

    create_url(report_name)


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
