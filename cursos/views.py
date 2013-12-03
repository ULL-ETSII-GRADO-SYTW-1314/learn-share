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
				course=Curso.objects.create(titulo = title,	descripcion = description,lenguaje=leng,creator = request.user,creado = datetime.datetime.now())           
				course.save()
				return redirect('/home')
			else:
					
				  state=" Error en el registro"
				  return render_to_response('curso_new.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))
		else:
			form =  CourseForm()
		return render_to_response('curso_new.html', {'title':'Registro', 'formulario': form,'state':state}, context_instance=RequestContext(request))

	
	
	
