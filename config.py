import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    #MAIL_USE_TLS = True
    BLOG_MAIL_SUBJECT_PREFIX = '[Ariapa]'
    BLOG_MAIL_SENDER = 'Ariapa Admin <no-rely@ariapa.com>'
    BLOG_ADMIN = 'joe@ariapa.com'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOG_POSTS_PER_PAGE = 20
    BLOG_FOLLOWERS_PER_PAGE = 50

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://{}'.format(os.path.join(basedir, 'data-test.sqlite'))


class ProductionConfig(Config):
    pass

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler, RotatingFileHandler
        credentials = None
        secure = None
        mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr=cls.BLOG_MAIL_SENDER,
                toaddrs=[cls.BLOG_ADMIN],
                subject='Ariapa Failure',
                credentials=credentials,
                secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        # size of log file 50KB, keeping the last 10 log files as backup
        file_handler = RotatingFileHandler('logs/ariapa.log', maxBytes=51200, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
                '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Ariapa startup')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
