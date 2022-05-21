from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="base"),
	path('about/', views.about, name="about"),
	path('blog/', views.blog, name="blog"),
	path('case_details', views.case_details, name="case_details"),
	path('case_study/', views.case_study, name="case_study"),
	path('contact/', views.contact, name="contact"),
	path('submitted_contact/', views.submitted_contact, name="submitted_contact"),
	path('elements/', views.elements, name="elements"),
	path('services', views.services, name="services"),
	path('single_blog/', views.single_blog, name="single_blog"),

]