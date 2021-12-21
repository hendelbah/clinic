"""
Admin panel routes
"""
from datetime import date

from flask import Blueprint, render_template, abort, redirect, url_for, flash, request
from flask_login import current_user, login_required

from clinic_app.models import User, Doctor, Patient
from clinic_app.service import UserService, DoctorService, PatientService
from clinic_app.views.forms import FilterUsers, EditUser, FilterDoctors, EditDoctor, \
    FilterPatients, EditPatient
from clinic_app.views.utils import get_pagination_args, random_password, parse_filters, \
    extract_filters

admin_bp = Blueprint('admin', __name__, url_prefix='/admin-panel')

user_endpoints = {
    'list': 'admin.users',
    'item': 'admin.user',
    'delete': 'admin.delete_user'
}
doctor_endpoints = {
    'list': 'admin.doctors',
    'item': 'admin.doctor',
    'delete': 'admin.delete_doctor'
}
patient_endpoints = {
    'list': 'admin.patients',
    'item': 'admin.patient',
    'delete': 'admin.delete_patient'
}
appointment_endpoints = {
    'list': 'admin.appointments',
    'item': 'admin.appointment',
    'delete': 'admin.appointment_delete'
}


@admin_bp.before_request
def admins_only():
    """
    Checks if user is logged in and has admin privileges
    before all requests for this blueprint.
    """
    if response := login_required(lambda: None)() is not None:
        return response
    if not current_user.is_admin:
        return abort(403)
    return None


# pylint: disable=missing-function-docstring
@admin_bp.route('/')
def index():
    return render_template('admin_panel/index.html')


@admin_bp.route('/users', methods=['GET', 'POST'])
def users():
    form = FilterUsers()
    if form.validate_on_submit():
        filters = extract_filters(['search_email'], form)
        return redirect(url_for('admin.users', **filters))
    filters = parse_filters([{'key': 'search_email'}], form)
    pages = get_pagination_args()
    data = UserService.get_pagination(*pages, **filters)
    return render_template('admin_panel/users.html', data=data, form=form, title='Users',
                           active_menu_item=1, endpoints=user_endpoints)


@admin_bp.route('/users/<uuid>', methods=['GET', 'POST'])
def user(uuid):
    choices = [('', '<None>')]
    if uuid == 'new':
        title = 'New user'
        user_ = None
    else:
        user_ = UserService.get(uuid)
        if user_ is None:
            abort(404)
        if user_.doctor is not None:
            choices.append((user_.doctor.uuid, user_.doctor.full_name))
        title = f'{user_.email}'
    form = EditUser(obj=user_)
    pagination = DoctorService.get_pagination(per_page=100, no_user=True)
    choices.extend((doc.uuid, doc.full_name) for doc in pagination.items)
    form.doctor_uuid.choices = choices
    if form.validate_on_submit():
        if uuid == 'new':
            user_ = User('', '', False)
            password = random_password()
            user_.set_password(password)
        form.populate_obj(user_)
        error = UserService.save_instance(user_)
        if error is None:
            flash('Data saved successfully', 'success')
            if 'uuid' == 'new':
                pass
                # :TODO: send password to the email of new user
        else:
            flash(f'Error: {error}', 'error')
        return redirect(url_for('admin.users'))
    return render_template('admin_panel/item.html', item=user_, form=form, item_name='user',
                           title=title, active_menu_item=1, readonly=('email',),
                           endpoints=user_endpoints)


@admin_bp.route('/users/<uuid>/delete', methods=['POST'])
def delete_user(uuid):
    result = UserService.delete(uuid)
    if result:
        flash('User deleted successfully', 'success')
    else:
        flash('Can\'t delete: user not found', 'error')
    return redirect(url_for('admin.users'))


@admin_bp.route('/doctors', methods=['GET', 'POST'])
def doctors():
    form = FilterDoctors()
    filters = {'patient': request.args.get('patient')}
    if form.validate_on_submit():
        filters = extract_filters(['search_name'], form)
        return redirect(url_for('admin.doctors', **filters))
    filters = parse_filters([{'key': 'search_name'}], form)
    pages = get_pagination_args()
    data = DoctorService.get_pagination(*pages, **filters)
    return render_template('admin_panel/doctors.html', data=data, form=form, title='Doctors',
                           active_menu_item=2, endpoints=doctor_endpoints)


@admin_bp.route('/doctors/<uuid>', methods=['GET', 'POST'])
def doctor(uuid):
    if uuid == 'new':
        title = 'New doctor'
        doctor_ = None
    else:
        doctor_ = DoctorService.get(uuid)
        if doctor_ is None:
            abort(404)
        title = f'{doctor_.full_name}'
    form = EditDoctor(obj=doctor_)
    if form.validate_on_submit():
        if uuid == 'new':
            doctor_ = Doctor('', '', '', 0)
        form.populate_obj(doctor_)
        error = DoctorService.save_instance(doctor_)
        if error is None:
            flash('Data saved successfully', 'success')
        else:
            flash(f'Error: {error}', 'error')
        return redirect(url_for('admin.doctors'))
    return render_template('admin_panel/item.html', item=doctor_, form=form, item_name='doctor',
                           title=title, active_menu_item=2, readonly=(), endpoints=doctor_endpoints)


@admin_bp.route('/doctors/<uuid>/delete', methods=['POST'])
def delete_doctor(uuid):
    result = DoctorService.delete(uuid)
    if result:
        flash('Doctor deleted successfully', 'success')
    else:
        flash('Can\'t delete: doctor not found', 'error')
    return redirect(url_for('admin.doctors'))


@admin_bp.route('/patients', methods=['GET', 'POST'])
def patients():
    form = FilterPatients()
    if form.validate_on_submit():
        filters = extract_filters(['search_phone', 'search_name'], form)
        return redirect(url_for('admin.patients', **filters))
    kwargs_list = [{'key': 'search_phone'}, {'key': 'search_name'}]
    filters = parse_filters(kwargs_list, form)
    pages = get_pagination_args()
    data = PatientService.get_pagination(*pages, **filters)
    return render_template('admin_panel/patients.html', data=data, form=form, title='Patients',
                           active_menu_item=3, endpoints=patient_endpoints)


@admin_bp.route('/patients/<uuid>', methods=['GET', 'POST'])
def patient(uuid):
    if uuid == 'new':
        title = 'New patient'
        patient_ = None
    else:
        patient_ = PatientService.get(uuid)
        if patient_ is None:
            abort(404)
        title = f'{patient_.surname} {patient_.name}'
    form = EditPatient(obj=patient_)
    if form.validate_on_submit():
        if uuid == 'new':
            patient_ = Patient('', '', date(1, 1, 1))
        form.populate_obj(patient_)
        error = DoctorService.save_instance(patient_)
        if error is None:
            flash('Data saved successfully', 'success')
        else:
            flash(f'Error: {error}', 'error')
        return redirect(url_for('admin.patients'))
    return render_template('admin_panel/item.html', item=patient_, form=form, item_name='patient',
                           title=title, active_menu_item=3, readonly=(),
                           endpoints=patient_endpoints)


@admin_bp.route('/patients/<uuid>/delete', methods=['POST'])
def delete_patient(uuid):
    result = PatientService.delete(uuid)
    if result:
        flash('Patient deleted successfully', 'success')
    else:
        flash('Can\'t delete: patient not found', 'error')
    return redirect(url_for('admin.patients'))


@admin_bp.route('/appointments')
def appointments():
    return render_template('admin_panel/appointment/list.html')
