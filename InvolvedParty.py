
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

engineIcms = create_engine('ibm_db_sa://saazimi:Pq+5x?8MUVbYr>uux3qk@172.29.250.66:50000/ICMSD148', echo=True)
SessionIcms = sessionmaker(bind=engineIcms)
sessionIcms = SessionIcms()
Base1 = declarative_base()

class InvolvedParty(Base1):

    __tablename__ = 'TB_INVOLVED_PARTY'
    schema = 'CRM'
    id = Column(Integer, primary_key=True)
    customer_id = Column(String(30))
    fk_lkp_iptype = Column(Integer, nullable=False)
    first_name = Column(String(300), nullable=False)
    last_name = Column(String(300))
    en_first_name = Column(String(150))
    en_last_name = Column(String(150))
    fk_lkp_is_legal_capacity = Column(Integer)
    fk_lkp_is_reference_verified = Column(Integer)
    reference_verified_date = Column(DateTime)
    fk_lkp_data_share_level = Column(Integer)
    national_code_national_id = Column(String(30))
    identity_code = Column(String(30))
    fida_code = Column(String(30))
    identity_serial_code = Column(Integer)
    identity_serichar_code = Column(String(30))
    identity_serinumber_code = Column(String(30))
    fk_lkp_is_replica_identity = Column(Integer)
    fk_lkp_nationality_type = Column(Integer, nullable=False)
    birth_date = Column(DateTime, nullable=False)
    fk_lkp_residentalsatus = Column(Integer)
    fk_lkp_legal_competency_type = Column(Integer)
    fk_lkp_legal_incompetency_type = Column(Integer)
    description = Column(String(300))
    death_date = Column(DateTime)
    fk_brc_branch_code_id = Column(Integer, nullable=False)
    fk_loc_geolocation_id_country = Column(Integer)
    fk_loc_geolocation_id_city = Column(Integer)
    fk_loc_geolocation_id_place_of_residence = Column(Integer)
    economic_id = Column(String(30))
    identity_document_id = Column(String(30))
    fk_lkp_identity_document_type_id = Column(Integer)
    postal_code = Column(String(10))
    created_by = Column(Integer)
    created_date = Column(DateTime)
    last_modified_by = Column(Integer)
    last_modified_date = Column(DateTime)
    version = Column(String)
    competency_description = Column(String(150))
    shahab_code = Column(Integer)
    fk_lkp_sanction = Column(Integer)
    fk_lkp_customer_segment = Column(Integer)
