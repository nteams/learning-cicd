from django.http import HttpResponse


def usercenter(request):
    return HttpResponse("Hello, world. You're at the usercenter index.")