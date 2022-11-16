from .views import EmployeeListView
from django.urls import path
urlpatterns = [
    path("",EmployeeListView.as_view(), name='home'),
]