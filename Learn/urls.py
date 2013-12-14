from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Learn.views.home', name='home'),
    # url(r'^Learn/', include('Learn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^login/$', 'users.views.login_user', name='Login'),
    url(r'^home/$', 'users.views.home', name='home'),   
    url(r'^logout/$', 'users.views.logout_user', name='Logout'),
    url(r'^perfil/(?P<user_id>\d+)/$', 'users.views.perfil'),
    #urls de cursos
    url(r'^curso/(?P<course_id>\d+)/$', 'cursos.views.curso_info', name='info_curso'),
    url(r'^curso/new/$','cursos.views.curso_add', name='info_curso'),
    url(r'^curso/list/$','cursos.views.curso_list', name='info_curso'),
    url(r'^curso/inscribe/(?P<course_id>\d+)/$','cursos.views.inscribe', name='info_curso'),
    url(r'^curso/add_lec/(?P<course_id>\d+)/$','cursos.views.curso_add_leccion', name='info_curso'),
    url(r'^curso/edit/(?P<course_id>\d+)/$','cursos.views.curso_edit', name='info_curso'),
    url(r'^curso/view/(?P<course_id>\d+)/$', 'users.views.view_courses_lessons', name='info_curso'),
    #urls tareas
    url(r'^curso/view/(?P<course_id>\d+)/(?P<lesson_id>\d+)/$','cursos.views.new_task', name='info_curso'),

    url(r'^mytasks/$','cursos.views.my_tasks', name='revisiones'),   
    url(r'^mytasks/review/(?P<task_id>\d+)/$','cursos.views.task_reviews', name='info_curso'),

    
    url(r'^registro/', 'users.views.register', name='registro'),

    url(r'^seguir/(?P<user_id>\d+)/$', 'users.views.follow'),
    url(r'^unfollow/(?P<user_id>\d+)/$', 'users.views.unfollow'),
    url(r'^ayuda/', 'Learn.views.ayuda', name='ayuda'),
    url(r'^contacto/', 'Learn.views.contacto', name='contacto'),
    url(r'^mycourses/', 'cursos.views.my_courses', name='mycourses'),
    url(r'^reviews/$', 'cursos.views.task_list', name='revisiones'),
    url(r'^reviews/(?P<task_id>\d+)/$', 'cursos.views.review_new', name='info_curso'),
)
