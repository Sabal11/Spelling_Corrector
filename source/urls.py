from django.contrib import admin
from django.urls import path, include
from source import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('aboutus', views.about),
    path('contactus', views.contact),
    path('contactus', views.click),
    path('', include('Test.urls')),

]
