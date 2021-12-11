from datetime import datetime
from app import db

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

#db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
        

# add a row
# comment out after the 1st run
def InitialAdd():
    from app.models import User, Post
    table_row = User(username="My Name", email="myemail@mail.com")
    db.session.add(table_row)
    db.session.commit()        
    table_row = User(username="AAAA", email="myffff@mail.com")
    db.session.add(table_row)
    db.session.commit()        
    u = User(username='john', email='john@example.com')    
    db.session.add(u)
    db.session.commit()
    u = User(username='susan', email='susan@example.com')
    db.session.add(u)
    db.session.commit()
def ShowState():
  users = User.query.all()
  print(users)
  for u in users:
    print(u.id, u.username)
  u = User.query.get(1)  
  print(u)
  print(u.posts.all())
  print(u.posts.all())
  u = User.query.get(2)
  print(u)
  posts = Post.query.all()
  for p in posts:
    print(p.id, p.author.username, p.body)
  s = User.query.order_by(User.username.desc()).all()
  print(s)
    
'''    
def DeleteAll():
  users = User.query.all()
  for u in users:
    db.session.delete(u)

  posts = Post.query.all()
  for p in posts:
    db.session.delete(p)

  db.session.commit()
'''
  
def AddPosts():  

  '''
  p = Post(body='my first post!', author=u)
  db.session.add(p)
  db.session.commit()
  '''
  
ShowState()

