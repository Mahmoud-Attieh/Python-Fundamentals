from django.urls import path, include

urlpatterns = [
    path('', include('book_app.urls') ),
]
