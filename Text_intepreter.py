def count_word_in_file(filename, target_word):
    # read entire file and lowercase once
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()

    # characters to strip off the ends of tokens
    punctuation = '.,!?:;()[]{}"“”‘’'

    tw = target_word.lower()
    count = 0
    for token in text.split():
        # remove leading/trailing punctuation
        word = token.strip(punctuation)
        # check exact match or possessive form
        if word == tw or word.startswith(tw + "'s") or word.startswith(tw + "’s"):
            count += 1
    return count

if __name__ == "__main__":
    file_path = 'LebronJames.txt'
    word_to_find = input("Type your word here: ")
    occurrences = count_word_in_file(file_path, word_to_find)
    print(f"The word '{word_to_find}' appears {occurrences} times.")