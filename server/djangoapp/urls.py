# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from . import views

app_name = 'djangoapp'
urlpatterns = [
    
    # path for login
    path(route='login', view=views.login_user, name='login'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),
    path(route='add_review', view=views.add_review, name='add_review'),
    path('login/', view=TemplateView.as_view(template_name="index.html")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

    
