from django.http import HttpResponse
from django.urls import path, include, re_path

from users.views import UserProfileCreateView, ClientCreateView, ClientRetrieveUpdateDeleteView, ClientListView

# Create your views here.

urlpatterns = [
    path('answer/', lambda x: HttpResponse('Ok')),
    path('new_user_profile/', UserProfileCreateView.as_view()),
    path('client/', ClientListView.as_view()),
    path('client/create/', ClientCreateView.as_view()),
    path('client/<slug:username>/', ClientRetrieveUpdateDeleteView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # authorization
]

# http://127.0.0.1:8001/users/auth/token/login - получить токен
