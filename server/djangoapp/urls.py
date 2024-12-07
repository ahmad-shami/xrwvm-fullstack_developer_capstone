# Uncomment the imports before you add the code
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views
from django.contrib import admin



app_name = 'djangoapp'
urlpatterns = [
    
    # path for login
    path('login/', view=TemplateView.as_view(template_name="index.html")),
    path(route='login', view=views.login_user, name='login'),
    #path('logout/', view=TemplateView.as_view(template_name="Home.html")),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    path(route='add_review', view=views.add_review, name='add_review'),
    path(route='register', view=views.registration, name='register'),
    
    

    

    
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

    
