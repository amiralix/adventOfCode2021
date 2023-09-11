
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engineNahab = create_engine('ibm_db_sa://saazimi:emYhSJotG0m7d6b2FlM9@172.29.250.66:50000/nahab164', echo=True)
SessionNahab = sessionmaker(bind=engineNahab)
sessionnahab = SessionNahab()
Base2 = declarative_base()

class IranianReal(Base2):
    
    __tablename__ = 'TB_IRANIAN_REAL'
    schema = 'NAHAB'
    id = Column(Integer, primary_key=True)
    nahab_response_id = Column('FK_NRE', Integer, nullable=False)
    identification_no = Column('IDENTIFICATION_NO', String(30), nullable=False)
    birth_date = Column('BIRTH_DATE', DateTime, nullable=False)
    cert_no = Column('CERT_NO', Integer, nullable=False)
    cert_series = Column('CERT_SERIES', String(30))
    birth_location = Column('BIRTH_LOCATION', String(150))
    postal_code = Column('POSTAL_CODE', String(10))
    first_name = Column('FIRST_NAME', String(200))
    last_name = Column('LAST_NAME', String(250))
    father_name = Column('FATHER_NAME', String(100))
    sex_id = Column('FK_LKP_SEX', Integer)
    address = Column('ADDRESS', String(500))