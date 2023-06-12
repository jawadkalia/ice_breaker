import os
from dotenv import load_dotenv

def load_env():
    load_dotenv()
    os.environ['OPENAI_API_KEY']
    os.environ['PROXYCURL_API_KEY']
    os.environ['PROXYCURL_CACHE_URL']
    os.environ['PROXYCURL_CACHE_URL2']