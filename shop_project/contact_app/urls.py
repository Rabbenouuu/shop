from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
  path('contact_form/', views.contact_form, name='contact_form'),
  path('contact_form/contact_succes/', views.contact_succes, name='contact_succes'),
  ]