from django.urls import path
from .views import profile_view,bookSearch_view,showBook_view,addBook_view,deleteBook
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', profile_view, name="profile"),
    path('search/',bookSearch_view,name="bookSearch"),
    path('showBook/',showBook_view,name="showBook"),
    path('addBook/',addBook_view,name="addBook"),
    path('deleteBook/<int:id>/',deleteBook,name="deleteBook"),
]