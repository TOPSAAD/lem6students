from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cours/<int:id>/<str:sub>', views.cours_details, name='cours_details'),
    # path('cours/<str:file>', views.pdf_view, name='pdf_view'),
    path('<str:id>/<str:cte>/<str:sub>', views.pages, name='pages'),
    path('login', views.login, name='login'),
    path('account', views.account, name='account'),
    path('contact', views.contact, name='contact'),
]
