import  sys
import os
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum,Sequence,LargeBinary
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship


root_dir =os.path.dirname(os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir)))
sys.path.insert(1, root_dir)
print(root_dir)
from lc_config_db import Base_lc_config, engine_lc_config


class Vessel(Base_lc_config):
    __tablename__ = "vessel"

    id = Column(Integer,Sequence('id_seq'), primary_key=True)
    name = Column(String(50), unique=False, nullable=True)
    imo = Column(String(50), unique=False, nullable=True)
    vtype = Column(String(50), unique=False, nullable=True)
    flag= Column(String(50), unique=False, nullable=True)
    yearbuilt = Column(Integer, unique=False, nullable=True)
    shipyard= Column(String(50), unique=False, nullable=True)
    owner = Column(String(50), unique=False, nullable=True)
    operator = Column(String(50), unique=False, nullable=True)
    vclass = Column(String(50), unique=False, nullable=True)
    atex = Column(String(50), unique=False, nullable=True)
    ais = Column(String(50), unique=False, nullable=True)
    mmsi = Column(String(50), unique=False, nullable=True)
    grt = Column(Integer, unique=False, nullable=True)
    dwt = Column(Integer, unique=False, nullable=True)
    capacity = Column(Integer, unique=False, nullable=True)
    length = Column(Integer, unique=False, nullable=True)
    beam = Column(Integer, unique=False, nullable=True)
    draft = Column(Integer, unique=False, nullable=True)
    DraftUnit = Column(String(50), unique=False, nullable=True)
    LengthUnit = Column(String(50), unique=False, nullable=True)
    BeamUnit = Column(String(50), unique=False, nullable=True)
    techDetailsFileName = Column(String(50) , unique=False, nullable=True)
    linearityFileName = Column(String(50) , unique=False, nullable=True)
    q88FileName = Column(String(50) , unique=False, nullable=True)
    sireReportFileName = Column(String(50) , unique=False, nullable=True)


    __table_args__ = {'extend_existing': True}

class Tank(Base_lc_config):
    __tablename__ = "tank"

    id = Column(Integer, Sequence('id_seq'), primary_key = True)
    tank_name = Column(String(50), unique=False, nullable=True)
    volume = Column(Integer, unique=False, nullable=True)
    tonnage = Column(Integer, unique=False, nullable=True)
    issloptank = Column(Boolean, unique=False, nullable=False, default=False)

    #relationship with vessel
    id_vessel = Column(Integer, ForeignKey('vessel.id'), nullable=True)
    __table_args__ = {'extend_existing': True}


class File(Base_lc_config):
    __tablename__ = "file"

    id= Column(Integer, Sequence('id_seq'), primary_key = True)
    file_name =  Column(String(50), unique=False, nullable=True)

    id_vessel = Column(Integer, ForeignKey('vessel.id'), nullable=True)
    __table_args__ = {'extend_existing': True}

Base_lc_config.metadata.create_all(engine_lc_config)
