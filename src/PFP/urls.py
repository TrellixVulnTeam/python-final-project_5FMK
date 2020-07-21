from django.contrib import admin
from django.urls import path, include
from src.PFP.views import homepage
from src.PFP.views import news
from src.PFP.views import about

app_name = 'PFP'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', homepage, name="Login"),
    path('News', news, name="News"),
    path('about', about, name="about")
]
