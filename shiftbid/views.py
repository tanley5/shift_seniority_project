from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import threading

from .forms import ShiftbidCreateForm, ShiftbidResponseForm
from .utils.test_run import test_run
from .utils.test_run import create_view


def shiftbidIndexView(request):
    template_name = 'shiftbid/shiftbid_index.html'

    if request.method == 'POST' and 'run_script' in request.POST:
        t = threading.Thread(target=test_run, args=(), kwargs={})
        t.setDaemon(True)
        t.start()
        return HttpResponseRedirect(reverse_lazy('shift_list'))

    return render(request, template_name)


class ShiftbidCreateView(FormView):
    template_name = 'shiftbid/shiftbid_create.html'
    form_class = ShiftbidCreateForm
    success_url = reverse_lazy('shift_list_admin')

    def form_valid(self, form):
        # print(form.cleaned_data['seniority_file'])
        form.handle_seniority_file()
        form.handle_shift_file()
        return super().form_valid(form)


# class CreateShiftbidResponse(FormView):
#     template_name = 'shiftbid/shiftbid_response.html'
#     form_class = ShiftbidResponseForm
#     success_url = reverse_lazy('shiftbid_thanks')

#     def form_valid(self, form):
#         form.handle_response()
#         return super().form_valid(form)


class ShiftbidThankyouView(TemplateView):
    template_name = 'shiftbid/shiftbid_response_thanks.html'


create_view
