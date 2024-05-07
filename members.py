from main import db

class Members(db.Model):
    __tablename__ = 'members'

    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    password = db.Column(db.String(250))
    email = db.Column(db.String(), unique=True)
    registration_date = db.Column(db.DateTime)

    # member_id = db.Column(db.Integer, primary_key=True)
    # firstname = db.Column(db.String())
    # email = db.Column(db.String())
