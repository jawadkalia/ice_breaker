import requests
import os

from dotenv import load_dotenv

load_dotenv()
value = os.environ['PROXYCURL_API_KEY']

api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/profile/resolve'
api_key = os.getenv("PROXYCURL_API_KEY")
header_dic = {'Authorization': 'Bearer ' + api_key}
params = {
    'first_name': 'Jawad',
    'company_domain': 'Signify Health',
    'similarity_checks': 'include',
    'enrich_profile': 'enrich',
    'last_name': 'Kalia',
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)

print(response.json())