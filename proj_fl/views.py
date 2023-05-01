from django.shortcuts import render
from django.core.cache import cache
from . import words_work
from . import notes_work


def index(request):
    return render(request, "index.html")


def words_list(request):
    words = words_work.get_words_for_table()
    return render(request, "word_list.html", context={"words": words})


def add_word(request):
    return render(request, "word_add.html")


def send_word(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_word = request.POST.get("new_word", "")
        new_transcription = request.POST.get("new_transcription", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        elif len(new_transcription) == 0:
            context["success"] = False
            context["comment"] = "Транскрипция должна быть не пустой"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            words_work.write_word(new_word, new_transcription, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "word_request.html", context)
    else:
        add_word(request)


def show_stats(request):
    stats = words_work.get_words_stats()
    return render(request, "stats.html", stats)

def notes_list(request):
    notes = notes_work.get_notes_for_table()
    return render(request, "note_list.html", context={"notes": notes})


def add_note(request):
    return render(request, "note_add.html")


def send_note(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_note = request.POST.get("new_note", "")
        new_comment = request.POST.get("new_comment", "")
        new_link = request.POST.get("new_link", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_comment) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_note) == 0:
            context["success"] = False
            context["comment"] = "Запись должна быть не пустой"
        elif len(new_link) == 0:
            context["success"] = False
            context["comment"] = "Запись должна быть не пустой(Поставьте хотя бы \"-\")"
        else:
            context["success"] = True
            context["comment"] = "Ваша запись принята"
            notes_work.write_note(new_note, new_comment, new_link)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "note_request.html", context)
    else:
        add_note(request)
