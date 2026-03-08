from django.contrib import admin
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),           # homepage
    path('register/', views.register, name='register'),   # register page

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)