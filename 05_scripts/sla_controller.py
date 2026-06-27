import argparse
import subprocess
import json
from sla_logic import init_memory, update_memory, MEMORY_FILE

TOOLS = {
    "wiki_search": "python 05_scripts/wiki_search.py",
    "hybrid_search": "python 05_scripts/hybrid_search.py"
}

def run_step(tool_key, query):
    cmd = f"{TOOLS[tool_key]} \"{query}\" --json"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
    try:
        data = json.loads(result.stdout)
        # Tự động cập nhật Gaps nếu tool trả về
        if isinstance(data, dict) and "next_queries" in data:
            return data
        return {"evidence": [], "next_queries": [], "gaps": ["Thiếu nguồn RAW"]}
    except:
        return {"evidence": [], "next_queries": [], "gaps": ["Lỗi parse JSON"]}

def get_adaptive_query(memory):
    """
    Logic tiến hóa query dựa trên Gaps thực tế và độ ưu tiên nguồn RAW.
    """
    # Nếu có gaps từ kết quả trước, tập trung vào đó
    gaps = memory["state"].get("missing_gaps", [])
    query_base = memory["query_chain"][0]
    
    if gaps:
        return f"{query_base} {gaps[0]}"
    
    # Nếu không có gaps, ép tìm nguồn RAW
    return f"{query_base} raw source evidence quantitative data"

def sla_loop(tool_key, query):
    print(f"\n--- [SLA ENGINE START: {query}] ---")
    init_memory(query)
    
    for i in range(3): 
        print(f"\n[Iteration {i+1}]")
        
        # 1. Retrieve
        data = run_step(tool_key, query)
        
        # 2. Update Memory (Bao gồm cập nhật Gaps từ tool)
        memory = update_memory(data)
        
        # 3. Check Stop Condition
        conf = memory["state"]["confidence"]
        print(f"Current Confidence: {conf} (Goal: 0.8)")
        
        if conf >= 0.8:
            print("Confidence target reached. Stopping.")
            break
            
        # 4. Plan Next Query (Adaptive)
        query = get_adaptive_query(memory)
        print(f"Evolving to: {query}")

    print("\n--- [FINAL SYNTHESIS READY] ---")
    print("Memory stored in 05_scripts/sla_memory.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", choices=TOOLS.keys(), required=True)
    parser.add_argument("--query", required=True)
    args = parser.parse_args()
    
    sla_loop(args.tool, args.query)
