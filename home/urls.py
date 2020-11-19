from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("",views.index, name= 'index'),
    path("index",views.index, name= 'index'),
    path("about",views.about, name= 'about'),
    path("services",views.services, name= 'services'),
    path("contech",views.contech, name= 'contech'),
    path("salon",views.salon, name= 'salon'),
    
    
]
