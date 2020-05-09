from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('all_user_profile/', views.AllUserProfile.as_view(), name='AllUserProfile'),
    path('all_post/', views.allPost.as_view(), name='allPost'),
    path('post_byTitle/', views.post_byTitle.as_view(), name='postByTitle'),
    path('register/', views.RegisterUser.as_view(), name='RegisterUser'),
]
