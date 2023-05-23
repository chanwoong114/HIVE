from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage),
    path('delete/', views.delete),
    path('<int:user_pk>/follow/', views.follow),
    path('username/<str:username>/', views.userpage),

]
