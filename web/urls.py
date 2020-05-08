from django.urls import path, include
from . import views

urlpatterns = [
    path('submit/expense/', views.submit_expense , name='submit_expense'),
    path('submit/income/', views.submit_income , name='submit_income'),
    path('hello/', views.HelloView.as_view(), name='hello'),
]
