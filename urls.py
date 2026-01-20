from django.urls import path
from .views import PartSearchView, AnalyticsView

urlpatterns = [
    path('', PartSearchView.as_view(), name='search'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
]