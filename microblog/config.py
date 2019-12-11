import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMINS = ['vishal.hmt@gmail.com']
    MAIL_SERVER="smtp.googlemail.com"
    MAIL_PORT=587
    MAIL_USE_TLS=1
    MAIL_USERNAME="vishwebprog1@gmail.com"
    MAIL_PASSWORD="password1212P"
    POSTS_PER_PAGE = 3