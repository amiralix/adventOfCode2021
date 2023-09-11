from sqlalchemy import create_engine, Column, Integer, String,join,select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from InvolvedParty import InvolvedParty
from IranianReal import IranianReal
from ipQueryResponse import ipQueryResponse
from irealQueryResponse import *
import pandas as pd

# create engine and session
engineIcms = create_engine('ibm_db_sa://saazimi:Pq+5x?8MUVbYr>uux3qk@172.29.250.66:50000/ICMSD148', echo=True)
SessionIcms = sessionmaker(bind=engineIcms)
sessionIcms = SessionIcms()

engineNahab = create_engine('ibm_db_sa://saazimi:emYhSJotG0m7d6b2FlM9@172.29.250.66:50000/nahab164', echo=True)
SessionNahab = sessionmaker(bind=engineNahab)
sessionnahab = SessionNahab()
# create base class

# create base class
Base = declarative_base()

connIcms = engineIcms.connect()
connNahab = engineNahab.connect()



data = pd.read_csv("d:/deficit_ireanian_reals.csv")
for rows in range(0,len(data)):
    str_melli_code = str(data.NATIONAL_CODE_NATIONAL_ID[rows])
    myQueryString = f'select BIRTH_DATE from NAHAB.TB_IRANIAN_REAL where IDENTIFICATION_NO = {str_melli_code}'



ipQueryList = []
TB_INVOLVED_PARTY = connIcms.execute('select national_code_national_id , birth_date from CRM.TB_INVOLVED_PARTY where fk_lkp_iptype = 1601 and fk_lkp_nationality_type = 9001').fetchall()
for i in range(0,len(TB_INVOLVED_PARTY)):
    ipQueryList.append( ipQueryResponse(TB_INVOLVED_PARTY[i][0],TB_INVOLVED_PARTY[i][1]) )

iRealQueryList = []
TB_IRANIAN_REAL = connNahab.execute('select identification_no , birth_date from  NAHAB.TB_IRANIAN_REAL ire ').fetchall()
for j in range(0,len(TB_IRANIAN_REAL)):
    iRealQueryList.append( iRealQueryResponse(TB_IRANIAN_REAL[j][0],TB_IRANIAN_REAL[j][1]))

failed = ''
for rowsmax in range(0,len(ipQueryList)):
        for rowsNahab in range(0,len(iRealQueryList)):
            if ( ipQueryList[rowsmax].getNatcode() ==  iRealQueryList[rowsmax].getNatcode() ):
                    if ( ipQueryList[rowsmax].getBdate() ==  iRealQueryList.getBdate() ):
                        continue
                    else: 
                        failed += f"{TB_INVOLVED_PARTY[rowsmax].getNatcode()} , {iRealQueryList.getBdate()}"

with open("d:/icmsNahabNocrConflict.txt") as file:
    file.write(failed)

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