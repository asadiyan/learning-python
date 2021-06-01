from django import forms
from .models import Book

# this name means(we have a model with name of Book) we want to create a form for this model
# and it inherits from = forms.ModelForm


class BookForm(forms.ModelForm):
    class Meta:
        # we can not go direcly to declare model and feils we should first declare meta class then
        # model and feilds should be inside the meta class
        # meta is a class that holds class information
        # class Meta:
        model = Book
        fields = ["name", "desc", "price", "book_image"]
