from django.urls import path
from .views import ShiftListView, ShiftListUpdateableView, ShiftEditView, ShiftDeleteView

urlpatterns = [
    path('shift_list', ShiftListView.as_view(), name='shift_list'),
    path('shift_list_admin', ShiftListUpdateableView.as_view(),
         name='shift_list_admin'),
    path('shift_update/<int:pk>', ShiftEditView.as_view(), name='shift_update'),
    path('shift_delete/<int:pk>', ShiftDeleteView.as_view(), name='shift_delete'),
]
