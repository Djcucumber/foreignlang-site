from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import notes_work


def index(request):
    return render(request, "index.html")


def terms_list(request):
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})


def add_term(request):
    return render(request, "term_add.html")


def send_term(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def show_stats(request):
    stats = terms_work.get_terms_stats()
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
