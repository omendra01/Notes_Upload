from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages


def index(request):
    obj = Home_notes.objects.all()
    return render(request, 'index.html', {'obj': obj})


def subjectby_details(request, id):
    result = Subjectby_notes.objects.filter(home_notes=id)
    return render(request, 'notes_template/gs.html', {'result': result})


def history_notes_payments(request, id):
    result = Subjectby_notes.objects.get(id=id)
    obj = Subjectby_notes.objects.filter(id=result.id)
    return render(request, 'notes_template/history_payments.html', {'obj': obj})


def download_pdf(request, id):
    result = Download_pdf.objects.filter(subjectby_notes=id)
    return render(request, 'notes_template/pdf_detail.html', {'result': result})


def payments(request):
    return render(request, 'notes_template/payments.html')


# ++++++++++++++++second template code start+++++++++++++++++++++++++++++

def notes_template(request):
    obj = Home_notes.objects.all()
    return render(request, 'notes_template/index2.html', {'obj': obj})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(name=name, email=email,
                       subject=subject, message=message)
        data.save()
        messages.info(
            request, 'Message Send SuccessFully...')
    return render(request, 'notes_template/contact.html')


def about(request):
    return render(request, 'notes_template/about.html')


def header(request):
    return render(request, 'notes_template/header.html')
