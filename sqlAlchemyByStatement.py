from sqlalchemy import create_engine, Column, Integer, String,join,select,MetaData,Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from InvolvedParty import InvolvedParty
from IranianReal import IranianReal
from sqlalchemy import Column, Integer, String, DateTime


# create engine and session
engineIcms = create_engine('ibm_db_sa://saazimi:Pq+5x?8MUVbYr>uux3qk@172.29.250.66:50000/ICMSD148', echo=True)
SessionIcms = sessionmaker(bind=engineIcms)
sessionIcms = SessionIcms()
metadata = MetaData(bind = engineIcms)
#Base1 = declarative_base()

TB_INVOLVED_PARTY = Table('TB_INVOLVED_PARTY',metadata,autoload=True)
select_statement = select([TB_INVOLVED_PARTY])
with engineIcms.connect() as connection:
    result = connection.execute(select_statement)
    rows = result.fetchall()


"""
class TB_INVOLVED_PARTY(Base1):
    __table__ = Base1.metadata.tables['CRM.TB_INVOLVED_PARTY']
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
"""

engineNahab = create_engine('ibm_db_sa://saazimi:emYhSJotG0m7d6b2FlM9@172.29.250.66:50000/nahab164', echo=True)
SessionNahab = sessionmaker(bind=engineNahab)
sessionnahab = SessionNahab()
Base2 = declarative_base()

class TB_IRANIAN_REAL(Base2):
    
    __table__ = Base2.metadata.tables['NAHAB.TB_IRANIAN_REAL']
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




join_query = sessionIcms.query(TB_INVOLVED_PARTY, TB_IRANIAN_REAL).join(TB_IRANIAN_REAL, TB_INVOLVED_PARTY.national_code_national_id == TB_IRANIAN_REAL.identification_no)
result = join_query.all()





#IPStatement = select(InvolvedParty.national_code_national_id , InvolvedParty.birth_date).where(InvolvedParty.fk_lkp_iptype == 1601 and InvolvedParty.fk_lkp_nationality_type == 9001)
#NahabStatement = select(IranianReal.identification_no , InvolvedParty.birth_date)
#joinedStatement = IPStatement.join(NahabStatement,InvolvedParty.national_code_national_id == IranianReal.identification_no)


#join_query = join(TB_INVOLVED_PARTY, TB_IRANIAN_REAL, TB_INVOLVED_PARTY.national_code_national_id == TB_IRANIAN_REAL.identification_no)
#join_query = join(TB_INVOLVED_PARTY, TB_IRANIAN_REAL,TB_INVOLVED_PARTY == TB_IRANIAN_REAL[0][:])

#result = connIcms.execute( select([TB_INVOLVED_PARTY, TB_IRANIAN_REAL]).select_from(join_query) )

""""
# Define aliases for the two tables to use in the join
involved_party_alias = aliased(InvolvedParty)
iranian_real_alias = aliased(IranianReal)

results = sessionnahab.query(
    involved_party_alias.national_code_national_id,
    involved_party_alias.birth_date,
    iranian_real_alias.identification_no,
    iranian_real_alias.birth_date
).join(
    iranian_real_alias,
    involved_party_alias.national_code_national_id == iranian_real_alias.identification_no
).all()

for party in results:
    print(party)

    """