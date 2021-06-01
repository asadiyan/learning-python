from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
# Create your views here.


def index(request):
    # give us access to all of object inside the table
    book_list = Book.objects.all()
    context = {
        "book_list": book_list,
    }
    return render(request, "myapp/index.html", context)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "myapp/detail.html", {"book": book})


def add_book(request):

    # a post request comes from add_booh page by pressing submit button
    # when a post request comes we check it
    if request.method == "POST":
        # we save the name typed bye user in the name feild
        # we should becareful about what ever we use in "" inside get function
        # it should be same as in the add_book we gave as name
        name = request.POST.get("name",)
        desc = request.POST.get("desc",)
        price = request.POST.get("price",)
        book_image = request.FILES["book_image"]

        # now we have saved them and we should save them in database
        # we create a object of our class which we have in models
        book = Book(name=name, desc=desc, price=price, book_image=book_image)
        book.save()

    # we make this view render a template with return render()
    # request and temmplate path to this view
    return render(request, "myapp/add_book.html")
    # after this we need url pattern
    # now we go to myapp/urls.py


def edit(request, id):
    book = Book.objects.get(id=id)
    # request.POST means it will be method of POST
    # request.FILES is for haveing image
    # instance is nothing but book which we want to edit and the book is coming from top we have book=Book.object
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        # returning homepage
        return redirect("/")
    # we passs book and form as context to edit.html
    return render(request, "myapp/edit.html", {"form": form, "book": book})


def delete(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect("/")
    return render(request, "myapp/delete.html")
