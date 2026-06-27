import os
import json
import re
import yaml

WIKI_DIR = "03_wiki"
SOURCES_DIR = "02_sources"
GRAPH_JSON = "graphify-out/graph.json"

def parse_wiki_node(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Extract frontmatter
    fm_match = re.search(r"^---\s+(.*?)\s+---", content, re.DOTALL)
    fm = {}
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1))
        except:
            pass
            
    title = fm.get("title", os.path.basename(file_path))
    thesis = fm.get("thesis", "No thesis provided.")
    source_refs = fm.get("source_refs", [])
    
    # Extract wikilinks
    links = re.findall(r"\[\[(.*?)\]\]", content)
    
    return {
        "id": os.path.splitext(os.path.basename(file_path))[0],
        "label": title,
        "thesis": thesis,
        "links": links,
        "source_refs": source_refs,
        "source_file": file_path
    }

def main():
    if not os.path.exists(GRAPH_JSON):
        print(f"Error: {GRAPH_JSON} not found.")
        return

    with open(GRAPH_JSON, "r", encoding="utf-8") as f:
        graph_data = json.load(f)

    existing_node_ids = {n["id"] for n in graph_data["nodes"]}
    
    new_nodes = []
    new_edges = []

    # 1. Process Raw Sources
    print("Processing Raw Sources...")
    for root, _, files in os.walk(SOURCES_DIR):
        for file in files:
            if not file.endswith(".md"):
                continue
            source_id = os.path.splitext(file)[0]
            source_node = {
                "label": source_id.replace("_", " "),
                "file_type": "document",
                "source_file": os.path.join(root, file),
                "source_location": "L1",
                "id": source_id,
                "community": 20,
                "norm_label": source_id
            }
            if source_id not in existing_node_ids:
                new_nodes.append(source_node)
            else:
                # Update existing node in graph_data
                for n in graph_data["nodes"]:
                    if n["id"] == source_id:
                        n.update(source_node)
                        break

    # 2. Process Wiki Nodes
    print("Processing Wiki Nodes...")
    # Clear old edges for updated nodes to avoid duplicates if needed, but for now we just append new edges
    # A better way would be to manage edges by ID too.
    
    # RAW_FILTER_LINK: loại bỏ page anchors và .md# references khỏi wikilinks
    LINK_FILTER = re.compile(r'\.md#|#page=|#p=|\|', re.I)

    for root, _, files in os.walk(WIKI_DIR):
        for file in files:
            # Skip auto-generated index files và hidden files
            if not file.endswith(".md") or file.startswith("_") or file.startswith("."):
                continue
            node_data = parse_wiki_node(os.path.join(root, file))

            wiki_node = {
                "label": node_data["label"],
                "file_type": "document",
                "source_file": node_data["source_file"],
                "source_location": "L1",
                "id": node_data["id"],
                "community": 10,
                "norm_label": node_data["label"]
            }

            rat_id = f"{node_data['id']}_thesis"
            rat_node = {
                "label": node_data["thesis"],
                "file_type": "rationale",
                "source_file": node_data["source_file"],
                "source_location": "L1",
                "id": rat_id,
                "community": 10,
                "norm_label": node_data["thesis"][:50]
            }

            if node_data["id"] not in existing_node_ids:
                new_nodes.append(wiki_node)
                new_nodes.append(rat_node)
                new_edges.append({
                    "source": node_data["id"],
                    "target": rat_id,
                    "label": "has_thesis",
                    "type": "rationale_for"
                })
            else:
                # Update existing
                for n in graph_data["nodes"]:
                    if n["id"] == node_data["id"]:
                        n.update(wiki_node)
                    if n["id"] == rat_id:
                        n.update(rat_node)

            # Add edges for wikilinks — filter out page anchors, .md# refs, pipe aliases
            for link in node_data["links"]:
                target_id = link.split("|")[0].strip()
                # Skip page-anchor refs and .md extension refs
                if LINK_FILTER.search(target_id):
                    continue
                # Skip empty or very short targets
                if len(target_id) < 3:
                    continue
                new_edges.append({
                    "source": node_data["id"],
                    "target": target_id,
                    "label": "links_to",
                    "type": "reference"
                })

            # Add edges to Raw Sources (if cited) — runs ONCE per node, not per link
            for ref in node_data["source_refs"]:
                if isinstance(ref, dict):
                    ref_file = ref.get("file", "")
                elif isinstance(ref, str):
                    ref_file = ref
                else:
                    ref_file = ""

                if "Alexander During" in ref_file:
                    match = re.search(r"-(\d+)\.pdf", ref_file)
                    if match:
                        ch_num = match.group(1)
                        ch_padded = ch_num.zfill(2) if int(ch_num) < 10 else ch_num
                        source_node_id = f"Fixed_Income_Alexander_During_Ch{ch_padded}"
                        new_edges.append({
                            "source": node_data["id"],
                            "target": source_node_id,
                            "label": "derived_from",
                            "type": "provenance"
                        })
                elif "Perry" in ref_file:
                    match = re.search(r"_P(\d+)", ref_file)
                    if match:
                        p_num = match.group(1)
                        source_node_id = f"Perry_Central_Bank_Policy_P{p_num}"
                        new_edges.append({
                            "source": node_data["id"],
                            "target": source_node_id,
                            "label": "derived_from",
                            "type": "provenance"
                        })

    graph_data["nodes"].extend(new_nodes)
    graph_data["links"].extend(new_edges)

    with open(GRAPH_JSON, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, indent=2)

    print(f"Successfully injected {len(new_nodes)} nodes/rationales and {len(new_edges)} edges into the graph.")

if __name__ == "__main__":
    main()
