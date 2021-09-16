from django.contrib import admin
from .models import *
# Register your models here.
from .views import minsert

admin.site.register(Profile)
admin.site.register(DBList)
admin.site.register(Data)
admin.site.register(links)
admin.site.register(ratings)
admin.site.register(movies)
#admin.site.register(minsert)
admin.site.register(tags)