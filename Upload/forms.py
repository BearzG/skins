from django import forms

class Upload_Skin(forms.Form):
    Author = forms.CharField(max_length = 25)
    Name = forms.CharField(max_length = 20)
    Image = forms.ImageField()