def top_keywords_no_import(docs, top_n=10, max_df=0.8, min_df=2):
    # 1) Simple whitespace‐tokenizer + lowercase + strip punctuation
    punctuation = '.,!?:;()[]{}"\'“”‘’'
    stop_words = {
        'the','and','is','in','it','of','to','a','for','on','with','as',
        'by','that','at','from','this','be','are','or','an','was','were'
    }

    # tokenize & remove stop words
    tokenized = []
    for doc in docs:
        toks = []
        for raw in doc.lower().split():
            w = raw.strip(punctuation)
            if not w or w in stop_words:
                continue
            toks.append(w)
        tokenized.append(toks)

    N = len(docs)

    # 2) document frequency (DF) & filter by max_df/min_df
    df = {}
    for toks in tokenized:
        seen = set()
        for w in toks:
            if w not in seen:
                seen.add(w)
                df[w] = df.get(w, 0) + 1

    # build list of allowed terms
    allowed = {
        w for w, cnt in df.items()
        if cnt >= min_df and cnt / N <= max_df
    }

    # 3) term‐frequency (TF) per document
    tf_list = []
    for toks in tokenized:
        tf = {}
        total = 0
        for w in toks:
            if w in allowed:
                tf[w] = tf.get(w, 0) + 1
                total += 1
        # convert counts → frequencies
        for w in tf:
            tf[w] /= total
        tf_list.append(tf)

    # 4) inverse‐DF (approximate IDF without log)
    idf = { w: N / df[w] for w in allowed }

    # 5) compute TF‐IDF for the first document
    tfidf0 = {
        w: tf_list[0].get(w, 0) * idf[w]
        for w in allowed
    }

    # 6) pick top_n terms
    top = sorted(tfidf0.items(), key=lambda x: x[1], reverse=True)[:top_n]
    print("Top keywords:", top)


if __name__ == "__main__":
    # Example usage:
    docs = [
        open("transcript.txt", encoding="utf-8").read(),
        # add more docs here if needed
    ]
    top_keywords_no_import(docs)