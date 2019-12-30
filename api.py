


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_whooshalchemy as wa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+oursql://root:mysql@localhost/outreach'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['WHOOSH_BASE']='whoosh'

db = SQLAlchemy(app)

class Article(db.Model):
  __tablename__ = 'article'
  __searchable__ = ['title', 'content']  

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text)
  content = db.Column(db.Text)  

wa.whoosh_index(app, Article)

class Faq(db.Model):
  __tablename__ = 'faq'
  __searchable__ = ['question', 'answer']  

  id = db.Column(db.Integer, primary_key=True)
  question = db.Column(db.Text)
  answer = db.Column(db.Text)

# class Knowledgebase(db.Model):
# 	__tablename__ = 'knowledgebase'
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(128), nullable=False)
#     categories

class Role(db.Model):

    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

if __name__ == '__main__':
	app.run(debug=True)