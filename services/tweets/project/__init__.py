import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# instantiate the db
db = SQLAlchemy()

# Application Factory Pattern
# http://flask.pocoo.org/docs/1.0/patterns/appfactories/
def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    # allowing CROSS ORIGIN on all routes - this is an exercise. No problem!
    CORS(app)

    # config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.tweets import tweets_blueprint
    # import pdb; pdb.set_trace()
    app.register_blueprint(tweets_blueprint)

    # shell context for cli 
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}
    
    return app


