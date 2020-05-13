from django.urls import path
from . import views

app_name = 'reviews'

ulrpatterns = [
    path('<int:review_pk>/', views.detail, name='detail'),
    path('create/<int:movie_pk>/', views.create_review, name='create_review'),
    path('update/<int:review_pk>/', views.update_review, name='update_review'),
    path('delete/<int:review_pk>/', views.delete_review, name='delete_review'),
    path('comment/create/<int:review_pk>/', views.create_comment, name='create_comment'),
    path('comment/update/<int:comment_pk>/', views.update_comment, name='update_comment'),
    path('comment/delete/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
]