from django.contrib import admin
from django.urls import path, include, reverse

urlpatterns = [
    path('', include('users.urls')),
    path('books/', include('books.urls')),
    path('admin/', admin.site.urls),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='books/', permanent=True)),
]