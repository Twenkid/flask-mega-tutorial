# flask-mega-tutorial

Miguel ...


Z:\flask\microblog> cmd /v /c "set FLASK_APP=microblog.py&& flask run"

 * Serving Flask app "microblog.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)


v4 ... db

```
Z:\flask\microblog>python -m flask db init

C:\Users\toshb\AppData\Local\Programs\Python\Python39\lib\site-packages\flask_sqlalchemy\__init__.py:851: UserWarning: Neither SQLALCHEMY_DATABASE_URI nor SQLALCHEMY_BINDS is set. Defaulting SQLALCHEMY_DATABASE_URI to "sqlite:///:memory:".
  warnings.warn(
C:\Users\toshb\AppData\Local\Programs\Python\Python39\lib\site-packages\flask_sqlalchemy\__init__.py:872: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
Creating directory Z:\flask\microblog\migrations ...  done
Creating directory Z:\flask\microblog\migrations\versions ...  done
Generating Z:\flask\microblog\migrations\alembic.ini ...  done
Generating Z:\flask\microblog\migrations\env.py ...  done
Generating Z:\flask\microblog\migrations\README ...  done
Generating Z:\flask\microblog\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'Z:\\flask\\microblog\\migrations\\alembic.ini' before proceeding.
```

## v7 - Errors 

Install: 
```
python -m pip install Werkzeug==0.15.6
```
0.15.5 - bug when turning on the development mode

Debug mode vs production ... Console, stack trace ... don't activate on production server!

```
cmd /v /c "set FLASK_APP=microblog.py&&set FLASK_ENV=development&&flask run"
cmd /v /c "set FLASK_APP=microblog.py&&set FLASK_ENV=production&&flask run"
```

Receive mail in the console:

```
python -m smtpd -n -c DebuggingServer localhost:8025
```

Users: aaaa 1111
kur 1
etc.
Try to change the user name in Edit Profile to the existing kur --> Validation, error etc.

Send error via email, logging to /logs ... rotation

```
Z:\flask\microblog>cmd /v /c "set FLASK_APP=microblog.py&&set FLASK_ENV=production&&set MAIL_SERVER=localhost&&set MAIL_PORT=8025&&flask run"

 * Serving Flask app "microblog.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
SQLALCHEMY_DATABASE_URI= sqlite:///Z:\flask\microblog\app.db
[2021-12-15 19:42:46,032] INFO in __init__: Microblog startup
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [15/Dec/2021 19:42:58] "←[37mGET /index HTTP/1.1←[0m" 200 -
127.0.0.1 - - [15/Dec/2021 19:43:00] "←[37mGET /index HTTP/1.1←[0m" 200 -
avatar= https://www.gravatar.com/avatar/a3cdcf905995a6e83ca1e78c81cb6c47?d=identicon&s=128
avatar= https://www.gravatar.com/avatar/a3cdcf905995a6e83ca1e78c81cb6c47?d=identicon&s=36
avatar= https://www.gravatar.com/avatar/a3cdcf905995a6e83ca1e78c81cb6c47?d=identicon&s=36
127.0.0.1 - - [15/Dec/2021 19:43:02] "←[37mGET /user/aaaa HTTP/1.1←[0m" 200 -
127.0.0.1 - - [15/Dec/2021 19:43:10] "←[37mGET /edit_profile HTTP/1.1←[0m" 200 -
127.0.0.1 - - [15/Dec/2021 19:43:12] "←[32mPOST /edit_profile HTTP/1.1←[0m" 302 -
127.0.0.1 - - [15/Dec/2021 19:43:12] "←[37mGET /edit_profile HTTP/1.1←[0m" 200 -
127.0.0.1 - - [15/Dec/2021 19:43:25] "←[32mPOST /edit_profile HTTP/1.1←[0m" 302 -
127.0.0.1 - - [15/Dec/2021 19:43:25] "←[37mGET /edit_profile HTTP/1.1←[0m" 200 -
127.0.0.1 - - [15/Dec/2021 19:43:40] "←[37mGET /index HTTP/1.1←[0m" 200 -
127.0.0.1 - - [15/Dec/2021 19:43:41] "←[32mGET /logout HTTP/1.1←[0m" 302 -
127.0.0.1 - - [15/Dec/2021 19:43:42] "←[32mGET /index HTTP/1.1←[0m" 302 -
127.0.0.1 - - [15/Dec/2021 19:43:42] "←[37mGET /login?next=%2Findex HTTP/1.1←[0m" 200 -
```

## v8
16.12.2021

Followers, foreign keys, followers and followed by, emptyform, ... OK

Manually creating the followers table with a one-time call, migrate upgrade sequence fails, KeyFormatter ...

In models.py

