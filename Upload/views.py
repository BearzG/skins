from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

from . import forms
from .models import Store_skins
import os

class Main(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': forms.Upload_Skin()
        }
        return render(request, 'upload.html', context)

    def post(self, request, *args, **kwargs):
        form = forms.Upload_Skin(request.POST, request.FILES)
        if (form.is_valid()):
            print(form.cleaned_data)
            Data = {
                "Author": form.cleaned_data.get('Author'),
                "Name": form.cleaned_data.get("Name"),
                "Image": form.cleaned_data.get('Image')
            }
            Obj = Store_skins(Author = Data["Author"], Name = Data["Name"], Image = Data['Image'])
            Obj.save()
            Form_Red = {
                "form": forms.Upload_Skin()
            }
            return render(request, 'upload.html', Form_Red)


def get_skins():
    list_img  = os.listdir('media/Skins')
    Data = {
        "Images": list_img
    }
    return Data

class Show(View):
    def get(self, request, *args, **kwargs):
        #Getting our model objects
        # print('Data model is ', Store_skins.objects.all()[0].Author) -> List with objects for each record in the DB
        context = {
            "Data": Store_skins.objects.all()
        }
        return render(request, 'show.html', context)