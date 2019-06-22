from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home',
         views.create_widget, name=''),
    path('<int:pk>/delete/',
         views.WidgetDelete.as_view(), name='WidgetDelete'),
]
