from django.urls import path, include, re_path
from . import views

print("in urls")
urlpatterns=[
    path('', views.index),
    path('authors',views.authors),
    path('add',views.add_book),
    path('authors/add',views.add_author),
    path('books/<num>', views.book_info),
    path('authors/<num>',views.author_info),
    path('join',views.join),
    path('connect',views.connect),
    re_path(r'^.*$', views.catchall)
]
