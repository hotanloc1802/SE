from django.urls import path
from .views import login_view, signup_view

urlpatterns = [
    path('login/', login_view, name='login'),  # Đăng nhập
    path('signup/', signup_view, name='signup'),  # Đăng ký
]
