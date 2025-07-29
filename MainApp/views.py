from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

# def home(request):
#     text ="""
#     <h1>"Изучаем django"</h1>
#     <strong>Автор</strong>: <i>Иванов И.П.</i>
#     """
#     return HttpResponse(text)

def home(request) -> HttpResponse:
    context = {
        "name": "Иванов Иван Иванович",
        "email": "mail@mail.ru"
    }
    return render(request, "index.html", context)
"""
    author = {
        "Имя": "Иван",
        "Отчество": "Петрович",
        "Фамилия": "Иванов",
        "телефон": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
"""


def about(request):
    author = {
        "name": "Иван",
        "middle_name": "Петрович",
        "last_name": "Иванов",
        "phone": "8-923-600-01-02",
        "email": "vasya@mail.ru",
    }
    context = {
        'author': author
    }
    return render(request, "about.html", context)



def get_item(request, item_id: int):
    """ По указанному id возвращает элемент из DB"""
    try:    
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {'errors': [f'Item with id={item_id} not found']})
    else:
        return render(request, "item_page.html", {"item": Item.objects.get(id=item_id)})


def get_items(request):
    return render(request, "items_list.html", {"items": Item.objects.all()})


# Проверка урла
# def get_item(request, item_id: int):
#     return HttpResponseNotFound(item_id)