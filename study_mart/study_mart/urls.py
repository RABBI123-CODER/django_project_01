"""
URL configuration for study_mart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

'''''
# from machine_learning import views as vi
from machine_learning.views import machine_learning
from machine_learning.views import deep_learning
from machine_learning.views import about_us1
# from Blogs import views as blo
from Blogs.views import blog1
# from Data_analysis import views as da
from Data_analysis.views import data_ana
# from Deep_learning import views as deep
from Deep_learning.views import deep_lear
# from About_US import views as ab
from About_US.views import about
'''''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/', include('machine_learning.urls')),
    path('about/', include('About_US.urls')),
    path('blog/', include('Blogs.urls')),
    path('deep/', include('Deep_learning.urls')),
    path('data/', include('Data_analysis.urls')),


]
