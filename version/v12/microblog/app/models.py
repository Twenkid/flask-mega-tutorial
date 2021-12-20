from datetime import datetime
#from app import db
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from time import time #v10
import jwt
from app import app

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

#db = SQLAlchemy(app)


'''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
'''
#'''
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)
#'''
print(followers)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    #added v6
    #Every time the database is modified it is necessary to generate a database migration
    #python -m flask db migrate -m "new fields in user model"
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        s = 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
        print("avatar=",s)
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
            
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
            
    def followed_posts(self): #v8
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())
        
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)
      


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
        

def AddColumnsV6():
   #about_me = db.Column(db.String(140))
   #last_seen = db.Column(db.DateTime, default=datetime.utcnow)
   from sqlalchemy import create_engine
   engine = create_engine('sqlite:///app.db')
   engine.execute('alter table user add column about_me String(140)')
   engine.execute('alter table user add column last_seen dateTime')

def AddFollowersV8():
   print("AddFollowersV8")
   #about_me = db.Column(db.String(140))
   #last_seen = db.Column(db.DateTime, default=datetime.utcnow)
   from sqlalchemy import create_engine
   engine = create_engine('sqlite:///app.db')
   #engine.execute('create table follower')
   #engine.execute('alter table follower add column follower_id Integer) # foreignkey=user.id')  
   engine.execute('CREATE TABLE followers(follower_id Integer, followed_id Integer, FOREIGN KEY(follower_id) references users(user_id), FOREIGN KEY(followed_id) references users(user_id))'
   )
   print("#AFTER ... engine.execute('CREATE TABLE followers ...")
 
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
  users = User.query.all()  #while migrating v6
  print(users)  
  for u in users:
    print(u.id, u.username)
  u = User.query.get(1)  
  print(u)
  #print(u.posts.all()) #up to v4  
  u = User.query.get(2)
  print(u)
  posts = Post.query.all()
  #for p in posts:  #up to v4
  #  print(p.id, p.author.username, p.body)
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
  
#AddColumnsV6() #only for v6  
#ShowState()


#AddFollowersV8() #call once 