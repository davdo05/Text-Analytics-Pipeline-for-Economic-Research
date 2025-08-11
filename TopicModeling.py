def simple_topic_modeling(docs, num_topics=5, top_n=10):
    # punctuation to strip off each token
    punctuation = '.,!?:;()[]{}"“”‘’'
    
    # 1) tokenize & lowercase
    texts = []
    for doc in docs:
        words = []
        for tok in doc.lower().split():
            w = tok.strip(punctuation)
            if w:
                words.append(w)
        texts.append(words)
    
    # 2) prepare counters for each topic
    topic_word_counts = [ {} for _ in range(num_topics) ]
    
    # 3) assign every word to a topic via hash, count frequencies
    for words in texts:
        for word in words:
            topic = hash(word) % num_topics
            cnt = topic_word_counts[topic]
            cnt[word] = cnt.get(word, 0) + 1
    
    # 4) print top words per “topic”
    for idx, cnt in enumerate(topic_word_counts):
        # sort words by descending freq
        top_words = sorted(cnt.items(), key=lambda x: x[1], reverse=True)[:top_n]
        print(f"Topic {idx}:", [w for w, _ in top_words])

if __name__ == "__main__":
    # example: read all docs from disk
    docs = []
    for fname in ["LebronJames.txt"]: #using an example txt file
        with open(fname, encoding="utf-8") as f:
            docs.append(f.read())
    simple_topic_modeling(docs, num_topics=5, top_n=8)