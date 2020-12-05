"""reauthorProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import mainApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainApp.views.main, name='main'),
    path('accounts/', include('allauth.urls')),
    path('login/', mainApp.views.login, name="login"),
    path('kakao/', mainApp.views.kakao, name="kakao"),
    path('oauth/', mainApp.views.oauth, name="oauth"),
    path('signup/', mainApp.views.signup, name="signup"),
    path('upload1/',mainApp.views.upload1, name='upload1'),
    path('upload2/',mainApp.views.upload2, name='upload2'),
    path('upload3/',mainApp.views.upload3, name='upload3'),
    path('author1/',mainApp.views.author1, name='author1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

