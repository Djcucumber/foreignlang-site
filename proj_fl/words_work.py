def get_words_for_table():
    words = []
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            word, transcription, definition, source = line.split(";")
            words.append([cnt, word, transcription, definition])
            cnt += 1
    return words


def write_word(new_word, new_transcription, new_definition):
    new_word_line = f"{new_word};{new_transcription};{new_definition};user"
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        existing_words = [l.strip("\n") for l in f.readlines()]
        title = existing_words[0]
        old_words = existing_words[1:]
    words_sorted = old_words + [new_word_line]
    words_sorted.sort()
    new_words = [title] + words_sorted
    with open("./data/words.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_words))


def get_words_stats():
    db_words = 0
    user_words = 0
    defin_len = []
    with open("./data/words.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            word, trans, defin, added_by = line.split(";")
            words = defin.split()
            defin_len.append(len(words))
            if "user" in added_by:
                user_words += 1
            elif "db" in added_by:
                db_words += 1
    stats = {
        "words_all": db_words + user_words,
        "words_own": db_words,
        "words_added": user_words,
        "words_avg": round(sum(defin_len)/len(defin_len), 2),
        "words_max": max(defin_len),
        "words_min": min(defin_len)
    }
    return stats
