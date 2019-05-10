from django.shortcuts import render,get_object_or_404
from books.models import Genre,Author,Books
from django.db.models import Q
from images.models import Images
# Create your views here.
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):

    query=request.GET.get('q')
    found=True

    if query:
        query=query.title()

        books=Books.objects.filter(Q(name__icontains=query)|Q(author__name__icontains=query)|Q(genre__name__icontains=query))[:12]

    else:
        books=Books.objects.all()[:12]
    images=Images.objects.all()
    genres=Genre.objects.all()[:10]
    authors=Author.objects.all()[:10]
    return render(request,'books/index.html',locals())
def genre_detail(request,slug):

    genres=Genre.objects.all()[:10]
    authors=Author.objects.all()[:10]
    genre=get_object_or_404(Genre,slug=slug)
    object_list=Books.objects.filter(genre=genre)[:12]
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request,'books/genre_detail.html',locals())
def author_detail(request,slug):
    genres = Genre.objects.all()[:10]
    authors = Author.objects.all()[:10]
    author = get_object_or_404(Author, slug=slug)
    object_list = Books.objects.filter(author=author)[:12]
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request,'books/author_detail.html',locals())
def books_list(request):

    query=request.GET.get('q')
    found=True

    if query:
        query=query.title()

        object_list=Books.objects.filter(Q(name__icontains=query)|Q(author__name__icontains=query)|Q(genre__name__icontains=query))[:12]

    else:
        object_list=Books.objects.all()


    genres = Genre.objects.all()[:10]
    authors = Author.objects.all()[:10]
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'books/books_list.html',locals())


from comments_book.forms import CommentForm
from django.contrib import auth
def book_detail(request,slug):


    genres = Genre.objects.all()[:10]
    authors = Author.objects.all()[:10]
    book=get_object_or_404(Books,slug=slug)
    comments = book.comments.filter(book=book).filter(active=True)
    new_comment = None
    user = auth.get_user(request)
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.author = user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'books/book_detail.html',locals())


def book_rules(request):

    genres=Genre.objects.all()[:10]
    authors=Author.objects.all()[:10]

    return render(request,'books/book_rules.html',locals())

def teshin_rules(request):

    genres=Genre.objects.all()[:10]
    authors=Author.objects.all()[:10]

    return render(request,'books/teshin_rules.html',locals())

def read_rules(request):

    genres=Genre.objects.all()[:10]
    authors=Author.objects.all()[:10]

    return render(request,'books/read_rules.html',locals())

def library_best(request):

    genres=Genre.objects.all()[:10]
    authors=Author.objects.all()[:10]

    return render(request,'books/library_best.html',locals())

def about_us(request):

    genres=Genre.objects.all()[:10]
    authors=Author.objects.all()[:10]

    return render(request,'books/about_us.html',locals())
from contact_us.models import Contact,Contact_form
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class ContactCreate(CreateView):
    template_name = 'books/contact-us.html'
    form_class = Contact_form
    success_url = reverse_lazy('home:contact_create_succes')
def contact_create_succes(request):
    return render(request,'books/contact_create_succes.html')







def author_list(request):
    genres = Genre.objects.all()[:10]
    authors = Author.objects.all()[:10]
    object_list = Author.objects.all()
    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request,'books/author_list.html',locals())







