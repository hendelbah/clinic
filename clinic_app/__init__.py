from flask import Flask
from models import db


def create_app(*, testing=False, test_db=False, echo=False):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    db_uri = 'mysql+pymysql://clinic_admin:clinic_pwd@localhost/' + ('clinic_test' if test_db else 'clinic')
    app.config.from_mapping(
        SECRET_KEY="qwerty",
        TESTING=testing,
        SQLALCHEMY_DATABASE_URI=db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=echo
    )

    db.app = app
    db.init_app(app)

    # from high_school import api
    # app.register_blueprint(api.api_bp, url_prefix='/api/v1')
    return app


if __name__ == '__main__':
    my_app = create_app(testing=True, echo=True)
    db.drop_all()
    db.create_all()
    # my_app.run()
