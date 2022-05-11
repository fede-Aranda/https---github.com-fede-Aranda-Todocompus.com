from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. \n Guyot tiene olor a pata, \n Hace una semana que no se baña ")
    return render(request,index.html)
