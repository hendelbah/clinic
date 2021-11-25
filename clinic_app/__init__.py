from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    return 1


if __name__ == '__main__':
    app = create_app()
