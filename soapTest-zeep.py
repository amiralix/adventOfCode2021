import zeep
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep.transports import Transport
from zeep import helpers

wsdl_url = 'https://gsbservices.iran.gov.ir/ghovehghazaeye/LegalPersonServiceJIX?wsdl'
session = Session()
session.auth = HTTPBasicAuth('mellibank_gsb', 'm3l!b4nk@gsb1395')
client = zeep.Client(wsdl=wsdl_url , transport=Transport(session=session))
request = client.get_type('ns2:Parameter')
my_request = request(Date = "" , Name="",NationalCode = '10862064732' , PassWord =  'MeliBank.Service', UserName ='MeliBank.Service')
InquirySpecialByNationalCodeResponse = client.service.InquirySpecialByNationalCode(my_request)
result =  helpers.serialize_object(InquirySpecialByNationalCodeResponse)
print(result) #result is a dictionary