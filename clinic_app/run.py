"""
This module should be used for running this application
"""
import os
from clinic_app import create_app, db
from clinic_app.service.db_population import populate

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    populate()
    # app.run()
