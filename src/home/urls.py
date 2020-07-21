from django.urls import path, include
from src.home.views import student
from src.home.views import profile
from src.home.views import courses
from src.home.views import edit
from src.home.views import selection
from src.home.views import modify
from src.home.views import select
from src.home.views import drop
from src.home.views import remove
from src.home.views import logout
from src.home.views import point
from src.home.views import calculate
from src.home.views import tuition
from src.home.views import payment

app_name = 'home'

urlpatterns = [
    path('student', student, name="student"),
    path('profile', profile, name="profile"),
    path('courses', courses, name="courses"),
    path('Edit', edit, name="edit"),
    path('selection', selection, name="selection"),
    path('modify', modify, name="modify"),
    path('select', select, name="select"),
    path('Drop', drop, name="Drop"),
    path('remove', remove, name="remove"),
    path('Logout', logout, name="Logout"),
    path('point', point, name="point"),
    path('calculate', calculate, name="calculate"),
    path('tuition', tuition, name="tuition"),
    path('payment', payment, name="payment"),
]
