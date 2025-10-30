"""
This scripts uses both pyld and RDFlib to extract tuples from JSON-LD files without the need for framing. It then issues
example queries to each method and compares their output.
"""

from pathlib import Path
from rdflib import Graph, RDF, Namespace
from pyld import jsonld
from collections import Counter
import networkx as nx
import matplotlib.pyplot as plt
from rdflib import URIRef, Literal

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

    return paths


def create_graph(paths):
    """
    Extracts tuples from the provided JSON-LDs using the rdflib module.

        :param paths:  The paths of the file(s).
        :returns: The populated graph.
    """
    g = Graph()
    print(f"Extracting information from {paths}............")
    g.parse(paths, format="json-ld")

    print(f"Loaded {len(g)} triples.\n")

    return g


def bind_namespaces(g):
    """
    Binds the main namespaces with thei prefixes.

        :param g: The populated graph.
        :returns: The populated graph with bound namespace prefixes.
    """
    g.bind("schema", Namespace("https://schema.org/"))
    g.bind("orcid", Namespace("https://orcid.org/"))
    g.bind("doi", Namespace("https://doi.org/"))

    return g


def get_query_results(g):
    """
    Creates the query structure and applies it to the graph.

        :param g: The populated graph with bound namespace prefixes.
        :returns: The result of the query request.
    """
    g = bind_namespaces(g)
    query = """
    PREFIX schema: <https://schema.org/>

    SELECT ?title ?author ?year
    WHERE {
        ?article a schema:ScholarlyArticle ;
                 schema:name ?title ;
                 schema:datePublished ?year ;
                 schema:author ?author .
    }
    """
    results = g.query(query)

    return results


def plot_with_networkx(g, input_dir):
    """"
    Plots the graph structure.

        :param g: The populated graph with bound namespace prefixes.
    """
    G = nx.DiGraph()

    for s, p, o in g:
        s_label = g.qname(s) if isinstance(s, URIRef) else str(s)
        p_label = g.qname(p) if isinstance(p, URIRef) else str(p)
        o_label = g.qname(o) if isinstance(o, URIRef) else str(o)
        G.add_edge(s_label, o_label, label=p_label)

    pos = nx.spring_layout(G, k=0.5, iterations=50)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, font_weight="bold", arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("RDF Graph Visualization for an example paper")
    print(f"Saving plot as {input_dir}/GraphVisualisation.png............")
    plt.savefig(input_dir / "GraphVisualisation.png")


def main():
    """
    Holds the main body of the script
    """
    paths = get_jsonld_files(Path("JSONLDs"))

    for path in paths:
        g = create_graph(path)
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

        results = get_query_results(g)
        for row in results:
            print(f"Title: {row.title}")
            print(f"Author(s): {row.author}")
            print(f"Year: {row.year}")

        plot_with_networkx(g, Path("JSONLDs"))

        
if __name__ == "__main__":
    main()
