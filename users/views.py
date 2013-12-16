from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import ExtendUser
from cursos.models import *
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.core.validators import *

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage

from users.forms import ContactoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404




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

def home(request):
   if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
   else:
	   
	
	   User_ = ExtendUser.objects.all()
	   Users=[]
	   usuario=ExtendUser.objects.get(user = request.user)
	   ##Bloque de followers
	   User__=usuario.followers.all()
	   for u in (User_):
		   if (u!=usuario):
			   Users.append(u)
	   followers=[] 
	   for u in (User__):
		   if (u!=request.user):
			   followers.append(ExtendUser.objects.get(user=u))
	   ##Bloque de cursos usuario
	   Curso_=Realiza.objects.filter(usuario = request.user)
	   cursos=[]
	   for c in (Curso_):
		   cursos.append(Curso.objects.get(id=c.curso.id))
	   return render_to_response('home.html', {'title':'Home', 'Extendido':User_,'User': request.user,'Users': Users,'seguidores': followers, 'cursos': cursos}, context_instance=RequestContext(request) )

def view_courses_lessons(request,course_id):
	course = Curso.objects.get(id=course_id)
	lecciones=Leccion.objects.filter(curso = course)
	return render_to_response('list_lessons.html', {'title':'Curso', 'Curso':course,'lecciones': lecciones, 'User': request.user}, context_instance=RequestContext(request) )




def logout_user(request):
	logout(request)
	return redirect('/home')

def follow(request, user_id):
        if not request.user.is_authenticated():
                return redirect('/login/?next=%s' % request.path)
        else:
                
                usuario=ExtendUser.objects.get(user = request.user)
                usuario.followers.add(User.objects.get(id = user_id))
                return redirect('/home/')
def unfollow(request, user_id):
        if not request.user.is_authenticated():
                return redirect('/login/?next=%s' % request.path)
        else:
                
                usuario=ExtendUser.objects.get(user = request.user)
                usuario.followers.remove(User.objects.get(id = user_id))
                return redirect('/home/')

def perfil(request, user_id):
        if not request.user.is_authenticated():
            return redirect('/login/?next=%s' % request.path)
        else:
            usuario=User.objects.get(id=user_id)
            usuario_=ExtendUser.objects.get(user=usuario)

            User__=usuario_.followers.all()
            followers=[]
            for u in (User__):
                    followers.append(ExtendUser.objects.get(user=u))

            #Cursos del usuario que esta logueado
            Curso_login=Realiza.objects.filter(usuario = request.user)
            cursos_login=[]
            for c_login in (Curso_login):
                cursos_login.append(Curso.objects.get(id=c_login.curso.id))
            
            #Cursos del perfil que estamos usando.        
            Curso_=Realiza.objects.filter(usuario = usuario)
            cursos=[]
            for c in (Curso_):
                cursos.append(Curso.objects.get(id=c.curso.id))

                
            return render_to_response('perfil.html', {'title':'Perfil', 'user': usuario, 'User': usuario_, 'follower':followers, 'cursos': cursos, 'cursos_login': cursos_login})

def update(request):
        error='Recuerde, las password deben ser iguales.'
        usuario = request.user
        extendido = ExtendUser.objects.get(user=usuario)
        alias = extendido.alias[1:len(extendido.alias)]
        if request.method=='POST':
                usuario.username=request.POST.get('username')

                if request.POST.get('password'):

                        if request.POST.get('password') == request.POST.get('rpassword'):
                                usuario.set_password(request.POST.get('password'))
                                error = "El password ha sido actualizado correctamente."
                        else:
                                error = "Los password no coinciden."
                try:
                        if validate_email(request.POST.get('email')):
                                usuario.email=request.POST.get('email')
                except:

                        if error == 'Recuerde que los password deben coincidir.':

                                error = "El e-mail es incorrecto."
                        else:
                                error = error + " El e-mail es incorrecto."

                usuario.save()
                if extendido.alias!=request.POST.get('alias'):
                        extendido.alias='@'+request.POST.get('alias')

                if request.POST.get('photo'):
                        extendido.photo=request.POST.get('photo')
                if "borrar" in request.POST.keys():
                        extendido.photo='/static/img/default/defaultProfile.png'

                extendido.save()


        return render_to_response('profile.html', {'title':'Informacion personal', 'User': usuario, 'Extend':extendido, 'MERROR':error, 'Alias':alias}, context_instance=RequestContext(request))

def deluser(request):
        if not request.user.is_authenticated():
                return redirect('/login/?next=%s' % request.path)
        else:
                E=ExtendUser.objects.get(user = request.user)
                E.delete()
                U=request.user
                logout(request)
                U.delete()
                return redirect('/login/?next=%s' % request.path)

def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)        

        #subject = 'Mensaje de contacto Learn&Share'
        #message = formulario.cleaned_data['mensaje'] + "\n"
        #message += 'Responder a: ' + formulario.cleaned_data['correo']

        subject = 'Mensaje de contacto Learn&Share'
        message = request.POST.get('mensaje', '') + "\n"
        message += 'Responder a: ' + request.POST.get('correo', '')


        if subject and message:
            try:
                send_mail(subject,message,'learnyshare@gmail.com',['learnyshare@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('/home/')
            
        else:
            return HttpResponse('Invalid header found')
    else:
        formulario =  ContactoForm()
    return render_to_response('contactoform.html', {'title':'Informacion personal', 'formulario': formulario}, context_instance=RequestContext(request))