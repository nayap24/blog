import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #MAIL_SERVER = 'localhost'
    #MAIL_PORT = 8025
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = 'joe'
    #MAIL_PASSWORD = 'abc'
    BLOG_MAIL_SUBJECT_PREFIX = '[Blog]'
    BLOG_MAIL_SENDER = 'Blog Admin <blog@localhost>'
    BLOG_ADMIN = 'joe@ariapa.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOG_POSTS_PER_PAGE = 20


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://{}'.format(os.path.join(basedir, 'data-test.sqlite'))


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
