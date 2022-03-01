
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('expenseTracker.expenses.urls')),
    path('profile/', include('expenseTracker.profiles.urls')),
]
