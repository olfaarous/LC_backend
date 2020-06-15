import uuid
import datetime
import logging
import os, sys
from sqlalchemy import or_ 
from sqlalchemy.exc import SQLAlchemyError

from .adapter_maria.adapter_vessel_maria import VesselAdapterStorage
vessel_adapter_storage = VesselAdapterStorage()

log = logging.getLogger(__name__) 
log.setLevel('ERROR')  


def get_all_vessels(): 
    try:
        return vessel_adapter_storage.get_all_vessels()
    except SQLAlchemyError as e:
        log.exception("Getting all vessels exception", exc_info=e)
        return []

def get_a_vessel(id):
    try:
        vessel = vessel_adapter_storage.search_vessel_by_id(id)
        if vessel:
            return vessel
        else:
            return {}
    except SQLAlchemyError as e:
        log.exception("Filtring vessels by id exception", exc_info=e)
        response_object = {
                'status': 'fail',
                'message': 'Vessel can’t be returned du to technical issues'
        }
        return response_object, 500

def save_new_vessel(data):
    try:
        vessel = vessel_adapter_storage.search_vessel_by_name(data)
        if not vessel:
            vessel_adapter_storage.add_new_vessel(data)
            response_object = {
                'response': True,
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'response': False,
                'status': 'fail',
                'message': 'Vessel already exists. Please Log in.',
            }
            return response_object, 409
    except SQLAlchemyError as e:
        log.exception("Adding new vessel exception", exc_info=e)
        response_object = {
            'response': False,
            'status': 'fail',
            'message': 'Vessel can’t be created du to technical issues'
        }
        return response_object, 500



def save_changes(data):
    db.session.add(data)
    db.session.commit()
