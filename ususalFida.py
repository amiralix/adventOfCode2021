import pandas as pd
from roohanion_faragir import rooahanioon_faragir
import time
import math
import numpy as np

print(f'reading File...')  
data = pd.read_csv("d:/faragir_must_inq_by_shahab.csv")
for rows in range(0,len(data)):
            fida_code = str(data.FIDA_CODE[rows])
            idDocNumber = str(data.IDENTITY_DOCUMENT_ID[rows])
            birthDate = str(data.BIRTH_DATE[rows])
            birthCountry = data.FK_LOC_GEOLOCATION_ID_COUNTRY[rows]
            if (birthCountry.astype(np.float64)):
                birthCountry = 103167
            shahabinq = rooahanioon_faragir.shahbInq(fida_code , idDocNumber,birthDate ,math.ceil(birthCountry),False)
            if (shahabinq is not None and shahabinq[0] == 200 and shahabinq[1]['response']['personInfo']['shahabCode'] is None ):
                time.sleep(1)
                shahabinq = rooahanioon_faragir.shahbInq(fida_code , idDocNumber,birthDate ,math.ceil(birthCountry),True)
            else: continue

            



    