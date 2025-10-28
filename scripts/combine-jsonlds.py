"""
This script is deigned to merge and expand linked JSON-LD files by creating graphs. It also outputs framed versions of each input
file.
"""

import sys
from pathlib import Path
import json
from pyld import jsonld

def load_jsonld_files(input_dir):
    """
    Load all JSON-LD files from the provided input directory.

        :param input_dir: The directory where the JSON-LD are stored.
        :returns: The paths of the files and the files themselves as a list.
        :raises FileNotFoundError: An error is printed if no JSON-LD files are found in input_dir.
    """
    paths = sorted(input_dir.glob("*.jsonld"))
    if not paths:
        raise FileNotFoundError(f"No JSON-LD files found in {input_dir.resolve()}")
        sys.exit(1)
    
    files = [json.loads(path.read_text(encoding="utf-8")) for path in paths]

    return paths, files


def expand_and_merge(files):
    """
    Combines and marges the JSON-LD files to a single path.

        :param files: The JSON-LD files as type list.
        :returns: The combined and expanded graph of all JSON-LD files in the list.
    """
    expanded_graph = []
    for file in files:
        expanded = jsonld.expand(file)
        expanded_graph.extend(expanded)
        
    print(f"The expanded graph constains {len(expanded_graph)} nodes.")

    return expanded_graph


def build_context(files):
    """
    Generates the combined context for framing and implants a fallback context if none is provided, as well as hadnling 
    duplicates if the same context is provided mutliple times.

        :param files: The JSON-LD files as type list.
        :returns: The deduplicated context.
    """
    combined = []
    for file in files:
        con = file.get("@context")
        if not con:
            continue
        if isinstance(con, list):
            combined.extend(con)
        else:
            combined.append(con)
    if not combined:
        combined.append({"vocab": "https://schema.org/", "xsd": "https://www.w3.org/2001/XMLSchema#"})
        
    seen = []
    deduped = []
    for item in combined:
        key = repr(item)
        if key not in seen:
            seen.append(key)
            deduped.append(item)

    return deduped


def compact(expanded_graph, context):
    """
    Compacts the expanded graph and applies the context.

        :param expanded_graph: The combined and expanded graph of all JSON-LD files in the list.
        :param context: The deduplicated context parameters.
        :returns: The compacted file.
    """
    file = {"@graph": expanded_graph}
    
    return jsonld.compact(file, context)


def frame(context, type_name):
    """
    Generates the framed versions of each JSON-LD file.

        :param context: The deduplicated context parameters.
        :param type_name: The type variable.
        :returns: The a framed version of the input JSON-LD file.
    """

    return {"@context": context, "@type": type_name}


def save_jsonlds(path, data):
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():

    input_dir = Path("JSONLDs")
    compact_out = input_dir / "merged-comp.jsonld"
    framed_out_dir = input_dir / "framed" 
    framed_out_dir.mkdir(parents=True, exist_ok=True)
    framed_paper_out = framed_out_dir / "framed_paper.jsonld"
    framed_authors_out = framed_out_dir / "framed_authors.jsonld"
    framed_institution_out = framed_out_dir / "framed_institution.jsonld"

    paths, files = load_jsonld_files(input_dir)
    print("Files loading....")
    for p in paths:
        print(f"- {p.name}")

    merged = expand_and_merge(files)
    context = build_context(files)
    compacted = compact(merged, context)
    save_jsonlds(compact_out, compacted)

    paper_frame = frame(context, "scholarlyArticle")
    authors_frame = frame(context, "Person")
    institution_frame = frame(context, "Organisation")
    framed_paper = jsonld.frame(compacted, paper_frame)
    framed_authors = jsonld.frame(compacted, authors_frame)
    framed_institution = jsonld.frame(compacted, institution_frame)

    save_jsonlds(framed_paper_out, framed_paper)
    save_jsonlds(framed_authors_out, framed_authors)
    save_jsonlds(framed_institution_out, framed_institution)

if __name__ == "__main__":
    main()
