import json
from rich.console import Console
from rich.table import Table

class ResultsProcessor:
    """
    Process and export results from Google Dorks search.
    """
    def __init__(self, results):
        """
        Initialize the ResultsProcessor class.

        Args:
            results (list of dict): The results to process.
        """
        self.results = results

    def export_html(self, output_file):
        """Export the results to an HTML file based on a template.

        Args:
            output_file (str): The name of the output file where the HTML will be saved.
        """
        with open("html_template.html", 'r', encoding='utf-8') as f:
            plantilla = f.read()

        html_elements = ''
        for index, result in enumerate(self.results, start=1):
            element = f'<div class="result">' \
                       f'<div class="index">result {index}</div>' \
                       f'<h5>{result["title"]}</h5>' \
                       f'<p>{result["description"]}</p>' \
                       f'<a href="{result["link"]}" target="_blank">{result["link"]}</a>' \
                       f'</div>'
            html_elements += element
        
        html_content = plantilla.replace('{{ results }}', html_elements)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Results exported to HTML. File created: {output_file}")

    def export_json(self, output_file):
        """Export the results to a JSON file.

        Args:
            output_file (str): The name of the output file where the JSON will be saved.
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=4)
        print(f"Results exported to JSON. File created: {output_file}")

    def show_results(self):
        """Show the results in the console using a formatted table."""
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim")
        table.add_column("Titulo", width=50)
        table.add_column("Descripcion")
        table.add_column("Enlace")

        for index, result in enumerate(self.results, start=1):
            table.add_row(str(index), result['title'], result['description'], result['link'])
            table.add_row("", "", "", "")
        console.print(table)