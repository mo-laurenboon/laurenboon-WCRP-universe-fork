from pathlib import Path
import json
from pyld import jsonld

def load_jsonld_files(input_dir)
    paths = sorted(directory.glob("*.jsonld"))
    if not paths:
        raise FileNotFoundError(f"No JSON-LD files found in {directory.resolve()}")
    
    files = [json.loads(path.read_text(encoding="utf-8")) for path in paths]

    return paths, files


def expand_and_merge():
    expanded_graph = []
    for file in files:
        expanded = jsonld.expanded(file)
        expanded_graph.extend(expanded)
        
    print(f"The expanded graph constains {len(merged)} nodes.")

    return expanded_graph


def define_context():
    context = {
        "@vocab": "https://schema.org/",
        "@xsd": "https://www.w3.org/2001/XMLSchema#"
    }

    return context


def compact(expanded_graph, context):
    file = {"@graph": expanded_graph}
    
    return jsonld.compact(file, context)


def frame(context, type_name):

    return {"@context": context, "@type": type_name}


def save_jsonlds(path, data):
    path.write_text(json.dump(data, indent=4, ensure_ascii=False), encoding="utf-8")

def main():

    input_dir = Path("JSONLDs")
    compact_out = input_dir / "merged-comp.jsonld"
    framed_out_dir = input_dir / "framed" 
    framed_paper_out = framed_out_dir / "framed_paper.jsonld"
    framed_authors_out = framed_out_dir / "framed_authors.jsonld"
    framed_institution_out = framed_out_dir / "framed_institution.jsonld"

    paths, files = load_jsonld_files(input_dir)
    print("Files loading....")
    for p in paths:
        print(f"- {p.name}")

    merged = expand_and_merge(files)
    compacted = compact(merged_expanded, context)
    save_jsonlds(compact_out, compacted)

    paper_frame = frame(context, "scholarlyArticle")
    authors_frame = frame(context, "Person")
    institution_frame = frame(context, "Organisation")
    framed_paper = jsonld.frame(compacted, paper_frame)
    framed_authors = jsonld.frame(compacted, authors_frame)
    framed_institution = jsonld.frame(compacted, institution_frame)

    save_josnlds(framed_paper_out, framed_paper)
    save_jsonlds(framed_authors_out, framed_authors)
    save_jsonlds(framed_institution_out, framed_institution)

if __name__ == "__main__":
    main()
