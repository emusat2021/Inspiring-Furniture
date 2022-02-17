from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.order_history_list, name='order_history_list'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/rating/delete/<int:product_id>/', views.delete_rating, name='delete_rating'),
    path('reviews/rating/edit/<int:product_id>/', views.edit_rating, name='edit_rating'),
    path('reviews/review/delete/<int:product_id>/', views.delete_review, name='delete_review'),
    path('reviews/review/edit/<int:product_id>/', views.edit_review, name='edit_review'),
]
