from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    #path("query_result/<dict:params>/", views.query_result, name = "query_result")
]
