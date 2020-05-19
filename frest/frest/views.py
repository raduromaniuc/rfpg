from django.http import HttpResponse

from rfpg import model


def index(request):
    dcgan = model.DCGAN()
    return HttpResponse("Hello, world. You're at the fpg index.")
