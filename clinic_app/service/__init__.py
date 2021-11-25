from sqlalchemy import create_engine
from clinic_app import db
engine = create_engine('mysql+pymysql://clinic_admin:clinic_pwd@localhost/clinic')

print(db)
with engine.connect() as connection:
    query = 'SHOW GRANTS'
    res = connection.execute(query)
    print(res.all())
