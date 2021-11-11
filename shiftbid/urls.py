from django.urls import path
from .views import ShiftbidCreateView, ShiftbidThankyouView
from .views import shiftbidIndexView, create_view

urlpatterns = [
    path('', shiftbidIndexView, name='shiftbid_index'),
    path('shiftbid_create', ShiftbidCreateView.as_view(), name='shiftbid_create'),
    path('shiftbid_thanks', ShiftbidThankyouView.as_view(), name='shiftbid_thanks'),
    # Custom Paths
    path('shiftbid_response/<report_name>',
         create_view, name='shiftbid_response')
]
