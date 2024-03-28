from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .utils import get_mongodb
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote
from bson.objectid import ObjectId


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_page})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            # Зберігаємо автора
            form.save()
            # Перенаправляємо користувача на інший URL
            return redirect(to='quotes:root')
        else:
            # Якщо форма недійсна, повертаємо HTML-шаблон з помилкою та формою
            return render(request, 'quotes/author.html', {'form': form})
    # Якщо запит GET , повертаємо порожній інстанс форми
    return render(request, 'quotes/author.html', {'form': AuthorForm()})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            # Отримуємо об'єкт автора з форми
            author = form.cleaned_data['author']
            # Створюємо новий цитату з автором
            quote = Quote(quote=form.cleaned_data['quote'], author=author)
            # Зберігаємо цитату
            quote.save()
            # Перенаправляємо користувача на інший URL
            return redirect('quotes:root')
        else:
            # Якщо форма недійсна, повертаємо HTML-шаблон з помилкою та формою
            return render(request, 'quotes/quote.html', {'form': form})

    # Якщо запит GET , повертаємо порожній інстанс форми
    return render(request, 'quotes/quote.html', {'form': QuoteForm()})


def biography(request, author_id):
    # Convert the author_id from a string to an ObjectId
    author_id = ObjectId(author_id)

    # Get the MongoDB database connection
    db = get_mongodb()

    # Retrieve the author document from the authors collection
    author = db.authors.find_one({'_id': author_id})

    # If the author is not found, return a 404 error
    if not author:
        raise Http404("Author does not exist")

    # Prepare the context
    context = {
        'author': author,
        # Add other variables you want to pass to the template
    }

    return render(request, 'quotes/biography.html', context)

