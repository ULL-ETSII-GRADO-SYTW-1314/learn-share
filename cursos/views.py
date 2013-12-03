from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import ExtendUser
from cursos.models import *
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from forms import *
from django.contrib.auth import authenticate, login
from django.core.validators import *
import datetime


def curso_info(request, course_id):
	course = Curso.objects.get(id=course_id)
	return render_to_response('curso_info.html', {'title':'Curso', 'curso':course}, context_instance=RequestContext(request) )
	
def curso_add(request):
	state = " Se dispone a realizar un nuevo registro.Recuerde que todos los campos son obligatorios"
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:	
		if request.method == 'POST':
			form = CourseForm(request.POST)
			if form.is_valid():
				
				title = form.cleaned_data['title']
				description = form.cleaned_data['description']
				precio = form.cleaned_data['prize']
				leng= form.cleaned_data['lenguaje']
				course=Curso.objects.create(titulo = title,	descripcion = description,lenguaje=leng,creator = request.user,
				creado = datetime.datetime.now())           
				course.save()
				return redirect('/curso/edit/'+str(course.id))
			else:
					
				  state=" Error en el registro"
				  return render_to_response('curso_new.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))
		else:
			form =  CourseForm()
		return render_to_response('curso_new.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))
def curso_add_leccion(request, course_id):
	state = " Se dispone a realizar un nuevo registro.Recuerde que todos los campos son obligatorios"
	if not request.user.is_authenticated():
		return redirect('/login/?next=%s' % request.path)
	else:	
		if request.method == 'POST':
			form = LeccionForm(request.POST)
			if form.is_valid():
				course = Curso.objects.get(id=course_id)
				title = form.cleaned_data['title']
				description = form.cleaned_data['description']
				lec = Leccion.objects.create(titulo = title, descripcion = description, curso=course)           
				lec.save()
				return redirect('/home'+str(course.id))
			else:
					
				  state=" Error en el registro"
				  return render_to_response('curso_lecc.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))
		else:
			form =  LeccionForm()
		return render_to_response('curso_lecc.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))

def curso_edit(request, course_id):
	#lista con las lecciones del curso
	course = Curso.objects.get(id=course_id)
	lecciones=Leccion.objects.filter(curso = course)
	return render_to_response('curso_edit.html', {'title':'Curso', 'curso':course,'lecciones': lecciones}, context_instance=RequestContext(request) )
	
	
	
def curso_list(request):
	cursos_ = Curso.objects.all()
	return render_to_response('curso_list.html', {'title':'Curso', 'cursos':cursos_}, context_instance=RequestContext(request) )
		
def inscribe(request, course_id):
	course = Curso.objects.get(id=course_id)		
	inscripcion=Realiza.objects.create(usuario=request.user,curso=course, comenzado=datetime.datetime.now(), finalizado=datetime.datetime.now(), nota=0)
	inscripcion.save()
	return 	redirect('/home')
