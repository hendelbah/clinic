from clinic_app.views.api_controllers import ItemApiController, CollectionApiController


class ApiHelper:
    user = ItemApiController('api.user')
    doctor = ItemApiController('api.doctor')
    patient = ItemApiController('api.patient')
    b_appointment = ItemApiController('api.booked_appointment')
    s_appointment = ItemApiController('api.served_appointment')
    users = CollectionApiController('api.users')
    doctors = CollectionApiController('api.doctors')
    patients = CollectionApiController('api.patients')
    b_appointments = CollectionApiController('api.booked_appointments')
    s_appointments = CollectionApiController('api.served_appointments')
