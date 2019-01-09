from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Tweet

import unittest

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def seed_db():
    db.session.add(Tweet(title='Carver Edison', name="Prakash Sinha"))
    db.session.add(Tweet(title='Software Engineer', name="Gamal Ali"))
    db.session.commit()

@cli.command()
def test():
    """ Runs tests without code coverage """
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner().run(tests)
    if result.wasSuccessful():
        return 0
    return 1
    



if __name__ == '__main__':
    cli()