
from django.urls import path
from . import views

urlpatterns = [
    path('mll/', views.machine_learning),
    path('de/', views.deep_learning),
    path('ab/', views.about_us1),

]
