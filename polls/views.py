from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. Guyot tiene olor a pata, Hace una semana que no se baña ")
    
