from . import views
from django.urls import path


app_name = "quotes"

urlpatterns = [
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("author", views.add_author, name="author"),
    path("quote", views.add_quote, name="quote"),
    path("biography/<str:author_id>", views.biography, name="biography")
]
