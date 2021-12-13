"""
General routes
"""
from flask import Blueprint, render_template, redirect, url_for, request, flash

from clinic_app.views.api_controllers import ApiHelper

general_bp = Blueprint('general', __name__)


# pylint: disable=missing-function-docstring
@general_bp.route('/')
def index():
    return render_template('index.html')


@general_bp.route('/doctors')
def doctors():
    page = request.args.get('page')
    per_page = request.args.get('per_page', default=8)
    response = ApiHelper.doctors.get(page=page, per_page=per_page)
    if response.status_code == 200:
        data = response.json
    else:
        data = {'page': 1, 'per_page': 10, 'pages': 1, 'has_prev': False,
                'has_next': False, 'total': 0, 'items': []}
        flash('API error', 'error')
    if len(data['items']) == 0 < data['total']:
        return redirect(url_for('general.doctors'))
    return render_template('doctors.html', data=data)
