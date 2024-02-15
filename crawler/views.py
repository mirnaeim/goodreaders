from django.shortcuts import render
from .forms import SearchForm
from .models import Book
import requests
from bs4 import BeautifulSoup
# from django.conf import settings
from goodreaders.settings import page_count, crawl_tab


def crawl(value, tab, page):
    base_url = "https://www.goodreads.com/search?page={page}&q={value}&search%5Bsource%5D=goodreads&" \
               "search_type={tab}&tab={tab}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/111.0.0.0 Safari/537.36'}

    tab = tab
    for p in range(1, page + 1):
        url = base_url.format(tab=tab, page=p, value=value)
        response = requests.get(url, headers=headers)
        soap = BeautifulSoup(response.content, 'html.parser')
        table = soap.find('table', 'tableList')
        items = table.find_all('tr')

        for b in items:
            try:
                title = b.find('a', 'bookTitle').get_text().strip()
                link = "https://www.goodreads.com/" + b.find('a', 'bookTitle')['href']
                author = b.find('a', 'authorName').get_text()
                rating = b.find('span', 'minirating').get_text().split()[0]
                print('Book title: ', title)
                print('Link: ', link)
                print('Author: ', author)
                print('Rate: ', rating)
                Book.objects.create(
                    title=title,
                    link=link,
                    author=author,
                    rating=rating
                )
            except Exception as e:
                print(e)
                continue

def get_title(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            book_title = form.cleaned_data['book_title']
            crawl(book_title, crawl_tab, page_count)

            # redirect to a new URL:
            books = Book.objects.filter(title__contains=book_title)
            context = {'books': books}
            return render(request, 'results.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, "search.html", {"form": form})
