import datetime

from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,CreateView,FormView,
                                    ListView,DetailView)
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse

from . import forms
from . import models

# Create your views here.

class FileList(ListView):
    model = models.UserFile
    template_name = 'file_storage/all.html'
    context_object_name = 'file_list'

class FileDetail(DetailView):
    model = models.UserFile

class CreateFile(CreateView):
    template_name = 'file_storage/home.html'
    form_class = forms.UploadForm

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.created_at = datetime.datetime.utcnow()
        self.object.expiration_date = (self.object.created_at +
                                        datetime.timedelta(days=self.object.estimation))
        self.object.countdown = abs((self.object.expiration_date-
                                    self.object.created_at).days)
        self.object.save()
        return HttpResponse('<a href="all/' + self.object.slug + '">Link</a>')
