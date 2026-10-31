from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),
    path('users/', include('users.urls')),
]