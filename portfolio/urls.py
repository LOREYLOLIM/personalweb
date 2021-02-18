from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'index'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('blog/', views.blog, name = 'blog'),
    path('testimonial/', views.testimonial, name = 'testimonial'),
    path('services/', views.services, name = 'services'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('FAQS/', views.FAQs, name = 'FAQs'),

]
