"""
This scripts uses both pyld and RDFlib to extract tuples from JSON-LD files without the need for framing. It then issues example queries to each method and compares their output.
"""

from pathlib import Path
from rdflib import Graph
from pyld import jsonld
import json

def get_jsonld_files(input_dir):
    """
    Load all JSON-LD files from the provided input directory.

        :param input_dir: The directory where the JSON-LD are stored.
        :returns: The paths of the files as a list.
        :raises FileNotFoundError: An error is printed if no JSON-LD files are found in input_dir.
    """
    print("Files loading............")
    paths = sorted(input_dir.glob("*.jsonld"))
    if not paths:
        raise FileNotFoundError(f"No JSON-LD files found in {input_dir.resolve()}")
        sys.exit(1)
    for path in paths:
        print(f"- {path.name}")

    return paths


def rdflib_extraction(paths):
    for path in paths:
        g = Graph()
        print(f"Extracting information from {path}............")
        g.parse(path, format="json-ld")
        for s, p, o in g:
            print(f"Subject: {s}\nPredicate: {p}\nObject: {o}")


def get_expanded_structure(paths):
    expansions=[]
    for path in paths:
        print(f"Getting expanded structure for {path}............")
        with open(path) as f:
            file = json.load(f)
        expanded = jsonld.expand(file)
        print("Expanded version of file is...")
        print(json.dumps(expanded, indent=4))
        expansions.append(expanded)
        
    return expansions
    

def main():
    """
    Holds the main body of the script
    """
    input_dir = Path("JSONLDs")
    paths = get_jsonld_files(Path("JSONLDs"))
    rdflib_extraction(paths)
    expansions = get_expanded_structure(paths)

        
if __name__ == "__main__":
    main()
