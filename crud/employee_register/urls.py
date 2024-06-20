from django.urls import path

from .views import employee_list, employee_form, employee_delete

app_name = 'employee_register'

urlpatterns = [
    path('', employee_list, name='employee_list'),
    path('create/', employee_form, name='create'),
    path('update/<int:id>/', employee_form, name='update'),
    path('delete/<int:id>/', employee_delete, name='delete'),
]
