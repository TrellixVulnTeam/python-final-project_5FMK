from django.contrib import admin
from src.home.models import Students
from src.home.models import Courses
from src.home.models import Semester
from src.home.models import Update

# Register your models here.
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Semester)
admin.site.register(Update)
