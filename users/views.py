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
from forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.core.validators import *



#Registramos el usuario
def register(request):
    state = " Se dispone a realizar un nuevo registro.Recuerde que todos los campos son obligatorios"

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
			
            name_user = form.cleaned_data['username']
            email_user = form.cleaned_data['email']
            pass_user = form.cleaned_data['password1']
            create_user = User.objects.create_user(username= name_user, email= email_user,password=pass_user)           
            create_user.save()
            aliases="@"+name_user
            extend=ExtendUser(user=create_user,alias=aliases)
            extend.save()


            return redirect('/login')
        else:
				
			  state=" Error en el registro"
			  return render_to_response('nuevo.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))
    else:
        form =  RegistrationForm()
    return render_to_response('nuevo.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        state = "Password o usuario incorrecto."
        user = authenticate(username=username, password=password)
      
			
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                return redirect('/home')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
			try:
				userna=User.objects.get(email=username)
				user = authenticate(username=userna.username, password=password)
			except:
				state = "Password o usuario incorrecto."
				return render_to_response('login.html',{'title':'Login', 'state':state, 'username': username}, context_instance=RequestContext(request))

			if user is None:	
				state = "Password o usuario incorrecto."
			if user.is_active:
				login(request, user)
				
				return redirect('/home')
			else:
				return redirect('/home')
				state = "Your account is not active, please contact the site admin."

    return render_to_response('login.html',{'title':'Login', 'state':state, 'username': username}, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return redirect('/home')
