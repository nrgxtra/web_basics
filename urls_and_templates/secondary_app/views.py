from django.shortcuts import render


def index(req):
    return render(req, 'secondary_app/index.html')

