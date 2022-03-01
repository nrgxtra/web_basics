from django.http import HttpResponse
from django.shortcuts import render, redirect

from django101.cities.models import Person


def show_forms_demo(request):
    return render(request, 'forms_demo.html')


def index(req):
    context = {
        'name': 'Kiril',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)


def test_index(req):
    return HttpResponse('{"name": "Kiril"}', content_type='application/json')


def create_person(req):
    Person(
        name='Goshkata',
        age='14',
        home_town='Sofia',
    ).save()

    return redirect('/cities')


def list_phones(req):
    context = {
        'phones': [
            {'name': 'Galaxy S21', 'quantity': 3},
            {'name': 'Iphone 13', 'quantity': 0},
            {'name': 'Xiaomi Redmi Note 9', 'quantity': 5},
        ]
    }
    # return HttpResponse('Phones list')
    context['message'] = 'Phones list'
    return render(req, 'phones.html', context)
