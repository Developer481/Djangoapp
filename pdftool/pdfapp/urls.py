from django.urls import path
from pdfapp import views

urlpatterns = [
   
    path('api/scrape/', views.scrape_api),
]