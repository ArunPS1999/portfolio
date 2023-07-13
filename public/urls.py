from django.urls import path
from .import views


app_name = "public"

urlpatterns = [
    path("",views.userhome,name="userhome"),
    
]