from django.http import HttpResponse


def servercenter(request):
    return HttpResponse("Hello, world. You're at the servercenter index.")