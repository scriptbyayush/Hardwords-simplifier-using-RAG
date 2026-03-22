from cwi import detect_hard_words
from retriever import retrieve
from generator import simplify

def run_pipeline(text):
    hard_words = detect_hard_words(text)
    meanings = retrieve(hard_words)
    output = simplify(text, meanings)
    return output