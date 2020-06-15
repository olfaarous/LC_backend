import os
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import pymysql

pymysql.install_as_MySQLdb()
from sqlalchemy.exc import SQLAlchemyError
import uuid
import datetime

from sqlalchemy import or_

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir))
sys.path.insert(1, root_dir)

from lc_config_db import Session_lc_config,engine_lc_config

from models.vessel import Vessel


class VesselAdapterStorage():

    def search_vessel_by_id(self, id):
        try:
            session = Session_gemini_config()
            return session.query(Vessel).filter_by(id=id).first()
        finally:
            session.close()


    # search vessel by name
    def search_vessel_by_name(self, data):
        try:
            session = Session_lc_config()
            return session.query(Vessel).filter(
                or_(Vessel.name == data['name'])).first()
        finally:
            session.close()

    # add a new vessel in mariadb
    def add_new_vessel(self, data):
        try:
            session = Session_lc_config()
            new_vessel = Vessel(
                name=data['name'],
                imo = data['imo'],
                vtype = data ['vtype'],
                flag = data ['flag'],
                yearbuilt = data ['yearbuilt'],
                shipyard = data ['shipyard'],
                owner = data ['owner'],
                operator = data ['operator'],
                vclass = data ['vclass'],
                atex = data['atex'],
                ais = data ['ais'],
                mmsi = data['mmsi'],
                grt = data['grt'],
                dwt = data['dwt'],
                capacity = data['capacity'],
                length = data['length'],
                beam = data['beam'],
                draft = data['draft'],
                
            )
            session.add(new_vessel)
            session.commit()
        finally:
            session.close()

    def get_all_vessels(self):
        try:
            session = Session_lc_config()
            return session.query(Vessel).all()
        finally:
            session.close()


class TankAdapterStorage():
    def search_tank_by_id(self, id):
        try:
            session = Session_gemini_config()
            return session.query(Tank).filter_by(id=id).first()
        finally:
            session.close()

    def add_new_tank(self,data):
        try:
            session = Session_lc_config()
            new_tank = Tank(
                tank_name=data['tank_name'],
                volume = data['volume'],
                tonnage = data ['tonnage'],
                issloptank = data ['issloptank'],
            )
            session.add(new_tank)
            session.commit()
        finally:
            session.close()




