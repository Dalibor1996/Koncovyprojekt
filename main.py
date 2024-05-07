# from flask import Flask, request
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uphu5cktegkurlks01fn:8npUda12zKCJY0tDmdRki1ed0aiHVD@bnuedpct9qcua81ejilc-postgresql.services.clever-cloud.com:50013/bnuedpct9qcua81ejilc'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# from authors import Authors
#
# # @app.route("/authors", methods=["GET"])
# # def show_authors():
# #     authors = Authors.query.all()
# #     return f"authors"
# #     return Authors
# @app.route("/authors", methods=["GET"])
# def show_authors():
#     authors = Authors.query.all()
#     author_details = []
#     for author in authors:
#         author_info = {'id': author.author_id, 'name': author.name, 'bio': author.bio}
#         author_details.append(author_info)
#     return jsonify(author_details)
#
# if __name__ == '__main__':
#     app.run()
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure your database URI below
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://uphu5cktegkurlks01fn:8npUda12zKCJY0tDmdRki1ed0aiHVD@bnuedpct9qcua81ejilc-postgresql.services.clever-cloud.com:50013/bnuedpct9qcua81ejilc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import the Authors model after initializing the db
from authors import Authors
from members import Members

@app.route("/authors", methods=["GET"])
def show_authors():
    authors = Authors.query.all()
    author_details = []
    for author in authors:
        author_info = {'id': author.author_id, 'name': author.name, 'bio': author.bio}
        author_details.append(author_info)
    return jsonify(author_details)

@app.route("/members", methods=["GET"])
def show_members():
    members = Members.query.all()
    member_details = []
    for member in members:
        member_info = {'id': member.member_id, 'name': member.first_name, 'email': member.email}
        member_details.append(member_info)
    return jsonify(member_details)

@app.route("/members/<int:member_id>/", methods=["GET"])
def show_member(member_id):
    member = Members.query.get(member_id)
    if member is None:
        return jsonify({'error': 'Member not found'}), 404
    member_info = {'id': member.member_id, 'name': member.first_name, 'email': member.email}
    return jsonify(member_info)

@app.route("/members", methods=["POST"])
def register_member():
    requestjson = request.json
    if not requestjson or not 'first_name' in requestjson or not 'email' in requestjson:
        return jsonify({'error': 'Missing name or email'}), 400

    new_member = Members(
        first_name=requestjson['first_name'],
        last_name=requestjson['last_name'],
        email=requestjson['email']
    )

    db.session.add(new_member)
    db.session.commit()

    return jsonify({'message': 'Member registered successfully', 'id': new_member.member_id}), 201

if __name__ == '__main__':
    app.run(debug=True)  # Turn on debug mode for development
