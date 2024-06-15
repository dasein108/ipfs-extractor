

def glue_summary_text(summary):
    words = summary.split()
    processed_words = []
    for word in words:
        if word.startswith("##"):
            if processed_words:
                processed_words[-1] += word[2:]
            else:
                processed_words.append(word[2:])
        else:
            processed_words.append(word)
    return ' '.join(processed_words)