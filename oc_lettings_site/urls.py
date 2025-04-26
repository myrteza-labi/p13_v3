from django.contrib import admin
from django.urls import path, include
from . import views

handler404 = 'oc_lettings_site.views.custom_404'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls',  namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
]
