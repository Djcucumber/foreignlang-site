def get_notes_for_table():
    notes = []
    with open("./data/notes.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            note, comment, source = line.split(";")
            notes.append([cnt, note, comment])
            cnt += 1
    return notes


def write_note(new_note, new_comment):
    new_note_line = f"{new_note};{new_comment};user"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_notes = [l.strip("\n") for l in f.readlines()]
        title = existing_notes[0]
        old_notes = existing_notes[1:]
    notes_sorted = old_notes + [new_note_line]
    notes_sorted.sort()
    new_notes = [title] + notes_sorted
    with open("./data/notes.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_notes))
