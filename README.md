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
