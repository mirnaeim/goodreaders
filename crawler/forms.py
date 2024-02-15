from django import forms


class SearchForm(forms.Form):
    book_title = forms.CharField(label="Book title", max_length=100)
