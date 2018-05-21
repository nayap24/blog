import os
from flask_migrate import Migrate, upgrade

from app import create_app, db
from app.models import User, Role, Permission, Post, Follow


config = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config)
migrate = Migrate(app, db)


#if __name__ == '__main__':
#    app.run()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Post=Post,
            Follow=Follow, Permission=Permission)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade

    # create or update user roles
    Role.insert_roles()

    # ensure all users are following themselves
    User.add_self_follows()
