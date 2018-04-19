import os
from flask_migrate import Migrate

from app import create_app, db
from app.models import User, Role


config = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)


@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