```
def AddFollowersV8():
   print("AddFollowersV8")
   from sqlalchemy import create_engine
   engine = create_engine('sqlite:///app.db')   
   engine.execute('CREATE TABLE followers(follower_id Integer, followed_id Integer, FOREIGN KEY(follower_id) references users(user_id), FOREIGN KEY(followed_id) references users(user_id))')
   print("#AFTER ... engine.execute('CREATE TABLE followers ...")

AddFollowersV8()
```

## v9 - Pagination ... 

17.12.2021
~ 60 min

PostForm ... paginate ... posts.items ...  return redirect(url_for('index'))

## v10 - Email, token jwt, ResetPasswordRequestForm ...

~ 34 min (without the upload)

## v11 - Bootstrap CSS framework ...
19.12.2021

~ 17 - 21 min

pip install flask-bootstrap

## v12 - Time formatting, moment, js ... 
19.12.2021

~ 13 - 14 min

## v13, v14 - flask-babel (localisation), ... translation via Microsoft Azure API, js ...

20.12.2021


--> start Elasticsearch v15 ... (Install, configure:...)

Edit jvm.options
Add:

-Xms262m
-Xmx262m

(default 4G - too big)

A comment suggests to add a file in the directory:
jvm.options.d
however adding it didn't change the config.

(Elastic 7.16.2)

with 4G it demands to allocate 17 GB memory.

Issues with the RAM disk drivers (probably), like with Rust cargo.
See log: ...


## v15 - Downloaded, added my app.db in 

21.12.2021

Better app structure.
Cloned from Miguel's, added my app.db.


## v16 - Elasticsearch ...

21.12.2021

- I cloned the Miguel's repository, but added my app.db to the folder of config.py etc.
Also I had to comment one form validation which was causing an error.

* Install Elastic and run it:

http://localhost:9200

It doesn't start correctly on a RAM disk (imdisk).

Set the env.variable when calling: 
``` 
cmd /v /c "set FLASK_APP=microblog.py&&set FLASK_ENV=production&&set MAIL_SERVER=localhost&&set MAIL_PORT=8025&&set ELASTICSEARCH_URL=http://localhost:9200&&flask run"
```
(Or/and set in in the .env file in the folder /microblog  with microblog.py, config.pt)

While Elastic is running, add new posts: they will be added to the Elastic index.
Search.

It finds only exact word matches, as it is here.

Changes from the tutorial:

In routes.py:  I commented the search form validation, it always throws exception, but there's not error.

```
@bp.route('/search')
@login_required
def search():
    #if not g.search_form.validate():
    #    print("ERROR: if not g.search_form.validate():...")    
    #    return redirect(url_for('main.explore'))
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title=_('Search'), posts=posts,
                           next_url=next_url, prev_url=prev_url)
```



__Useful links:__
https://www.pythonsheets.com/notes/python-sqlalchemy.html

## v20 - AJAX js jQuery popup ...

24.12.2021

base.html


## v21 - Messages and Notifications ... 

#30.12.2021
```
Creation of the new DB tables etc.
(without foreign keys and a few others;
 migrate didn't work in the previous versions,
 so I used sqlite console. SQLite doesn't support
alter table add constraint (?) and would require
to recreate the table (copy to a new one etc.?)

The app worked anyway.

c:\DB\sqlite>sqlite3 Z:\v21\microblog\app.db
SQLite version 3.37.0 2021-11-27 14:13:22
Enter ".help" for usage hints.
sqlite> Create table Notification(
   ...>   id INTEGER PRIMARY KEY,
   ...>     name TEXT(128),
   ...>     user_id  INTEGER,
   ...> timestamp DateTime default(NOW()),
   ...> payload_json TEXT
   ...> );
sqlite> alter table user add column last_message_read_time;

v21

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	
	==>

CREATE TABLE Message (
    id INTEGER PRIMARY KEY, 
    sender_id INTEGER, 
    recipient_id  INTEGER,
	body TEXT(140),
	timestamp DateTime default(NOW()),
    FOREIGN KEY(sender_id) REFERENCES user(id),
	FOREIGN KEY(recipient_id) REFERENCES user(id)
	);
	
	
	class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.Float, index=True, default=time)
    payload_json = db.Column(db.Text)


class User(UserMixin, db.Model):
    # ...
    notifications = db.relationship('Notification', backref='user',
                                    lazy='dynamic')
    ? How in SQL?
	OrderID REFERENCES Orders(ID)
	user - table, notification is table 
	

==>

Create table Notification(
  id INTEGER PRIMARY KEY, 
    name TEXT(128), 
    user_id  INTEGER,	
	timestamp DateTime default(NOW()),
	payload_json TEXT
	
	
);

alter table user add column last_message_read_time;

XXXXXX
	
class User(UserMixin, db.Model):
 messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)


Alter table user add column messages_read_time Datetime;

```
