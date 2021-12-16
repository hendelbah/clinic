"""
General routes
"""
from flask import Blueprint, render_template, redirect, url_for, request

from clinic_app.service import DoctorService

general_bp = Blueprint('general', __name__)


# pylint: disable=missing-function-docstring
@general_bp.route('/')
def index():
    return render_template('index.html')


@general_bp.route('/doctors')
def doctors():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=8, type=int)
    pagination = DoctorService.get_pagination(page=page, per_page=per_page)
    if len(pagination.items) == 0 < pagination.total:
        return redirect(url_for('general.doctors'))
    return render_template('doctors.html', data=pagination)
