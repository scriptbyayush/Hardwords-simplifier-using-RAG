def detect_hard_words(text):
    simple_words = ["यह", "है", "से", "और", "का", "में"]
    words = text.split()
    hard_words = [w for w in words if w not in simple_words]
    return hard_words