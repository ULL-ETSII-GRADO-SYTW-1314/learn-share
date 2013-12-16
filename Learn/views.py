from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import ExtendUser
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.validators import *

def ayuda(request):
   return render_to_response('ayuda.html', {'title':'Ayuda', 'user': request.user},context_instance=RequestContext(request) )

def contacto(request):
   return render_to_response('contacto.html', {'title':'Contacto', 'user': request.user},context_instance=RequestContext(request) )

def about(request):
   return render_to_response('about.html', {'title':'Acerca de', 'user': request.user},context_instance=RequestContext(request) )
