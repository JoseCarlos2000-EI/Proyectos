from django.urls import path
from . import views

urlpatterns=[

    path('',views.portafolio,name="inicio"),
    path('about/',views.about,name="sobre"),
    path('contact/',views.contact,name="contact"),
]