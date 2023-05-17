from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('random/', views.random_list),
    path('recommend_list/', views.recommend_list)
]
