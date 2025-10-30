"""
This scripts uses both pyld and RDFlib to extract tuples from JSON-LD files without the need for framing. It then issues
example queries to each method and compares their output.
"""

import sys
from pathlib import Path
from rdflib import Graph, RDF, Namespace
from pyld import jsonld
import json
from collections import Counter

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

def get_test_jsonld_file(input_dir, test_file_name):
    """
    Load a singular test JSON-LD file from the provided input directory.

        :param input_dir: The directory where the JSON-LD are stored.
        :returns: The paths of the file.
        :raises FileNotFoundError: An error is printed if no JSON-LD files are found in input_dir.
    """
    print("Test file loading............")
    paths = input_dir / test_file_name
    if not paths:
        raise FileNotFoundError("No JSON-LD file with that name found.")
        sys.exit(1)

    return paths


def rdflib_extraction(paths):
    """
    Extracts tuples from the provided JSON-LDs using the rdflib module.

        :param paths:  The paths of the files as a list.
    """
    g = Graph()
    print(f"Extracting information from {paths}............")
    g.parse(paths, format="json-ld")

    print(f"Loaded {len(g)} triples.\n")

    print("=============================TRIPLES===================================")
    for s, p, o in g:
        print(f"Subject: {s} -- Predicate: {p} --> Object: {o}")

    print("\n===================== Namespaces / Prefixes =====================")
    for prefix, namespace in g.namespaces():
        print(f"{prefix}: {namespace}")

    print("\n===================== RDF Types (Classes) =====================")
    for s, o in g.subject_objects(RDF.type):
        print(f"{s} a {o}")

    pred_counts = Counter(p for _, p, _ in g)
    print("\n===================== Predicate Frequency =====================")
    for p, count in pred_counts.items():
        print(f"{p} : {count}")

    #bind main namespaces
    g.bind("schema", Namespace("https://schema.org/"))
    g.bind("orcid", Namespace("https://orcid.org/"))
    g.bind("doi", Namespace("https://doi.org/"))


    query = """
    PREFIX schema: <https://schema.org/>

    SELECT ?title ?year
    WHERE {
        ?article a schema:ScholarlyArticle ;
                 schema:name ?title ;
                 schema:datePublished ?year .
    }
    """
    results = g.query(query)

    for row in results:
        print(f"Title: {row.title}")
        print(f"Year: {row.year}")
 

def get_expanded_structure(paths):
    """
    Generates an expanded structure for each of the JSON-LD files 

        :param paths:  The paths of the files as a list.
    """
    expansions=[]
    print(f"Getting expanded structure for {paths}............")
    with open(paths) as f:
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
    paths = get_test_jsonld_file(Path("JSONLDs"), "paper.jsonld")
    rdflib_extraction(paths)


        
if __name__ == "__main__":
    main()
