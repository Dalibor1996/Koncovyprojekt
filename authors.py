# from main import db
#
# class Authors(db.Model):
#     __tablename__ = 'authors'
#
#     author_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     bio = db.Column(db.String())
# with open('/mnt/data/authors.py', 'r') as file:
#     authors_py_content = file.read()
#
# authors_py_content
from main import db

class Authors(db.Model):
    __tablename__ = 'authors'

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    bio = db.Column(db.String())
