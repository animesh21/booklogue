from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150), nullable = False, index = True)
    description = db.Column(db.Text)
    rating = db.Column(db.Float, index = True)
    isbn = db.Column(db.String(15), index = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    picture = db.Column(db.String(50), index = True)
    authors = db.relationship('BookAuthor', backref = 'book', lazy = 'dynamic')

    
    def __repr__(self):
        return self.title
        
        
class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False, unique = True, index = True)
    books = db.relationship('Book', backref = 'category', lazy = 'dynamic')
    
    def __repr__(self):
        return self.name
        
        
class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True, index = True)
    books = db.relationship('BookAuthor', backref = 'author', lazy = 'dynamic')
    
    def __repr__(self):
        return self.name
        
        
class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    
    def __repr__(self):
        return '< ' + str(self.book_id) + ', ' + str(self.author_id) + ' >'

