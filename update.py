from app import db, models
from bs4 import BeautifulSoup
import urllib, os, re


for file in os.listdir('Books'):
    if file.endswith('.html'):
        category = file.split('-')[-1].split('.')[0]
        print 'Category: ', category
        fullpath = os.getcwd() + '/Books/' + file
        soup = BeautifulSoup(open(fullpath))
        authors = soup.find_all(attrs = {'class': 'authorName'})
        author_names = [author.text.strip() for author in authors]
        print 'Author list: ', author_names
        existing_authors = [author.name for author in models.Author.query.all()]
        existing_categories = [ctg.name for ctg in models.Category.query.all()]
        existing_titles = [book.title for book in models.Book.query.all()]
        for author_name in author_names:
            if author_name not in existing_authors:
                new_author = models.Author(name = author_name)
                db.session.add(new_author)
                print 'New author added: ', author_name
        if category not in existing_categories:
            print type(category)
            new_category = models.Category(name = category)
            db.session.add(new_category)
            print 'New category added: ', category
        db.session.commit()
        title = soup.find(id = 'bookTitle').text.strip()
        title = ' '.join(title.split())
        print 'Title: ', title
        description = soup.find(id = 'description').find_all('span')[1].text.strip()
        print 'Description: ', description[:40]
        rating = float(soup.find(attrs = {'class': 'average'}).text)
        print 'Rating: ', rating
        try: isbn = soup.find(attrs = {'itemprop': 'isbn'}).text.strip()
        except AttributeError: isbn = ''
        print 'ISBN: ', isbn
        image_src = soup.find(id = 'coverImage')['src']
        print 'Source: ', image_src
        # Naming the file and storing at the right location...
        image_name = title.lower().replace(' ', '_') + '.jpg'
        print 'Image name: ', image_name
        full_path = os.getcwd() + '/Media/' + image_name
        urllib.urlretrieve(image_src, full_path)
        # ...saved file in /Media folder
        print 'Path: ', full_path
        if title not in existing_titles:
            cat_id = models.Category.query.filter_by(name = category).first().id
            new_book = models.Book(
                                    title = title,
                                    description = description,
                                    rating = rating,
                                    isbn = isbn,
                                    category_id = cat_id,
                                    picture = full_path
                                  )
            db.session.add(new_book)
            db.session.commit()
        book_id = models.Book.query.filter_by(title = title).first().id
        for author_name in author_names:
            new_book_author = models.BookAuthor(
                                                book_id = book_id,
                                                author_id = models.Author.query.filter_by(name = author_name).first().id
                                                )
            db.session.add(new_book_author)
        db.session.commit()
