"""syschoque URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from p1 import urls as p1_urls

urlpatterns = [
    #path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('', admin.site.urls),
    path('p1/', include(p1_urls)),
    path('tinymce/', include('tinymce.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'SYSCHOQUE'
admin.site.site_title = 'SYSCHOQUE'
admin.site.index_title = 'Administração do Sistema'