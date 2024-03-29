from users.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
class CourseForm(forms.Form):
	title = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': 'Titulo del Curso', 'class':"form-control"}),regex=r'^[\w.@+-]+$',max_length=155)
	description = forms.CharField(max_length=155, widget=forms.Textarea(attrs={'placeholder': 'Descripcion', 'class':"form-control"}))
	lenguaje = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Lenguaje', 'class':"form-control"}),max_length=155)
	prize = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Puntos necesarios', 'class':"form-control"}),min_value=0, max_value=9999)
	
class LeccionForm(forms.Form):
	title = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': 'Titulo del Curso', 'class':"form-control"}),regex=r'^[\w.@+-]+$',max_length=155)
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descripcion', 'class':"form-control"}))
class TaskForm(forms.Form):
	body = forms.CharField(widget=forms.Textarea)
class ReviewForm(forms.Form):
	body = forms.CharField(widget=forms.Textarea)
	nota = forms.ChoiceField(choices=[(x,x) for x in range(0, 10)], required=True)

