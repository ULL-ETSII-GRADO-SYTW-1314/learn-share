from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class ExtendUser(models.Model):
    """ La clase se usa para almacenar las
  caracteristicas de los usuarios extendidos """
    user = models.ForeignKey(User, unique=True)
    puntuacion = models.IntegerField()
    alias = models.CharField(max_length=100)
    followers = models.ManyToManyField(User, related_name='seguidor')
    def content_file_name(self, filename):
        return '/'.join([self.email, 'img', filename])
    photo = models.ImageField(upload_to=content_file_name, default='/static/img/default/defaultProfile.png', blank=True)
    

    





class ExtendUserAdmin(admin.ModelAdmin):
    list_display = ["user"]
    list_filter = ["alias"]



admin.site.register(ExtendUser, ExtendUserAdmin)

