
from django.urls import path

from . import views

app_name='movies'
urlpatterns = [
    path('', views.all_movies_view, name='search'),
    path('<int:my_id>/', views.details_view, name='details')
]
