from django.urls import path
from .views import world, login, signup

urlpatterns = [
    path('world/', world),
    path('login/', login),
    path('signup/', signup),
    
]

