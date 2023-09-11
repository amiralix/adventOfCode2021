from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engineNahab = create_engine('ibm_db_sa://saazimi:emYhSJotG0m7d6b2FlM9@172.29.250.66:50000/nahab164', echo=True)
SessionNahab = sessionmaker(bind=engineNahab)
sessionnahab = SessionNahab()
Base =declarative_base()

class  nahabResponse(Base):
    __tablename__ = 'TB_NAHAB_RESPONSE'
    id = Column(Integer, primary_key=True)
    party_type_id = Column('FK_LKP_PARTY_TYPE', Integer, nullable=False)
    reference_id = Column(String(23), nullable=False)
    version = Column(Integer, nullable=False)
    created_by = Column('CREATE_BY', Integer, nullable=False)
    created_date = Column('CREATE_DATE', DateTime, nullable=False)
    last_modified_by = Column('LAST_MODIFIED_BY', Integer)
    last_modified_date = Column('LAST_MODIFIED_DATE', DateTime)
    shahab_code = Column(String(16))
    financial_level_activity = Column('FINANCIAL_LEVEL_ACTIVITY', Numeric(15))
    expiration_date = Column('EXPIRATION_DATE', DateTime)
    is_temporary_id = Column('FK_LKP_IS_TEMPORARY', Integer)