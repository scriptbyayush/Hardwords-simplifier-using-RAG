import json

with open("data/knowledge.json", "r", encoding="utf-8") as f:
    kb = json.load(f)

def retrieve(words):
    return {w: kb.get(w, "N/A") for w in words}