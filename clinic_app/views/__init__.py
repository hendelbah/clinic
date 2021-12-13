"""
This package contains all the frontend stuff.

Packages:

- `routes`: contains modules with frontend blueprints and all view functions.

Modules:

- `api_controllers.py': contains classes that help to send requests to API.
- `forms.py': there is all forms for posting data on web pages. It uses wtforms module.
- `user_login.py`: there is flask_login user class for authorization.
"""

from clinic_app.views.routes import auth_bp, general_bp
