from django.urls import path
from . import views

app_name = 'modal'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name = 'signup'),
    path('login/', views.CustomLoginView.as_view(), name = 'login'),
    path('update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('user/', views.user.as_view(), name='user')
]
