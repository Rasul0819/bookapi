from django.urls import path
from .views import *


urlpatterns = [
    path('',BooksApiView.as_view()),

    path('<int:pk>/',BookDetailView.as_view()),
    path('<int:pk>/update/',BookUpdateView.as_view()),
    path('<int:pk>/delete/',BookDeleteView.as_view()),
    path('create/',BookCreateApiView.as_view()),

]