import requests
from dotenv import load_dotenv
import os
from google_search import GoogleSearch

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')

query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'

gsearch = GoogleSearch(GOOGLE_API_KEY, SEARCH_ENGINE_ID)
results = gsearch.search(query, 1, 1, 'lang_en')
