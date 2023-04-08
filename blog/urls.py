
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .models import Post, Like

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.renderPosts, name="posts"),
    path('<int:post_id>', views.post_detail, name="post_detail"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name="register"),
    path('post/<int:post_id>/like/', views.post_like, name='post_like'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
