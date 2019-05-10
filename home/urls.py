from django.urls import path
from home import views
app_name='home'
urlpatterns=[
path('',views.index,name='home'),
    path('genre/<str:slug>/',views.genre_detail,name='genre_detail'),
    path('author/<str:slug>/',views.author_detail,name='author_detail'),
    path('authors/',views.author_list,name='author_list'),
    path('books/',views.books_list,name='book_list'),
    path('book/<str:slug>/',views.book_detail,name='book_detail'),
    path('book_rules/',views.book_rules,name='book_rules'),
    path('teshnick_rules/',views.teshin_rules,name='teshin_rules'),
    path('read_rules/',views.read_rules,name='read_rules'),
    path('library_best/',views.library_best,name='library_best'),
    path('about_us/',views.about_us,name='about_us'),
    path('contact_us/',views.ContactCreate.as_view(),name='contact_us'),
    path('contact_create_succes',views.contact_create_succes,name='contact_create_succes')

]