
from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signinpage , name= 'signin'),
    path('signup/',signuppage , name= 'signup'),
    path('profile/',profile , name= 'profile'),
    path('dashboard/',dashboard , name= 'dashboard'),
    path('logoutt/',logoutt , name= 'logout'),
    path('viewjob/',viewjob , name= 'viewjob'),
    path('applied/',applied , name= 'applied'),
    path('editprofile/',editprofile , name= 'editprofile'),
    path('updateprofile/',updateprofile , name= 'updateprofile'),
    path('addjob/',addjob , name= 'addjob'),
    path('seebasic/',seebasic , name= 'seebasic'),
    path('update/',update , name= 'update'),
    path('changepass/',changepass , name= 'changepass'),


    path('view/<str:myid>',view , name= 'view'),
    path('delete/<str:myid>',delete , name= 'delete'),
    path('edit/<str:myid>',edit , name= 'edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
