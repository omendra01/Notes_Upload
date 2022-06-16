from django.contrib import admin
from django.urls import path
from notesapp import views

urlpatterns = [
    path('subjectby_details/<int:id>',
         views.subjectby_details, name='subjectby_details'),
    path('histroy_payments/<int:id>',
         views.history_notes_payments, name='histroy_payments'),
    path('download_pdf/<int:id>', views.download_pdf, name='download_pdf'),
    path('payments/',
         views.payments, name='payments'),
    path('', views.notes_template, name='notes_template'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('header/', views.header, name='header'),

]
