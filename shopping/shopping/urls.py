"""
URL configuration for shopping project.

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
from django.urls import path, include

# to include media files 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mainapp.urls')),
    path('cart/',include('cart.urls')),
    path('',include('orders.urls')),
    path('',include('payments.urls')),
    path('accounts/',include('authentication.urls')),
    path('accounts/',include('django.contrib.auth.urls')) # includes others auth urls
]

# the folowing line allows us to use given media path diuring develomplment
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# THE above code genertaes unique urls for each media file in the provided media_root loaction 