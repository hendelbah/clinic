"""
Package contain service classes and functions to work with database
"""
from clinic_app.service.basic_query_helper import BasicQueryHelper
from clinic_app.service.population import populate

def func():
    r = BasicQueryHelper.exists(None)

    print(r)

    x = {}