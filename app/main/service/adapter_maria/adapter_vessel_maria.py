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

from models.vessel import Vessel, Tank, File


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
            tanksPropos = data['tanksProps']
            images_array = data['images']
            print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",images_array)
            # f = open("/home/olfa/Desktop/test.txt", "w")
            # f.write(str(images_array))
            # f.close()
            
            # print("*************************",type(images_array))
            #print(tanksPropos)
            new_vessel = Vessel(
                name=data['Name'],
                imo = data['IMO'],
                vtype = data ['Type'],
                flag = data ['Flag'],
                yearbuilt = data ['YearBuilt'],
                shipyard = data ['Shipyard'],
                owner = data ['Owner'],
                operator = data ['Operator'],
                vclass = data ['Class'],
                atex = data['Atex'],
                ais = data ['AIS'],
                mmsi = data['MMSI'],
                grt = data['GRT'],
                dwt = data['DWT'],
                capacity = data['Capacity'],
                length = data['Length'],
                beam = data['Beam'],
                draft = data['Draft'],
                DraftUnit = data ['DraftUnit'],
                BeamUnit = data['BeamUnit'],
                LengthUnit = data['LengthUnit'],
                techDetailsFileName = data['techDetails']['_fileNames'],
                linearityFileName = data['linearity']['_fileNames'],
                q88FileName = data['q88']['_fileNames'],
                sireReportFileName = data['sireReport']['_fileNames'],
                            )
            session.add(new_vessel)
            session.commit()

            #save tanks and file names
            session = Session_lc_config()
            query = 'select id from vessel order by id desc limit 1;'
            res = engine_lc_config.execute(query)
            last_id = res.fetchone()
            # print("========================", last_id[0])


            #save tanks
            for t in tanksPropos:
                # print("taaaaaaaaaaaaaaaaaaaaaaank",t)
                new_tank = Tank(
                    tank_name =  t['tankName'],
                    volume = t['tankVolume'] ,
                    tonnage = t ['tonnage'],
                    issloptank = t['isSlopTank'],
                    id_vessel = int(last_id[0])
                )
                session.add(new_tank)
                session.commit()

            #save image file names
            for img_name in images_array:
                new_file = File(
                    file_name = img_name,
                    id_vessel = int(last_id[0])
                )
                session.add(new_file)
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




