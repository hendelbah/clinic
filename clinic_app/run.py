from clinic_app import create_app, db
import os

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()

    app.run()
