from django.contrib import admin
from django.urls import path, include  # Не забудьте импортировать include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Включаем маршруты из приложения myapp
]
