from pathlib import Path
import json
from pyld import jsonld

def load_jsonld_files(input_dir):
    paths = sorted(input_dir.glob("*.jsonld"))
    if not paths:
        raise FileNotFoundError(f"No JSON-LD files found in {input_dir.resolve()}")
    
    files = [json.loads(path.read_text(encoding="utf-8")) for path in paths]

    return paths, files


def expand_and_merge(files):
    expanded_graph = []
    for file in files:
        expanded = jsonld.expand(file)
        expanded_graph.extend(expanded)
        
    print(f"The expanded graph constains {len(expanded_graph)} nodes.")

    return expanded_graph


def build_context(files):
    fallback = "https://schema.org/"
    combined = []
    combined.append({"vocab": fallback, "xsd": "https://www.w3.org/2001/XMLSchema#"})
    for file in files:
        con = file.get("@context")
        if not con:
            continue
        if isinstance(con, list):
            combined.extend(con)
        else:
            combined.append(con)
    seen = []
    deduped = []
    for item in combined:
        key = repr(item)
        if key not in seen:
            seen.append(key)
            deduped.append(item)

    return deduped


def compact(expanded_graph, context):
    file = {"@graph": expanded_graph}
    
    return jsonld.compact(file, context)


def frame(context, type_name):

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
