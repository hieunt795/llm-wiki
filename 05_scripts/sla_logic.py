import json
import os

MEMORY_FILE = "05_scripts/sla_memory.json"

def init_memory(query):
    memory = {
        "query_chain": [query],
        "evidence": [],
        "state": {"confidence": 0.0, "missing_gaps": [], "iterations": 0},
        "log": []
    }
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, indent=2)

def calculate_confidence(memory):
    # Rule ép RAW: RAW source = 3.0, Wiki = 0.2. 
    # Tích hợp depth (định lượng) để đạt confidence cao nhất.
    raw_sources = [e for e in memory["evidence"] if e.get("source") == "raw"]
    wiki_sources = [e for e in memory["evidence"] if e.get("source") == "wiki"]
    
    # RAW có trọng số gấp 15 lần Wiki để ép hệ thống ưu tiên tìm tài liệu thô
    score = (len(raw_sources) * 3.0) + (len(wiki_sources) * 0.2)
    depth = 0.3 if any("quantified" in str(e).lower() for e in memory["evidence"]) else 0.0
    
    # Chuẩn hóa về thang 0-1
    confidence = min(0.9, (score / 10.0) + depth)
    return round(confidence, 2)

def update_memory(new_data):
    with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
        memory = json.load(f)
    
    # Merge evidence (giữ top-k theo score)
    memory["evidence"].extend(new_data.get("evidence", []))
    memory["evidence"].sort(key=lambda x: x.get("score", 0), reverse=True)
    memory["evidence"] = memory["evidence"][:10] # Giữ top 10
    
    memory["state"]["confidence"] = calculate_confidence(memory)
    memory["state"]["iterations"] += 1
    
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, indent=2)
    return memory
