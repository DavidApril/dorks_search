import requests

class GoogleSearch:
    def __init__(self, api_key, search_engine_id):
        """
        Initialize the GoogleSearch class.

        Args:
            api_key (str): The API key.
            search_engine_id (str): The search engine ID.
        """
        self.api_key = api_key
        self.search_engine_id = search_engine_id

    def search(self, query, start_page = 1, pages = 1, lang = 'lang_en'):
        """
        Search for the query.

        Args:
            query (str): The search query.
            start_page (int): The start page.
            pages (int): The number of pages to search.
            lang (str): The language code.
        """
        final_results = []
        results_per_page = 10 # Google allows 10 results per page
        for page in range(pages): 
            start_index = (start_page - 1) * results_per_page + 1 + (page * results_per_page)
            url = f'https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.search_engine_id}&q={query}&start={start_index}&lr={lang}'
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                results = data.get('items', [])
                final_results.extend(results)
            else:
                print(f"Error: {response.status_code}")
        return self.print_results(final_results)

    def print_results(self, results):
        """
        Print the results.

        Args:
            results (list): The results.
        """
        custom_results = []
        for result in results:
            cresults = {}
            cresults['title'] = result.get('title')
            cresults['description'] = result.get('snippet')
            cresults['link'] = result.get('link')
            custom_results.append(cresults)
        return custom_results
