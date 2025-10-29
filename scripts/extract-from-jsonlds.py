"""
This scripts uses both pyld and RDFlib to extract tuples from JSON-LD files without the need for framing. It then issues example queries to each method and compares their output.
"""

from pathlib import Path
from pyld import jsonld
import json
from rdflib import Graph

def load_jsonld_files(input_dir):
    """
    Load all JSON-LD files from the provided input directory.

        :param input_dir: The directory where the JSON-LD are stored.
        :returns: The paths of the files and the files themselves as a list.
        :raises FileNotFoundError: An error is printed if no JSON-LD files are found in input_dir.
    """
    print("Files loading....")
    paths = sorted(input_dir.glob("*.jsonld"))
    if not paths:
        raise FileNotFoundError(f"No JSON-LD files found in {input_dir.resolve()}")
        sys.exit(1)
    for p in paths:
        print(f"- {p.name}")
    files = [json.loads(path.read_text(encoding="utf-8")) for path in paths]

    return paths, files
  
#extract using rdflib
def main():
    """
    Holds the main body of the script
    """
    input_dir = Path("JSONLDs")
    paths, files = load_jsonld_files(Path("JSONLDs"))
    
    #g = Graph()
    for file in files:
        print(f"This is the file: {file}.")
    for path in paths:
        print(f"This is the path: {path}.")
    
