
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.conf.urls.static import static  # type: ignore
from . import views
urlpatterns = [
    path('account',views.show_account,name='account')
    
    
]