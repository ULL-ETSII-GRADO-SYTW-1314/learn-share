from users.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _
class CourseForm(forms.Form):
	title = forms.RegexField(regex=r'^[\w.@+-]+$',max_length=155)
	description = forms.CharField(max_length=155, widget=forms.Textarea)
	lenguaje = forms.CharField(max_length=155)
	prize = forms.IntegerField(min_value=0, max_value=9999)
	
	
