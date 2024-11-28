from django.contrib import admin
from django.urls import path
from .views import ReactView, QuoteDetailView

urlpatterns = [
    path('quote/', ReactView.as_view()),
    path('quote/<int:pk>', QuoteDetailView.as_view())
]
