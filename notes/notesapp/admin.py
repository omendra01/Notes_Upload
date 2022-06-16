from django.contrib import admin
from .models import *


@admin.register(Home_notes)
class Home_NotesAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Subjectby_notes)
class subjectby_NotesAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Download_pdf)
class Download_pdfAdmin(admin.ModelAdmin):
    list_display = ['title', 'pdf']
    list_filter = ['title']

    def get_queryset(self, request):
        qs = super(Download_pdfAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
