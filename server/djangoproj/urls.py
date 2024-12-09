"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
#from django.urls import path, include
from django.contrib import admin
from djangoapp import views   
from django.views.generic import TemplateView
from django.views.static import serve




urlpatterns = [
    
    path('login/', view=TemplateView.as_view(template_name="index.html")),
    path(route='login', view=views.login_user, name='login'),
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    path('login/', view=TemplateView.as_view(template_name="index.html")),
    path(route='login', view=views.login_user, name='login'),
    path('dealers/', TemplateView.as_view(template_name="index.html")),
    path('dealer/', TemplateView.as_view(template_name="index.html")),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_details'),
    path('register/', TemplateView.as_view(template_name="index.html")),
    path('dealer/<int:dealer_id>',TemplateView.as_view(template_name="index.html")),
    path('manifest.json', TemplateView.as_view(template_name="manifest.json", content_type="application/json")),
    #re_path(r'^register/$', serve, kwargs={'path': 'index.html', 'document_root': settings.STATIC_ROOT}),
    #path('signup/', views.register_view, name='register')
    




    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


