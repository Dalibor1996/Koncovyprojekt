from main import db

class Books(db.Model):
    __tablename__ = 'books'

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('public.authors.author_id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('public.genres.genre_id'), nullable=True)
    isbn = db.Column(db.String(13), nullable=True)
    publication_year = db.Column(db.Integer, nullable=True)
    copies = db.Column(db.Integer, default=1, nullable=True)

    author = db.relationship("Author", back_populates="books")
    genre = db.relationship("Genre", back_populates="books")
