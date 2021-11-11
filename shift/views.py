from django.db.models import query
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.shortcuts import render

from .models import Shift
from .forms import ShiftUpdateForm


class ShiftListView(ListView):
    template_name = 'shift/shift_list.html'
    queryset = Shift.objects.all()
    ordering = ['-report_name']


class ShiftListUpdateableView(ListView):
    template_name = 'shift/shift_list_updatable.html'
    queryset = Shift.objects.all()
    ordering = ['-report_name']


class ShiftEditView(UpdateView):
    template_name = 'shift/shift_update_view.html'
    form_class = ShiftUpdateForm
    queryset = Shift.objects.all()
    success_url = reverse_lazy('shift_list_admin')


class ShiftDeleteView(DeleteView):
    model = Shift
    template_name = 'shift/shift_delete.html'
    success_url = reverse_lazy('shift_list_admin')
