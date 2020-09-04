from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /user/5/
    path('<int:dog_id>/', views.detail, name = 'detail'),
    path('login/', views.login, name = 'login'),
]
