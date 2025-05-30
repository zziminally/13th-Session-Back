"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from community.views import List, detail_post, detail_question

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List, name="main"),
    path('post/<int:pk>/', detail_post, name="detail_post"),
    #path('', List_question, name="list_question"),
    path('question/<int:pk>/', detail_question, name="detail_question"),
]
