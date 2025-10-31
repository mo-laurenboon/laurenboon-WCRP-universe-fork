"""
This scripts extracts tuples from JSON-LD files without the need for framing. It then issues example SPARQL queries and 
plots resulting graph for each indvidual file as well as the combined graph.
"""

from rdflib import Graph, RDF, Namespace
from collections import Counter
from rdflib import URIRef
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

def get_jsonld_file_paths(input_dir):
    """
    """
    print("Files loading............")
    paths = sorted(input_dir.glob("*.jsonld"))
    if not paths:
        raise FileNotFoundError(f"No JSON-LD files found in {input_dir.resolve()}")
    for path in paths:
        print(f"- {path.name}")

    return paths


def create_individual_graph(path):
    """
    """
    g = Graph()
    print(f"\nEXTRACTING INFORMATION FROM {path}............")
    g.parse(path, format="json-ld")

    print(f"Loaded {len(g)} triples............")

    return g

def create_combined_graph(g, path):
    """
    """
    print(f"\nEXTRACTING INFORMATION FROM {path}............")
    g.parse(path, format="json-ld")

    print(f"Loaded {len(g)} triples............")

    return g


def print_triples(g):
    """
    """
    print("============================ TRIPLES ============================")
    for s, p, o in g:
        print(f"Subject: {s} -- Predicate: {p} --> Object: {o}")
    print("============================ Namespaces / Prefixes ============================")
    for prefix, namespace in g.namespaces():
        print(f"{prefix}: {namespace}")
    print("============================ RDF Types (Classes) ============================")
    for s, o in g.subject_objects(RDF.type):
        print(f"{s} a {o}")
    pred_counts = Counter(p for _, p, _ in g)
    print("============================ Predicate Frequency ============================")
    for p, count in pred_counts.items():
        print(f"{p} : {count}")


def bind_namespaces(g):
    """
    """
    g.bind("schema", Namespace("https://schema.org/"))
    g.bind("orcid", Namespace("https://orcid.org/"))
    g.bind("doi", Namespace("https://doi.org/"))

    return g


def get_query_results(g):
    """
    """
    g = bind_namespaces(g)
    query = """
    PREFIX schema: <https://schema.org/>

    SELECT ?title ?author ?year ?url ?email
    WHERE {
        ?article a schema:ScholarlyArticle ;
                 schema:name ?title ;
                 schema:datePublished ?year ;
                 schema:author ?author ;
                 schema:url ?url ;
                 schema:email ?email ;
    }
    """
    results = g.query(query)

    for row in results:
        try:
            print(f"Title: {row.title}")
            print(f"Author(s): {row.author}")
            print(f"Year: {row.year}")
            print(f"url: {row.url}")
            print(f"Email: {row.email}")
        except:
            pass 


def get_type_colour_map(g):
    """
    """
    type_map = {}
    for s, _, o in g.triples((None, RDF.type, None)):
        s_label = g.qname(s) if isinstance(s, URIRef) else str(s)
        o_label = g.qname(o) if isinstance(o, URIRef) else str(o)
        type_map[s_label] = o_label.split(":")[-1]  
    print(type_map)       #delete later, print for testing -------------------------------------------------------------------

    colour_map = {
        "Person": "skyblue",
        "Paper": "darkseagreen",
        "Organization": "mediumpurple"
    }

    return type_map, colour_map


def plot_individual_graphs(g, paths, input_dir):
    """
    """
    G = nx.DiGraph()
    for s, p, o in g:
        s_label = g.qname(s) if isinstance(s, URIRef) else str(s)
        p_label = g.qname(p) if isinstance(p, URIRef) else str(p)
        o_label = g.qname(o) if isinstance(o, URIRef) else str(o)
        G.add_edge(s_label, o_label, label=p_label)
    
    combined_type_map = {}
    combined_colour_map = {}

    for path in paths:
        comb_graph = create_individual_graph(path)
        type_map, colour_map = get_type_colour_map(comb_graph)
        combined_type_map.update(type_map)
        combined_colour_map.update(colour_map)

    node_colour = []
    for node in G.nodes():
        node_type = type_map.get(node, "Unknown")
        node_colour.append(colour_map.get(node_type, "grey"))

    pos = nx.spring_layout(G, k=0.5, iterations=50)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colour, node_size=2000, font_size=10, font_weight="bold", 
            arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("RDF Graph Visualization for an example paper")
    figurename = f"GraphVisualisation_{paths.stem}.png"
    print(f"SAVING PLOT AS {input_dir}/{figurename}............\n")
    plt.savefig(input_dir / figurename)


def plot_combined_graph(g, input_dir):
    """
    """
    G = nx.DiGraph()
    for s, p, o in g:
        s_label = g.qname(s) if isinstance(s, URIRef) else str(s)
        p_label = g.qname(p) if isinstance(p, URIRef) else str(p)
        o_label = g.qname(o) if isinstance(o, URIRef) else str(o)
        G.add_edge(s_label, o_label, label=p_label)
    
    type_map, colour_map = get_type_colour_map(g)

    node_colour = []
    for node in G.nodes():
        node_type = type_map.get(node, "Unknown")
        node_colour.append(colour_map.get(node_type, "grey"))

    pos = nx.spring_layout(G, k=0.5, iterations=50)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color=node_colour, node_size=2000, font_size=10, font_weight="bold", 
            arrows=True)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("RDF Graph Visualization for an example paper")
    figurename = f"GraphVisualisation_COMBINED.png"
    print(f"SAVING PLOT AS {input_dir}/{figurename}............\n")
    plt.savefig(input_dir / figurename)


def main():
    """
    """

    #for each individual JSONLD file
    paths = get_jsonld_file_paths(Path("JSONLDs"))
    for path in paths:
        g = create_individual_graph(path)
        print_triples(g)
        get_query_results(g)
        plot_individual_graphs(g, paths, Path("JSONLDs"))

    #for combined JSONLD file
    g=Graph()
    for path in paths:
        g = create_combined_graph(g, path)
    print_triples(g)
    get_query_results(g)
    plot_combined_graph(g, Path("JSONLDs"))


if __name__ == "__main__":
    main()

