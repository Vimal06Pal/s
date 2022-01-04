from django.urls import path
from .views import *
from hyperlink_app import views

urlpatterns = [
    path('', views.index    ),
    path('snippets',SnippetsListView.as_view(),name = "snippet-list"),
    path('snippet-detail',SnippetsDetailView.as_view(),name = "snippet-detail"),


]