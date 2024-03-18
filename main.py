import requests
from bs4 import BeautifulSoup
import json


def get_quotes_and_tags(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    tags = soup.find_all('div', class_='tags')
    return quotes, tags


def get_author_info(base_url, author_url):
    response = requests.get(base_url + author_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    author_name = soup.find('h3', class_='author-title').text.strip()
    author_birthdate = soup.find('span', class_='author-born-date').text.strip()
    author_birthplace = soup.find('span', class_='author-born-location').text.strip()
    author_description = soup.find('div', class_='author-description').text.strip()
    return {
        'fullname': author_name,
        'born_date': author_birthdate,
        'born_location': author_birthplace,
        'description': author_description
    }


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def scrape_site(base_url):
    page = 1
    quotes_data = []
    authors_data = []

    while True:
        url = f'{base_url}/page/{page}'
        print(f'Scraping page {page}...')
        quotes, tags = get_quotes_and_tags(url)

        if not quotes:
            break

        for quote, tag in zip(quotes, tags):
            quote_text = quote.find('span', class_='text').text.strip()
            tagsforquotes = tag.find_all('a', class_='tag')
            tag2 = []
            for tagforquote in tagsforquotes:
                tag2.append(tagforquote.text)
            author_url = quote.find('small', class_='author').find_next_sibling('a')['href']
            author_info = get_author_info(base_url, author_url)
            authors_data.append(author_info)
            quotes_data.append({'text': quote_text, 'author': author_info['fullname'], 'tags': tag2})

        page += 1

    save_to_json(quotes_data, 'quotes.json')
    save_to_json(authors_data, 'authors.json')


if __name__ == '__main__':
    scrape_site('http://quotes.toscrape.com')
