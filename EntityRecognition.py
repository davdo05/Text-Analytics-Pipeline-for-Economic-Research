def is_date(token):
    t = token.strip(".,")
    # simple numeric dates like 2025-05-27 or 05/27/2025
    if (("-" in t or "/" in t) and
        all(part.isdigit() for part in t.replace("-", "/").split("/"))):
        return True
    # month names
    months = ("january","february","march","april","may","june",
              "july","august","september","october","november","december")
    if t.lower().strip(".,").rstrip("stndrh").lower() in months:
        return True
    return False

def is_money(token):
    t = token.strip(".,")
    return t.startswith("$") and any(ch.isdigit() for ch in t)

def is_org(token):
    t = token.strip(".,")
    # common suffixes
    for suf in ("Inc","Corp","Ltd","LLC","GmbH","SA","Co"):
        if t.endswith(suf):
            return True
    # title-case heuristic (but skip pure sentence starts)
    return t.istitle() and len(t) > 1

def extract_ents(text):
    ents = []
    for tok in text.split():
        if is_date(tok):
            ents.append((tok.strip(".,") , "DATE"))
        elif is_money(tok):
            ents.append((tok.strip(".,") , "MONEY"))
        elif is_org(tok):
            ents.append((tok.strip(".,") , "ORG"))
    return ents

def freq_count(ents):
    freq = {}
    for _, label in ents:
        freq[label] = freq.get(label, 0) + 1
    return freq

if __name__ == "__main__":
    txt = open("LebronJames.txt", encoding="utf-8").read()
    ents = extract_ents(txt)
    print("Entities found:", ents)
    print("Frequencies:", freq_count(ents))