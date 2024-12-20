from dotenv import load_dotenv, set_key
from google_search import GoogleSearch
import argparse
import os
import sys

def env_setup():
    """
    Configure the API key and search engine ID
    """
    api_key = input('Enter your Google API key: ')
    search_engine_id = input('Enter your Google Search Engine ID: ')
    set_key('.env', 'GOOGLE_API_KEY', api_key)
    set_key('.env', 'SEARCH_ENGINE_ID', search_engine_id)

def main(args):

    env_exists = os.path.exists('.env')
    if not env_exists or args.configure:
        env_setup()
        print('API key and search engine ID configured successfully.')
        sys.exit(1)
        
    load_dotenv()

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')
    
    if not args.query:
        print('Please provide a query to search for. -q "query"')
        sys.exit(1)
 
    gsearch = GoogleSearch(GOOGLE_API_KEY, SEARCH_ENGINE_ID)
    results = gsearch.search(args.query, args.start_page, args.pages, args.lang)

    gsearch.print_results(results)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ninja Dorks')
    parser.add_argument('-q', '--query', type=str, help='The dork to search for\ne.g. "filetype:sql "MySQL dump" (pass|password|passwd|pwd)"')
    parser.add_argument('-s', '--start-page', type=int, help='The page to start searching from')
    parser.add_argument('-p', '--pages', type=int, help='The number of pages to search')
    parser.add_argument('-l', '--lang', type=str, help='The language to search')
    parser.add_argument('-c', '--configure', action='store_true', help='Configure the API key and search engine ID')
    parser.add_argument('--json', action='store_true', help='Export the results to a JSON file')
    parser.add_argument('--html', action='store_true', help='Export the results to an HTML file')
    args = parser.parse_args()
    main(args)