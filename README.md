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
